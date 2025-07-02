Package URL specification v1.0.X
================================

The Package URL core specification defines a versioned and formalized format,
syntax, and rules used to represent and validate ``purl``.

A ``purl`` or package URL is an attempt to standardize existing approaches to
reliably identify and locate software packages.

A ``purl`` is a URL string used to identify and locate a software package in a
mostly universal and uniform way across programming languages, package managers,
packaging conventions, tools, APIs and databases.

Such a package URL is useful to reliably reference the same software package
using a simple and expressive syntax and conventions based on familiar URLs.

See `<PURL-TYPES.rst>`_ for known type definitions.

Check also this short ``purl`` presentation (with video) at FOSDEM 2018
https://fosdem.org/2018/schedule/event/purl/ for an overview.


``purl`` stands for **package URL**.

A ``purl`` is a URL composed of seven components::

    scheme:type/namespace/name@version?qualifiers#subpath

Components are separated by a specific character for unambiguous parsing.

The definition for each components is:

- **scheme**: this is the URL scheme with the constant value of "pkg". One of
  the primary reason for this single scheme is to facilitate the future official
  registration of the "pkg" scheme for package URLs. Required.
- **type**: the package "type" or package "protocol" such as maven, npm, nuget,
  gem, pypi, etc. Required.
- **namespace**: some name prefix such as a Maven groupid, a Docker image owner,
  a GitHub user or organization. Optional and type-specific.
- **name**: the name of the package. Required.
- **version**: the version of the package. Optional.
- **qualifiers**: extra qualifying data for a package such as an OS,
  architecture, a distro, etc. Optional and type-specific.
- **subpath**: extra subpath within a package, relative to the package root.
  Optional.


Components are designed such that they form a hierarchy from the most significant
on the left to the least significant components on the right.


A ``purl`` must NOT contain a URL Authority i.e. there is no support for
``username``, ``password``, ``host`` and ``port`` components. A ``namespace`` segment may
sometimes look like a ``host`` but its interpretation is specific to a ``type``.


Some ``purl`` examples
~~~~~~~~~~~~~~~~~~~~~~

::

    pkg:bitbucket/birkenfeld/pygments-main@244fd47e07d1014f0aed9c
    pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
    pkg:gem/ruby-advisory-db-check@0.12.4
    pkg:github/package-url/purl-spec@244fd47e07d1004f0aed9c
    pkg:golang/google.golang.org/genproto#googleapis/api/annotations
    pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources
    pkg:npm/foobar@12.3.1
    pkg:nuget/EnterpriseLibrary.Common@6.0.1304
    pkg:pypi/django@1.11.1
    pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25


A ``purl`` is a URL
~~~~~~~~~~~~~~~~~~~

- A ``purl`` is a valid URL and URI that conforms to the URL definitions or
  specifications at:

  - https://tools.ietf.org/html/rfc3986
  - https://en.wikipedia.org/wiki/URL#Syntax
  - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
  - https://url.spec.whatwg.org/

- This is a valid URL because it is a locator even though it has no Authority
  URL component: each ``type`` has a default repository location when defined.

- The ``purl`` components are mapped to these URL components:

  - ``purl`` ``scheme``: this is a URL ``scheme`` with a constant value: ``pkg``
  - ``purl`` ``type``, ``namespace``, ``name`` and ``version`` components: these are
    collectively mapped to a URL ``path``
  - ``purl`` ``qualifiers``: this maps to a URL ``query``
  - ``purl`` ``subpath``: this is a URL ``fragment``
  - In a ``purl`` there is no support for a URL Authority (e.g. NO
    ``username``, ``password``, ``host`` and ``port`` components).

- Special URL schemes as defined in https://url.spec.whatwg.org/ such as
  ``file://``, ``https://``, ``http://`` and ``ftp://`` are NOT valid ``purl`` types.
  They are valid URL or URI schemes but they are not ``purl``.
  They may be used to reference URLs in separate attributes outside of a ``purl``
  or in a ``purl`` qualifier.

- Version control system (VCS) URLs such ``git://``, ``svn://``, ``hg://`` or as
  defined in Python pip or SPDX download locations are NOT valid ``purl`` types.
  They are valid URL or URI schemes but they are not ``purl``.
  They are a closely related, compact and uniform way to reference VCS URLs.
  They may be used as references in separate attributes outside of a ``purl`` or
  in a ``purl`` qualifier.


Rules for each ``purl`` component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``purl`` string is an ASCII URL string composed of seven components.

Except as expressly stated otherwise in this section, each component:

- MAY be composed of any of the characters defined in the "Permitted
  characters" section
- MUST be encoded as defined in the "Character encoding" section

The rules for each component are:

- **scheme**:

  - The ``scheme`` is a constant with the value "pkg".
  - The ``scheme`` MUST be followed by an unencoded colon ':'.
  - ``purl`` parsers MUST accept URLs where the ``scheme`` and colon ':' are
    followed by one or more slash '/' characters, such as 'pkg://', and MUST
    ignore and remove all such '/' characters.


- **type**:

  - The package ``type`` MUST be composed only of ASCII letters and numbers,
    period '.', and dash '-'.
  - The ``type`` MUST start with an ASCII letter.
  - The ``type`` MUST NOT be percent-encoded.
  - The ``type`` is case insensitive. The canonical form is lowercase.


- **namespace**:

  - The ``namespace`` is optional, unless required by the package's ``type`` definition.
  - If present, the ``namespace`` MAY contain one or more segments, separated
    by a single unencoded slash '/' character.
  - All leading and trailing slashes '/' are not significant and SHOULD be
    stripped in the canonical form. They are not part of the ``namespace``.
  - Each ``namespace`` segment MUST be a percent-encoded string.
  - When percent-decoded, a segment:

    - MUST NOT contain any slash '/' characters
    - MUST NOT be empty
    - MAY contain any Unicode character other than '/' unless the package's
      ``type`` definition provides otherwise.

  - A URL host or Authority MUST NOT be used as a ``namespace``. Use instead a
    ``repository_url`` qualifier. Note however that for some types, the
    ``namespace`` may look like a host.


- **name**:

  - The ``name`` is prefixed by a single slash '/' separator when the
    ``namespace`` is not empty.
  - All leading and trailing slashes '/' are not significant and SHOULD be
    stripped in the canonical form. They are not part of the ``name``.
  - A ``name`` MUST be a percent-encoded string.
  - When percent-decoded, a ``name`` MAY contain any Unicode character unless
    the package's ``type`` definition provides otherwise.


- **version**:

  - The ``version`` is prefixed by a '@' separator when not empty.
  - This '@' is not part of the ``version``.
  - A ``version`` MUST be a percent-encoded string.
  - When percent-decoded, a ``version`` MAY contain any Unicode character unless
    the package's ``type`` definition provides otherwise.
  - A ``version`` is a plain and opaque string.


- **qualifiers**:

  - The ``qualifiers`` component MUST be prefixed by an unencoded question
    mark '?' separator when not empty.  This '?' separator is not part of the
    ``qualifiers`` component.
  - The ``qualifiers`` component is composed of one or more ``key=value``
    pairs.  Multiple ``key=value`` pairs MUST be separated by an
    unencoded ampersand '&'.  This '&' separator is not part of an
    individual ``qualifier``.

  - A ``key`` and ``value`` MUST be separated by the unencoded equal sign '='
    character.  This '=' separator is not part of the ``key`` or ``value``.
  - A ``value`` MUST NOT be an empty string: a ``key=value`` pair with an
    empty ``value`` is the same as if no ``key=value`` pair exists for this
    ``key``.

  - For each ``key=value`` pair:

    - The ``key`` MUST be composed only of lowercase ASCII letters and numbers,
      period '.', dash '-' and underscore '_'.
    - A ``key`` MUST start with an ASCII letter.
    - A ``key`` MUST NOT be percent-encoded.
    - Each ``key`` MUST be unique among all the keys of the ``qualifiers``
      component.
    - A ``value`` MAY contain any Unicode character and all characters MUST be
      encoded as described in the "Character encoding" section.


- **subpath**:

  - The ``subpath`` string is prefixed by a '#' separator when not empty
  - This '#' is not part of the ``subpath``
  - The ``subpath`` contains zero or more segments, separated by slash '/'
  - Leading and trailing slashes '/' are not significant and SHOULD be stripped
    in the canonical form
  - Each ``subpath`` segment MUST be a percent-encoded string
  - When percent-decoded, a segment:

    - MUST NOT contain any slash '/' characters
    - MUST NOT be empty
    - MUST NOT be any of '..' or '.'
    - MAY contain any Unicode character other than '/' unless the package's
      ``type`` definition provides otherwise.

  - The ``subpath`` MUST be interpreted as relative to the root of the package


Permitted characters
~~~~~~~~~~~~~~~~~~~~

A canonical ``purl`` is composed of these permitted ASCII characters:

- the Alphanumeric Characters: ``A to Z``, ``a to z``, ``0 to 9``,
- the Punctuation Characters: ``.-_~`` (period '.',
  dash '-', underscore '_' and tilde '~'),
- the Percent Character: ``%`` (percent sign '%'), and
- the Separator Characters ``:/@?=&#`` (colon ':', slash '/', at sign '@',
  question mark '?', equal sign '=', ampersand '&' and pound sign '#').


``purl`` separators
~~~~~~~~~~~~~~~~~~~

This is how each of the Separator Characters is used:

- ':' (colon) is the separator between ``scheme`` and ``type``
- '/' (slash) is the separator between ``type``, ``namespace`` and ``name``
- '/' (slash) is the separator between ``subpath`` segments
- '@' (at sign) is the separator between ``name`` and  ``version``
- '?' (question mark) is the separator before ``qualifiers``
- '=' (equals) is the separator between a ``key`` and a ``value`` of a
  ``qualifier``
- '&' (ampersand) is the separator between ``qualifiers`` (each being a
  ``key=value`` pair)
- '#' (number sign) is the separator before ``subpath``


Character encoding
~~~~~~~~~~~~~~~~~~

- In the "Rules for each ``purl`` component" section, each component
  defines when and how to apply percent-encoding and decoding to its content.
- When percent-encoding is required by a component definition, the component
  string MUST first be encoded as UTF-8.
- In the component string, each "data octet" MUST be replaced by the
  percent-encoded "character triplet" applying the percent-encoding mechanism
  defined in RFC 3986 section 2.1 (https://datatracker.ietf.org/doc/html/rfc3986#section-2.1),
  including the RFC definition of "data octet" and "character triplet",
  and using these definitions for RFC's "allowed set" and "delimiters":

  - "allowed set" is composed of the Alphanumeric Characters and the
    Punctuation Characters
  - "delimiters" is composed of the Separator Characters

- The following characters MUST NOT be percent-encoded:

  - the Alphanumeric Characters,
  - the Punctuation Characters,
  - the Separator Characters when being used as ``purl`` separators,
  - the colon ':', whether used as a Separator Character or otherwise, and
  - the percent sign '%' when used to represent a percent-encoded character.

- Where the space ' ' is permitted, it MUST be percent-encoded as '%20'.
- With the exception of the percent-encoding mechanism, the rules regarding
  percent-encoding are defined by this specification alone.


How to build ``purl`` string from its components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building a ``purl`` ASCII string works from left to right, from ``type`` to
``subpath``.

Note: some extra type-specific normalizations are required.
See the "Known types section" for details.

To build a ``purl`` string from its components:


- Start a ``purl`` string with the "pkg:" ``scheme`` as a lowercase ASCII string

- Append the ``type`` string to the ``purl`` as an unencoded lowercase ASCII string

  - Append '/' to the ``purl``

- If the ``namespace`` is not empty:

  - Strip the ``namespace`` from leading and trailing '/'
  - Split on '/' as segments
  - Apply type-specific normalization to each segment if needed
  - UTF-8-encode each segment if needed in your programming language
  - Percent-encode each segment
  - Join the segments with '/'
  - Append this to the ``purl``
  - Append '/' to the ``purl``
  - Strip the ``name`` from leading and trailing '/'
  - Apply type-specific normalization to the ``name`` if needed
  - UTF-8-encode the ``name`` if needed in your programming language
  - Append the percent-encoded ``name`` to the ``purl``

- If the ``namespace`` is empty:

  - Apply type-specific normalization to the ``name`` if needed
  - UTF-8-encode the ``name`` if needed in your programming language
  - Append the percent-encoded ``name`` to the ``purl``

- If the ``version`` is not empty:

  - Append '@' to the ``purl``
  - UTF-8-encode the ``version`` if needed in your programming language
  - Append the percent-encoded version to the ``purl``

- If the ``qualifiers`` are not empty and not composed only of key/value pairs
  where the ``value`` is empty:

  - Append '?' to the ``purl``
  - Build a list from all key/value pair:

    - Discard any pair where the ``value`` is empty.
    - UTF-8-encode each ``value`` if needed in your programming language
    - If the ``key`` is ``checksum`` and this is a list of checksums join this
      list with a ',' to create this qualifier ``value``
    - Create a string by joining the lowercased ``key``, the equal '=' sign and
      the percent-encoded ``value`` to create a qualifier

  - Sort this list of qualifier strings lexicographically
  - Join this list of qualifier strings with a '&' ampersand
  - Append this string to the ``purl``

- If the ``subpath`` is not empty and not composed only of empty, '.' and '..'
  segments:

  - Append '#' to the ``purl``
  - Strip the ``subpath`` from leading and trailing '/'
  - Split this on '/' as segments
  - Discard empty, '.' and '..' segments
  - Percent-encode each segment
  - UTF-8-encode each segment if needed in your programming language
  - Join the segments with '/'
  - Append this to the ``purl``


How to parse a ``purl`` string in its components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parsing a ``purl`` ASCII string into its components works from right to left,
from ``subpath`` to ``type``.

Note: some extra type-specific normalizations are required.
See the "Known types section" for details.

To parse a ``purl`` string in its components:

- Split the ``purl`` string once from right on '#'

  - The left side is the ``remainder``
  - Strip the right side from leading and trailing '/'
  - Split this on '/'
  - Discard any empty string segment from that split
  - Percent-decode each segment
  - Discard any '.' or '..' segment from that split
  - UTF-8-decode each segment if needed in your programming language
  - Join segments back with a '/'
  - This is the ``subpath``

- Split the ``remainder`` once from right on '?'

  - The left side is the ``remainder``
  - The right side is the ``qualifiers`` string
  - Split the ``qualifiers`` on '&'. Each part is a ``key=value`` pair
  - For each pair, split the ``key=value`` once from left on '=':

    - The ``key`` is the lowercase left side
    - The ``value`` is the percent-decoded right side
    - UTF-8-decode the ``value`` if needed in your programming language
    - Discard any key/value pairs where the value is empty
    - If the ``key`` is ``checksum``, split the ``value`` on ',' to create
      a list of checksums

  - This list of key/value is the ``qualifiers`` object

- Split the ``remainder`` once from left on ':'

  - The left side lowercased is the ``scheme``
  - The right side is the ``remainder``

- Strip all leading and trailing '/' characters (e.g., '/', '//', '///' and
  so on) from the ``remainder``

  - Split this once from left on '/'
  - The left side lowercased is the ``type``
  - The right side is the ``remainder``

- Split the ``remainder`` once from right on '@'

  - The left side is the ``remainder``
  - Percent-decode the right side. This is the ``version``.
  - UTF-8-decode the ``version`` if needed in your programming language
  - This is the ``version``

- Split the ``remainder`` once from right on '/'

  - The left side is the ``remainder``
  - Strip all leading characters (e.g., '/', '//' and so on)
    from the right side
  - Percent-decode the right side. This is the ``name``
  - UTF-8-decode this ``name`` if needed in your programming language
  - Apply type-specific normalization to the ``name`` if needed
  - This is the ``name``

- Split the ``remainder`` on '/'

  - Strip all leading '/' characters (e.g., '/', '//' and so on)
    from that split
  - Discard any empty segment from that split
  - Percent-decode each segment
  - UTF-8-decode each segment if needed in your programming language
  - Apply type-specific normalization to each segment if needed
  - Join segments back with a '/'
  - This is the ``namespace``


Known ``purl`` types
~~~~~~~~~~~~~~~~~~~~

There are several known ``purl`` package type definitions tracked in the
separate `<PURL-TYPES.rst>`_ document.

Known ``qualifiers`` key/value pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: Do not abuse ``qualifiers``: it can be tempting to use many qualifier
keys but their usage should be limited to the bare minimum for proper package
identification to ensure that a ``purl`` stays compact and readable in most cases.

Additional, separate external attributes stored outside of a ``purl`` are the
preferred mechanism to convey extra long and optional information such as a
download URL, VCS URL or checksums in an API, database or web form.


With this warning, the known ``key`` and ``value`` defined here are valid for use in
all package types:

- ``vers`` allows the specification of a version range.
  The value MUST adhere to the `Version Range Specification <VERSION-RANGE-SPEC.rst>`_.
  This qualifier is mutually exclusive with the ``version`` component.
  For example::

       pkg:pypi/django?vers=vers:pypi%2F%3E%3D1.11.0%7C%21%3D1.11.1%7C%3C2.0.0

- ``repository_url`` is an extra URL for an alternative, non-default package
  repository or registry. When a package does not come from the default public
  package repository for its ``type`` a ``purl`` may be qualified with this extra
  URL. The default repository or registry of a ``type`` is documented in the
  "Known ``purl`` types" section.

- ``download_url`` is an extra URL for a direct package web download URL to
  optionally qualify a ``purl``.

- ``vcs_url`` is an extra URL for a package version control system URL to
  optionally qualify a ``purl``. The syntax for this URL should be as defined in
  Python pip or the SPDX specification. See
  https://github.com/spdx/spdx-spec/blob/cfa1b9d08903/chapters/3-package-information.md#37-package-download-location

  - TODO: incorporate the details from SPDX here.

- ``file_name`` is an extra file name of a package archive.

- ``checksum`` is a qualifier for one or more checksums stored as a
  comma-separated list. Each item in the ``value`` is in form of
  ``lowercase_algorithm:hex_encoded_lowercase_value`` such as
  ``sha1:ad9503c3e994a4f611a4892f2e67ac82df727086``.
  For example (with checksums truncated for brevity) ::

       checksum=sha1:ad9503c3e994a4f,sha256:41bf9088b3a1e6c1ef1d


Tests
~~~~~

To support the language-neutral testing of ``purl`` implementations, a test suite
is provided as JSON document named ``test-suite-data.json``. This JSON document
contains an array of objects. Each object represents a test with these key/value
pairs some of which may not be normalized:

- **purl**: a ``purl`` string.
- **canonical**: the same ``purl`` string in canonical, normalized form
- **type**: the ``type`` corresponding to this ``purl``.
- **namespace**: the ``namespace`` corresponding to this ``purl``.
- **name**: the ``name`` corresponding to this ``purl``.
- **version**: the ``version`` corresponding to this ``purl``.
- **qualifiers**: the ``qualifiers`` corresponding to this ``purl`` as an object of
  {key: value} qualifier pairs.
- **subpath**: the ``subpath`` corresponding to this ``purl``.
- **is_invalid**: a boolean flag set to true if the test should report an
  error

To test ``purl`` parsing and building, a tool can use this test suite and for
every listed test object, run these tests:

- parsing the test canonical ``purl`` then re-building a ``purl`` from these parsed
  components should return the test canonical ``purl``

- parsing the test ``purl`` should return the components parsed from the test
  canonical ``purl``

- parsing the test ``purl`` then re-building a ``purl`` from these parsed components
  should return the test canonical ``purl``

- building a ``purl`` from the test components should return the test canonical ``purl``


License
~~~~~~~

This document is licensed under the MIT license

Definitions
~~~~~~~~~~~

[ASCII]  See, e.g.,

  - American National Standards Institute, "Coded Character Set -- 7-bit
    American Standard Code for Information Interchange", ANSI X3.4, 1986.
  - https://en.wikipedia.org/wiki/ASCII.
