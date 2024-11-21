======================================================
vers: a mostly universal version range specifier
======================================================

This specification is a new syntax for dependency and vulnerable version ranges.


Context
--------

Software package version ranges and version constraints are essential:

- When resolving the dependencies of a package to express which subset of the
  versions are supported. For instance a dependency or requirement statement
  such as "I require package foo, version 2.0 or later versions" defines a
  range of acceptable foo versions.

- When stating that a known vulnerability or bug affects a range of package
  versions. For instance a security advisory such as "vulnerability 123 affects
  package bar, version 3.1 and version 4.2 but not version 5" defines a range of
  vulnerable "bar" package versions.

Version ranges can be replaced by a list enumerating all the versions of
interest. But in practice, all the versions may not yet exist when defining an
open version range such as "v2.0 or later".

Therefore, a version range is a necessary, compact and practical way to
reference multiple versions rather than listing all the versions.


Problem
--------

Several version range notations exist and have evolved separately to serve the
specific needs of each package ecosystem, vulnerability databases and tools.

There is no (mostly) universal notation for version ranges and there is no
universal way to compare two versions, even though the concepts that exist in
most version range notations are similar.

Each package type or ecosystem may define their own ranges notation and version
comparison semantics for dependencies. And for security advisories, the lack of
a portable and compact notation for vulnerable package version ranges means that
these ranges may be either ambiguous or hard to compute and may be best replaced
by complete enumerations of all impacted versions, such as in the `NVD CPE Match
feed <https://nvd.nist.gov/vuln/data-feeds#cpeMatch>`_.

Because of this, expressing and resolving a version range is often a complex, or
error prone task.

In particular the need for common notation for version has emerged based on the
usage of Package URLs referencing vulnerable package version ranges such as in
vulnerability databases like `VulnerableCode
<https://github.com/nexB/vulnerablecode/>`_.

To better understand the problem, here are some of the many notations and
conventions in use:

- ``semver`` https://semver.org/ is a popular specification to structure version
  strings, but does not provide a way to express version ranges.

- RubyGems strongly suggest using ``semver`` for version but does not enforce it.
  As a result some gem use semver while several popular package do not use
  strict semver. RubyGems use their own notation for version ranges which
  looks like the ``node-semver`` notation with some subtle differences.
  See https://guides.rubygems.org/patterns/#semantic-versioning

- ``node-semver`` ranges are used in npm at https://github.com/npm/node-semver#ranges
  with range semantics that are specific to ``semver`` versions and npm.

- Dart pub versioning scheme is similar to ``node-semver`` and the documentation
  at https://dart.dev/tools/pub/versioning provides a comprehensive coverage of
  the topic of versioning. Version resolution uses its own algorithm.

- Python uses its own version and version ranges notation with notable
  peculiarities on how pre-release and post-release suffixes are used
  https://www.python.org/dev/peps/pep-0440/

- Debian and Ubuntu use their own notation and are remarkable for their use of
  ``epochs`` to disambiguate versions.
  https://www.debian.org/doc/debian-policy/ch-relationships.html

- RPM distros use their own range notation and use epochs like Debian.
  https://rpm-software-management.github.io/rpm/manual/dependencies.html

- Perl CPAN defines its own version range notation similar to this specification
  and uses two-segment versions. https://metacpan.org/pod/CPAN::Meta::Spec#Version-Ranges

- Apache Maven and NuGet use similar math intervals notation using brackets
  https://en.wikipedia.org/wiki/Interval_(mathematics)

  - Apache Maven http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html
  - NuGet https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges

- gradle uses Apache Maven notation with some extensions
  https://docs.gradle.org/current/userguide/single_versions.html

- Gentoo and Alpine Linux use comparison operators similar to this specification:
  - Gentoo https://wiki.gentoo.org/wiki/Version_specifier
  - Alpine linux https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/master/src/version.c

- Arch Linux https://wiki.archlinux.org/title/PKGBUILD#Dependencies use its
  own simplified notation for its PKGBUILD depends array and use a modified
  RPM version comparison.

- Go modules https://golang.org/ref/mod#versions use ``semver`` versions with
  specific version resolution algorithms.

- Haskell Package Versioning Policy https://pvp.haskell.org/ provides a notation
  similar to this specification based on a modified semver with extra notations
  such as star and caret.

- The NVD https://nvd.nist.gov/vuln/data-feeds#cpeMatch defines CPE ranges as
  lists of version start and end either including or excluding the start or end
  version. And also provides a concrete enumeration of the available ranges as
  a daily feed.

- The version 5 of the CVE JSON data format at
  https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0.schema#L303
  defines version ranges with a starting version, a versionType, and an upper
  limit for the version range as lessThan or lessThanOrEqual; or an enumeration
  of versions. The versionType is defined as ``"The version numbering system
  used for specifying the range. This defines the exact semantics of the
  comparison (less-than) operation on versions, which is required to understand
  the range itself"``. A "versionType" resembles closely the Package URL package
  "type".

- The OSSF OSV schema https://ossf.github.io/osv-schema/ defines vulnerable
  ranges with version events using "introduced", "fixed" and "limit" fields and
  an optional enumeration of all the versions in these ranges, except for
  semver-based versions. A range may be ecosystem-specific based on a provided
  package "ecosystem" value that resembles closely the Package URL package
  "type".


The way two versions are compared as equal, lesser or greater is a closely
related topic:

- Each package ecosystem may have evolved its own peculiar version string
  conventions, semantics and comparison procedure.

- For instance, ``semver`` is a prominent specification in this domain but this
  is just one of the many ways to structure a version string.

- Debian, RPM, PyPI, RubyGems, and Composer have their own subtly different
  approach on how to determine how two versions are compared as equal, greater
  or lesser.


Solution
---------

A solution to the many version range syntaxes is to design a new simplified
notation to unify them all with:

- a mostly universal and minimalist, compact notation to express version ranges
  from many different package types and ecosystems.

- the package type-specific definitions to normalize existing range expressions
  in this common notation.

- the designation of which algorithm or procedure to use when comparing two
  versions such that it is possible to resolve if a version is within or
  outside of a version range.

We call this solution "version range specifier" or "vers" and it is described
in this document.


Version range specifier
------------------------

A version range specifier (aka. "vers") is a URI string using the ``vers``
URI-scheme with this syntax::

   vers:<versioning-scheme>/<version-constraint>|<version-constraint>|...

For example, to define a set of versions that contains either version ``1.2.3``,
or any versions greater than or equal to ``2.0.0`` but less than ``5.0.0`` using
the ``node-semver`` versioning scheme used with the ``npm`` Package URL type,
the version range specifier will be::

    vers:npm/1.2.3|>=2.0.0|<5.0.0

``vers`` is the URI-scheme and is an acronym for "VErsion Range Specifier". It
has been selected because it is short, obviously about version and available
for a future formal URI-scheme registration at IANA.

The pipe "|" is used as a simple separator between ``<version-constraint>``.
Each ``<version-constraint>`` in this pipe-separated list contains a comparator
and a version::

    <comparator:version>

This list of ``<version-constraint>`` are signposts in the version timeline of
a package that specify version intervals.

A ``<version>`` satisfies a version range specifier if it is contained within
any of the intervals defined by these ``<version-constraint>``.


Using version range specifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``vers`` primary usage is to test if a version is within a range.

An version is within a version range if falls in any of the intervals defined
by a range. Otherwise, the version is outside of the version range.

Some important usages derived from this include:

- **Resolving a version range specifier to a list of concrete versions.**
  In this case, the input is one or more known versions of a package. Each
  version is then tested to check if it lies within or outside the range. For
  example, given a vulnerability and the ``vers`` describing the vulnerable
  versions of a package, this process is used to determine if an existing
  package version is vulnerable.

- **Selecting one of several versions that are within a range.**
  In this case, given several versions that are within a range and several
  packages that express package dependencies qualified by a version range,
  a package management tools will determine and select the set of package
  versions that satisfy all the version ranges constraints of all dependencies.
  This usually requires deploying heuristics and algorithms (possibly complex
  such as sat solvers) that are ecosystem- and tool-specific and outside of the
  scope for this specification; yet ``vers`` could be used in tandem with
  ``purl`` to provide an input to this dependencies resolution process.


Examples
~~~~~~~~~

A single version in an npm package dependency:

- originally seen as a dependency on version "1.2.3" in a package.json manifest
- the version range spec is: ``vers:npm/1.2.3``


A list of versions, enumerated:

- ``vers:pypi/0.0.0|0.0.1|0.0.2|0.0.3|1.0|2.0pre1``


A complex statement about a vulnerability in a "maven" package that affects
multiple branches each with their own fixed versions at 
https://repo1.maven.org/maven2/org/apache/tomee/apache-tomee/ 
Note how the constraints are sorted:


- "affects Apache TomEE 8.0.0-M1 - 8.0.1, Apache TomEE 7.1.0 - 7.1.2,
  Apache TomEE 7.0.0-M1 - 7.0.7, Apache TomEE 1.0.0-beta1 - 1.7.5."

- a normalized version range spec is:
  ``vers:maven/>=1.0.0-beta1|<=1.7.5|>=7.0.0-M1|<=7.0.7|>=7.1.0|<=7.1.2|>=8.0.0-M1|<=8.0.1``

- alternatively, four ``vers`` express the same range, using one ``vers`` for
  each vulnerable "branches": 
  - ``vers:tomee/>=1.0.0-beta1|<=1.7.5``
  - ``vers:tomee/>=7.0.0-M1|<=7.0.7``
  - ``vers:tomee/>=7.1.0|<=7.1.2``
  - ``vers:tomee/>=8.0.0-M1|<=8.0.1``

Conversing RubyGems custom syntax for dependency on gem. Note how the
pessimistic version constraint is expanded:

- ``'library', '~> 2.2.0', '!= 2.2.1'``
- the version range spec is: ``vers:gem/>=2.2.0|!= 2.2.1|<2.3.0``


URI scheme
~~~~~~~~~~

The ``vers`` URI scheme is  an acronym for "VErsion Range Specifier".
It has been selected because it is short, obviously about version and available
for a future formal registration for this URI-scheme at the IANA registry.

The URI scheme is followed by a colon ":".


``<versioning-scheme>``
~~~~~~~~~~~~~~~~~~~~~~~

The ``<versioning-scheme>`` (such as ``npm``, ``deb``, etc.) determines:

- the specific notation and conventions used for a version string encoded in
  this scheme. Versioning schemes often specify a version segments separator and
  the meaning of each version segments, such as [major.minor.patch] in semver.

- how two versions are compared as greater or lesser to determine if a version
  is within or outside a range.

- how a versioning scheme-specific range notation can be transformed in the
  ``vers`` simplified notation defined here.

By convention the versioning scheme **should** be the same as the ``Package URL``
package type for a given package ecosystem. It is OK to have other schemes
beyond the purl type. A scheme could be specific to a single package name.

The ``<versioning-scheme>`` is followed by a slash "/".


``<version-constraint>``
~~~~~~~~~~~~~~~~~~~~~~~~

After the ``<versioning-scheme>`` and "/" there are one or more
``<version-constraint>`` separated by a pipe "|". The pipe "|" has no special
meaning beside being a separator.

Each  ``<version-constraint>`` of this list is either a single ``<version>`` as
in ``1.2.3`` for example or the combination of a ``<comparator>`` and a ``<version>`` as in
``>=2.0.0`` using this syntax::

    <comparator><version>

A single version that means that a version equal to this version satisfies the
range spec. Equality is based on the equality of two normalized version strings
according to their versioning scheme. For most schemes, this is a simple string
equality. But schemes can specify normalization and rules for equality such as
``pypi`` with PEP440. 


The special star "*" comparator matches any version. It must be used **alone**
exclusive of any other constraint and must not be followed by a version. For
example "vers:deb/\*" represent all the versions of a Debian package. This
includes past, current and possible future versions.


Otherwise, the ``<comparator>`` is one of these comparison operators:

- "!=": Version exclusion or inequality comparator. This means a version must
  not be equal to the provided version that must be excluded from the range.
  For example: "!=1.2.3" means that version "1.2.3" is excluded.

- "<", "<=": Lesser than or lesser-or-equal version comparators point to all
  versions less than or equal to the provided version.
  For example "<=1.2.3" means less than or equal to "1.2.3".

- ">", ">=": Greater than or greater-or-equal version comparators point to
  all versions greater than or equal to the provided version.
  For example ">=1.2.3" means greater than or equal to "1.2.3".


The ``<versioning-scheme>`` defines:

- how to compare two version strings using these comparators, and

- the structure of a version string such as "1.2.3" if any. For instance, the
  ``semver`` specification for version numbers  defines a version as composed
  primarily of three dot-separated numeric segments named major, minor and patch.



Normalized, canonical representation and validation
-----------------------------------------------------

The construction and validation rules are designed such that a ``vers`` is
easier to read and understand by human and straight forward to process by tools,
attempting to avoid the creation of empty or impossible version ranges.

- Spaces are not significant and removed in a canonical form. For example
  "<1.2.3|>=2.0" and " <  1.2. 3 | > = 2  . 0" are equivalent.

- A version range specifier contains only printable ASCII letters, digits and
  punctuation.

- The URI scheme and versioning scheme are always lowercase as in ``vers:npm``. 

- The versions are case-sensitive, and a versioning scheme may specify its own
  case sensitivity.

- If a ``version`` in a ``<version-constraint>`` contains separator or
  comparator characters (i.e. ``><=!*|``), it must be quoted using the URL
  quoting rules. This should be rare in practice.

The list of ``<version-constraint>s`` of a range are signposts in the version
timeline of a package. With these few and simple validation rules, we can avoid
the creation of most empty or impossible version ranges:

- **Constraints are sorted by version**. The canonical ordering is the versions
  order. The ordering of ``<version-constraint>`` is not significant otherwise
  but this sort order is needed when check if a version is contained in a range.

- **Versions are unique**. Each ``version`` must be unique in a range and can
  occur only once in any ``<version-constraint>`` of a range specifier,
  irrespective of its comparators. Tools must report an error for duplicated
  versions.

- **There is only one star**: "*" must only occur once and alone in a range,
  without any other constraint or version.

Starting from a de-duplicated and sorted list of constraints, these extra rules
apply to the comparators of any two contiguous constraints to be valid:

- "!=" constraint can be followed by a constraint using any comparator, i.e.,
  any of "=", "!=", ">", ">=", "<", "<=" as comparator (or no constraint).

Ignoring all constraints with "!=" comparators:

- A "=" constraint must be followed only by a constraint with one of "=", ">",
  ">=" as comparator (or no constraint).

And ignoring all constraints with "=" or "!=" comparators, the sequence of
constraint comparators must be an alternation of greater and lesser comparators:

- "<" and "<=" must be followed by one of ">", ">=" (or no constraint).
- ">" and ">=" must be followed by one of "<", "<=" (or no constraint).

Tools must report an error for such invalid ranges.


Parsing and validating version range specifiers
-------------------------------------------------

To parse a version range specifier string:

- Remove all spaces and tabs.
- Start from left, and split once on colon ":".
- The left hand side is the URI-scheme that must be lowercase.
  - Tools must validate that the URI-scheme value is ``vers``.
- The right hand side is the specifier.

- Split the specifier from left once on a slash "/".

- The left hand side is the <versioning-scheme> that must be lowercase.
  Tools should validate that the <versioning-scheme> is a known scheme.

- The right hand side is a list of one or more constraints.
  Tools must validate that this constraints string is not empty ignoring spaces.

- If the constraints string is equal to "*", the ``<version-constraint>`` is "*".
  Parsing is done and no further processing is needed for this ``vers``. A tool
  should report an error if there are extra characters beyond "*". 

- Strip leading and trailing pipes "|" from the constraints string.
- Split the constraints on pipe "|". The result is a list of ``<version-constraint>``.
  Consecutive pipes must be treated as one and leading and trailing pipes ignored.

- For each ``<version-constraint>``:
  - Determine if the ``<version-constraint>`` starts with one of the two comparators:

    - If it starts with ">=", then the comparator is ">=".
    - If it starts with "<=", then the comparator is "<=".
    - If it starts with "!=", then the comparator is "!=".
    - If it starts with "<",  then the comparator is "<".
    - If it starts with ">",  then the comparator is ">".

    - Remove the comparator from ``<version-constraint>`` string start. The
      remaining string is the version.

  - Otherwise the version is the full ``<version-constraint>`` string (which implies
    an equality comparator of "=")

  - Tools should validate and report an error if the version is empty.

  - If the version contains a percent "%" character, apply URL quoting rules
    to unquote this string.

  - Append the parsed (comparator, version) to the constraints list.

Finally:

- The results are the ``<versioning-scheme>`` and the list of ``<comparator, version>``
  constraints.

Tools should optionally validate and simplify the list of ``<comparator, version>``
constraints once parsing is complete:

- Sort and validate the list of constraints.
- Simplify the list of constraints.


Version constraints simplification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tools can simplify a list of ``<version-constraint>`` using this approach:

These pairs of contiguous constraints with these comparators are valid:

- != followed by anything
- =, <, or <= followed by =, !=, >, or >=
- >, or >= followed by !=, <, or <=

These pairs of contiguous constraints with these comparators are redundant and
invalid (ignoring any != since they can show up anywhere):

- =, < or <= followed by < or <=: this is the same as < or <=
- > or >= followed by =, > or >=: this is the same as > or >=


A procedure to remove redundant constraints can be:

- Start from a list of constraints of comparator and version, sorted by version
  and where each version occurs only once in any constraint.

- If the constraints list contains a single constraint (star, equal or anything)
  return this list and simplification is finished.

- Split the constraints list in two sub lists:

  - a list of "unequal constraints" where the comparator is "!="
  - a remainder list of "constraints" where the comparator is not "!="

- If the remainder list of "constraints" is empty, return the "unequal constraints"
  list and simplification is finished.

- Iterate over the constraints list, considering the current and next contiguous
  constraints, and the previous constraint (e.g., before current) if it exists:

    - If current comparator is ">" or ">=" and next comparator is "=", ">" or ">=",
      discard next constraint

    - If current comparator is "=", "<" or "<="  and next comparator is <" or <=",
      discard current constraint. Previous constraint becomes current if it exists.

    - If there is a previous constraint:

        - If previous comparator is ">" or ">=" and current comparator is "=", ">" or ">=",
          discard current constraint

        - If previous comparator is "=", "<" or "<=" and current comparator is <" or <=",
          discard previous constraint

- Concatenate the "unequal constraints" list and the filtered "constraints" list
- Sort by version and return.


Checking if a version is contained within a range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check if a "tested version" is contained within a version range:

- Start from a parsed a version range specifier with:

  - a versioning scheme
  - a list of constraints of comparator and version, sorted by version
    and where each version occurs only once in any constraint.

- If the constraint list contains only one item and the comparator is "*",
  then the "tested version" is IN the range. Check is finished.

- Select the version equality and comparison procedures suitable for this
  versioning scheme and use these for all version comparisons performed below.

- If the "tested version" is equal to the any of the constraint version
  where the constraint comparator is for equality (any of "=", "<=", or ">=")
  then the "tested version" is in the range. Check is finished.

- If the "tested version" is equal to the any of the constraint version where
  the constraint comparator is "=!" then the "tested version" is NOT in the
  range. Check is finished.

- Split the constraint list in two sub lists:

  - a first list where the comparator is "=" or "!="
  - a second list where the comparator is neither "=" nor "!="

- Iterate over the current and next contiguous constraints pairs (aka. pairwise)
  in the second list.

- For each current and next constraint:

    - If this is the first iteration and current comparator is "<" or <="
      and the "tested version" is less than the current version
      then the "tested version" is IN the range. Check is finished.

    - If this is the last iteration and next comparator is ">" or >="
      and the "tested version" is greater than the next version
      then the "tested version" is IN the range. Check is finished.

    - If current comparator is ">" or >=" and next comparator is "<" or <="
      and the "tested version" is greater than the current version
      and the "tested version" is less than the next version
      then the "tested version" is IN the range. Check is finished.

    - If current comparator is "<" or <=" and next comparator is ">" or >="
      then these versions are out the range. Continue to the next iteration.

- Reaching here without having finished the check before means that the
  "tested version" is NOT in the range.


Notes and caveats
~~~~~~~~~~~~~~~~~~~

- Comparing versions from two different versioning schemes is an error. Even
  though there may be some similarities between the ``semver`` version of an npm
  and the ``deb`` version of its Debian packaging, the way versions are compared
  specific to each versioning scheme and may be different. Tools should report
  an error in this case.

- All references to sorting or ordering of version constraints means sorting
  by version. And sorting by versions always implies using the versioning
  scheme-specified version comparison and ordering.


Some of the known versioning schemes
----------------------------------------

These are a few known versioning schemes for some common Package URL
`types` (aka. ``ecosystem``).

- **deb**: Debian and Ubuntu https://www.debian.org/doc/debian-policy/ch-relationships.html
  Debian uses these comparators: <<, <=, =, >= and >>.

- **rpm**: RPM distros https://rpm-software-management.github.io/rpm/manual/dependencies.html
  The a simplified rmpvercmp version comparison routine is used by Arch Linux Pacman.

- **gem**: RubyGems https://guides.rubygems.org/patterns/#semantic-versioning
  which is similar to ``node-semver`` for its syntax, but does not use semver
  versions.

- **npm**: npm uses node-semver which is based on semver with its own range
  notation https://github.com/npm/node-semver#ranges
  A similar but different scheme is used by Rust
  https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html
  and several other package types may use ``node-semver``-like ranges. But most
  of these related schemes are not strictly the same as what is implemented in
  ``node-semver``. For instance PHP ``composer`` may need its own scheme as this
  is not strictly ``node-semver``.

- **pypi**: Python https://www.python.org/dev/peps/pep-0440/

- **cpan**: Perl https://perlmaven.com/how-to-compare-version-numbers-in-perl-and-for-cpan-modules

- **golang**: Go modules https://golang.org/ref/mod#versions use ``semver`` versions
  with a specific minimum version resolution algorithm.

- **maven**: Apache Maven supports a math interval notation which is rarely seen
  in practice http://maven.apache.org/enforcer/enforcer-rules/versionRanges.html

- **nuget**: NuGet https://docs.microsoft.com/en-us/nuget/concepts/package-versioning#version-ranges
  Note that Apache Maven and NuGet are following a similar approach with a
  math-derived intervals syntax as in https://en.wikipedia.org/wiki/Interval_(mathematics)

- **gentoo**: Gentoo https://wiki.gentoo.org/wiki/Version_specifier

- **alpine**: Alpine linux https://gitlab.alpinelinux.org/alpine/apk-tools/-/blob/master/src/version.c
  which is using Gentoo-like conventions.

- **generic**: a generic version comparison algorithm (which will be specified
  later, likely based on a split on any wholly alpha or wholly numeric segments
  and dealing with digit and string comparisons, like is done in libversion)


TODO: add Rust, composer and archlinux, nginx, tomcat, apache.

A separate document will provide details for each versioning scheme and:

- how to convert its native range notation to the ``vers`` notation and back.
- how to compare and sort two versions in a range.

This versioning schemes document will also explain how to convert CVE and OSV
ranges to ``vers``.


Implementations
-----------------------

- Python: https://github.com/nexB/univers
- Java: https://github.com/nscuro/versatile
- Yours!



Related efforts and alternative
------------------------------------

- CUDF defines a generic range notation similar to Debian and integer version
  numbers from the sequence of versions for universal dependencies resolution
  https://www.mancoosi.org/cudf/primer/

- OSV is an "Open source vulnerability DB and triage service." It defines
  vulnerable version range semantics using a minimal set of comparators for use
  with package "ecosystem" and version range "type".
  https://github.com/google/osv

- libversion is a library for general purpose version comparison using a
  unified procedure designed to work with many package types.
  https://github.com/repology/libversion

- unified-range is a library for uniform version ranges based on the Maven
  version range spec. It support Apache Maven and npm ranges
  https://github.com/snyk/unified-range

- dephell specifier is a library to parse and evaluate version ranges and
  "work with version specifiers (can parse PEP-440, SemVer, Ruby, NPM, Maven)"
  https://github.com/dephell/dephell_specifier


Why not reuse existing version range notations?
-----------------------------------------------------

Most existing version range notations are tied to a specific version string
syntax and are therefore not readily applicable to other contexts. For example,
the use of elements such as tilde and caret ranges in RubyGems, npm or Dart
notations implies that a certain structure exists in the version string (semver
or semver- like). The inclusion of these additional comparators is a result of
the history and evolution in a given package ecosystem to address specific needs.

In practice, the unified and reduced set of comparators and syntax defined for
``vers`` has been designed such that all these notations can be converted to a
``vers`` and back from a ``vers`` to the original notation.

In contrast, this would not be possible with existing notations. For instance,
the Python notation may not work with npm semver versions and reciprocally.

There are likely to be a few rare cases where round tripping from and to
``vers`` may not be possible, and in any case round tripping to and from ``vers``
should produce equivalent results and even if not strictly the same original
strings.

Another issue with existing version range notations is that they are primarily
designed for dependencies and not for vulnerable ranges. In particular, a
vulnerability may exist for multiple "version branches" of a given package such
as with Django 2.x and 3.x. Several version range notations have difficulties to
communicate these as typically all the version constraints must be satisfied.
In contrast,  a vulnerability can affect multiple disjoint version ranges of a
package and any version satisfying these constraints would be vulnerable: it
may not be possible to express this with a notation designed exclusively for
dependent versions resolution.

Finally, one of the goals of this spec is to be a compact yet obvious Package
URL companion for version ranges. Several existing and closely related notations
designed for vulnerable ranges are verbose specifications designed for use
in API with larger JSON documents.


Why not use the OSV Ranges?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See:

- https://ossf.github.io/osv-schema/

``vers`` and the OSSF OSV schema vulnerable ranges are equivalent and ``vers``
provides a compact range notation while OSV provides more verbose JSON notation.

``vers`` borrows the design from and was informed by the OSV schema spec and its
authors.

OSV uses a minimalist set of only three comparators:

- "=" to enumerate versions,
- ">=" for the version that introduced a vulnerability, and
- "<"  for the version that fixed a vulnerability.

OSV Ranges support neither ">" nor "!=" comparators making it difficult to
express some ranges that must exclude a version. This may not be an issue for
most vulnerable ranges yet:

- this makes it difficult or impossible to precisely express certain dependency
  and vulnerable ranges when a version must be excluded and the set of existing
  versions is not yet known,

- this make some ranges more verbose such as with the CVE v5 API ranges
  notation that can include their upper limit and would need two constraints.

Another high level difference between the two specifications are the
codes used to qualify a range package  "ecosystem" value that resembles closely
the Package URL package "type" used in ``vers``. This spec will provide a strict
mapping between the OSV ecosystem and the ``vers`` versioning schemes values.


Why not use the CVE v5 API Ranges?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See:

- https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0_schema.json#L303
- https://github.com/CVEProject/cve-schema/blob/master/schema/v5.0/CVE_JSON_5.0_schema.json#L123

The version 5 of the CVE JSON data format defines version ranges with a
starting version, a versionType, and an upper limit for the version range as
lessThan or lessThanOrEqual or as an enumeration of versions. The versionType
and the package collectionURL possible values are only indicative and left out
of this specification and both seem strictly equivalent to the Package URL
"type" on the one hand and the ``vers`` versioning scheme on the other hand.

The semantics and expressiveness of each range are similar and ``vers`` provides
a compact notation rather than a more verbose JSON notation. ``vers`` supports
strictly the conversion of any CVE v5 range to its notation and further
provides a concrete list of well known versioning schemes. ``vers`` design was
informed by the CVE v5 API schema spec and its authors.

When CVE v5 becomes active, this spec will provide a strict mapping between the
CVE ``versionType`` and the ``vers`` versioning schemes values. Furthermore, this
spec and the Package URL "types" should be updated accordingly to provide
a mapping with the upcoming CVE ``collectionURL`` that will be effectively used.

There is one issue with CVE v5: it introduces a new trailing "*" notation that
does not exists in most version ranges notations and may not be computable
easily in many cases. The description of the "lessThan" property is:

    The non-inclusive upper limit of the range. This is the least version NOT
    in the range. The usual version syntax is expanded to allow a pattern to end
    in an asterisk `(*)`, indicating an arbitrarily large number in the version
    ordering. For example, `{version: 1.0 lessThan: 1.*}` would describe the
    entire 1.X branch for most range kinds, and `{version: 2.0, lessThan: *}`
    describes all versions starting at 2.0, including 3.0, 5.1, and so on.

The conversion to ``vers`` range should be:

- with a version 1.0 and `"lessThan": "*"`, the ``vers`` equivalent is: ``>=1.0``.

- with a version 1.0 and `"lessThan": "2.*"`, the ``vers`` equivalent can be
  computed for ``semver`` versions as ``>=1.0|<2`` but is not accurate unless
  as versioning schemes have different rules. For instance, pre-release may be
  treated in some case as part of the v1. branch and in some other cases as part
  of the v2. branch. It is not clear if with "2.*"  the CVE v5 spec means:

    - ``<2``
    - or something that excludes any version string that starts with ``2.``

And in this case, with the expression `"lessThan": "2.*"` using  a ``semver``
version, it is not clear if ``2.0.0-alpha`` is "lessThan"; semver sorts it
before ``2.0`` and after ``1.0``, e.g., in ``semver`` ``2.0.0-alpha`` is
"less than" ``2``.


Why not use the NVD CPE Ranges?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See:

- https://nvd.nist.gov/vuln/vulnerability-detail-pages#divRange
- https://nvd.nist.gov/developers/vulnerabilities#divResponse
- https://csrc.nist.gov/schema/nvd/feed/1.1/nvd_cve_feed_json_1.1.schema

The version ranges notation defined in the JSON schema of the CVE API payload
uses these four fields: ``versionStartIncluding``, ``versionStartExcluding``,
``versionEndIncluding`` and ``versionEndExcluding``. For example::

    "versionStartIncluding": "7.3.0",
    "versionEndExcluding": "7.3.31",
    "versionStartExcluding" : "9.0.0",
    "versionEndIncluding" : "9.0.46",

In addition to these ranges, the NVD publishes a list of concrete CPE with
versions resolved for a range with daily updates at
https://nvd.nist.gov/vuln/data-feeds#cpeMatch 

Note that the NVD CVE configuration is a complex specification that goes well
beyond version ranges and is used to match comprehensive configurations across
multiple products and version ranges. ``vers`` focus is exclusively versions.

In contrast with ``vers`` compact notation, the NVD JSON notation is more
verbose, yet ``vers`` supports strictly the conversion of any CPE range.


Why not use node-semver ranges?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See:

- https://github.com/npm/node-semver#ranges

The node-semver spec is similar but much more complex than this spec. This is
an AND of ORs constraints with a few practical issues:

- A space means "AND", therefore white spaces are significant. Having
  significant white spaces in a string makes normalization more complicated and
  may be a source of confusion if you remove the spaces from the string. 
  ``vers`` avoids the ambiguity of spaces by ignoring them.

- The advanced range syntax has grown to be rather complex using hyphen ranges,
  stars ranges, carets and tilde constructs that are all tied to the JavaScript
  and npm ways of handling versions in their ecosystem and are bound furthermore
  to the semver semantics and its npm implementation. These are not readily
  reusable elsewhere. The multiple comparators and modifiers make the notation
  grammar more complex to parse and process for a machine and harder to read for
  human.

Notations that are directly derived from node-semver as used in Rust and PHP
Composer have the same issues.


Why not use Python PEP-0440 ranges?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See:

- https://www.python.org/dev/peps/pep-0440/#version-specifiers

The Python pep-0440 "Version Identification and Dependency Specification"
provides a comprehensive specification for Python package versioning and a
notation for "version specifiers" to express the version constraints of
dependencies.

This specification is similar to this ``vers`` spec, with more operators and
aspects specific to the versions used only in the Python ecosystem.

- In particular pep-0440 uses tilde, triple equal and wildcard star operators
  that are specific to how two Python versions are compared.

- The comma separator between constraints is a logical "AND" rather than an
  "OR". The "OR" does not exist in the syntax making some version ranges
  harder to express, in particular for vulnerabilities that may affect several
  exact versions or ranges for multiple parallel release branches. Ranges such as
  "Django 1.2 or later, or Django 2.2 or later or Django 3.2 or later" are
  difficult to express without an "OR" logic.


Why not use RubyGems requirements notation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See:

- https://guides.rubygems.org/patterns/#declaring-dependencies

The RubyGems specification suggests but does not enforce using semver. It uses
operators similar to the ``node-semver`` spec with the different of the "~>"
aka. pessimistic operator vs. a plain "~" tilde used in node-semver.  This
operator implies some semver-like versioning, yet gem version are not strictly
semver. This makes the notation complex to implement and impractical to reuse
in places that do not use the same Ruby-specific semver-like semantics.


Why not use fewer comparators with only =, >= and <?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For instance, the OSV schema adopts a reduced set of only three comparators:

- "=" is implied when used to enumerate vulnerable versions
- ">=" (greater or equal) is for the version that introduces a vulnerability
- "<" (lesser) is for the version that fixes a vulnerability

This approach is simpler and works well for most vulnerable ranges but it faces
limitations when converting from other notations:

- ">" cannot be converted reliably to ">=" unless you know all the versions and
  these will never change.

- "<=" cannot be converted reliably to "<" unless you know all the versions and
  these will never change.

- "!=" cannot be converted reliably: there is no ">" comparator to create an
  unequal equivalent of "><"; and a combo of ">=" and "<" is not equivalent
  to inequality unless you know all the versions and these will never change.


Why not use richer comparators such as tilde, caret and star?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some existing notations such as used with npm, gem, python, or composer
provide syntactic shorthand such as:

- a "pessimistic operator" using tilde, ~> or =~  as in "~1.3" or "~>1.2.3" 
- a caret ^ prefix as in "^ 1.2"
- using a star in a version segment as in "1.2.*"
- dash-separated ranges as in "1.2 - 1.4"
- arbitrary string equality such as "===1.2"

Most of these notations can be converted without loss to the ``vers`` notation.
Furthermore these notations typically assume a well defined version string
structure specific to their package ecosystem and are not reusable in another
ecosystem that would not use the exact same version conventions.

For instance, the tilde and caret notations demand that you can reliably
infer the next version (aka. "bump") from a given version; this is possible
only if the versioning scheme supports this operation reliably for all its
accepted versions.


Why not use mathematical interval notation for ranges?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apache Maven and NuGet use a mathematical interval notation with comma-separated
"[", "]", "(" and ")"  to declare version ranges.

All other known range notations use the more common ">", "<", and "=" as
comparators. ``vers`` adopts this familiar approach.


References
---------------------


Here are some of the discussions that led to the creation of this specification:

- https://github.com/package-url/purl-spec/issues/66
- https://github.com/package-url/purl-spec/issues/84
- https://github.com/package-url/purl-spec/pull/93
- https://github.com/nexB/vulnerablecode/issues/119
- https://github.com/nexB/vulnerablecode/issues/140
- https://github.com/nexB/univers/pull/11

License
---------------------

This document is licensed under the MIT license
