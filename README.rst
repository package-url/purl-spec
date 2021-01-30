Context
=======

We build and release software by massively consuming and producing software
packages such as NPMs, RPMs, Rubygems, etc.

Each package manager, platform, type or ecosystem has its own conventions and
protocols to identify, locate and provision software packages.


Problem
=======

When tools, APIs and databases process or store multiple package types, it is
difficult to reference the same software package across tools in a uniform way.

For example, these tools, specifications and API use relatively similar
approaches to identify and locate software packages, each with subtle
differences in syntax, naming and conventions:

- Grafeas uses a scheme, namespace, name and version in a URL-like string.
  https://github.com/Grafeas/Grafeas

- Here.com OSRK uses a package manager, name and version field and a colon-
  separated URL-like string
  https://github.com/heremaps/oss-review-toolkit

- JFrog XRay uses a scheme, namespace, name and version in a URL-like string
  https://www.jfrog.com/confluence/display/XRAY/Xray+REST+API#XrayRESTAPI-ComponentIdentifiers

- Libraries.io uses a platform, name and version
  https://libraries.io/

- OpenShift fabric8 analytics uses ecosystem, name and version
  https://github.com/fabric8-analytics/

- ScanCode and AboutCode.org use a type, name and version
  https://github.com/nexB/scancode-toolkit

- SPDX has an appendix for external repository references and uses a type and a
  locator with a type-specific syntax for component separators in a URL-like
  string
  https://github.com/spdx/spdx-spec/blob/master/chapters/3-package-information.md

- versioneye uses a type, name and version
  https://github.com/versioneye/

- Sonatype Lifecycle uses a format id followed by format specific coordinates. 
  https://help.sonatype.com/display/NXIQ/Component+Details+API+-+v2  


Solution
========

A `purl` or package URL is an attempt to standardize existing approaches to
reliably identify and locate software packages.

A `purl` is a URL string used to identify and locate a software package in a
mostly universal and uniform way across programing languages, package managers,
packaging conventions, tools, APIs and databases.

Such a package URL is useful to reliably reference the same software package
using a simple and expressive syntax and conventions based on familiar URLs.


Check also this short `purl` presentation (with video) at FOSDEM 2018
https://fosdem.org/2018/schedule/event/purl/ for an overview.


purl
~~~~~

`purl` stands for **package URL**.

A `purl` is a URL composed of seven components::

    scheme:type/namespace/name@version?qualifiers#subpath

Components are separated by a specific character for unambiguous parsing.

The defintion for each components is:

- **scheme**: this is the URL scheme with the constant value of "pkg". One of
  the primary reason for this single scheme is to facilitate the future official
  registration of the "pkg" scheme for package URLs. Required.
- **group**: defines the way which types are allowed and how they should be processed. Required.
- **type**: the package "type" or package "protocol" such as git, svn, dotnet/nuget,
  ruby/gem, py/pypi, etc. Required.
- **namespace**: some name prefix such as a Maven groupid, a Docker image owner,
  a GitHub user or organization. Optional and type-specific.
- **name**: the name of the package. Required.
- **version**: the version of the package. Optional.
- **qualifiers**: extra qualifying data for a package such as an OS,
  architecture, a distro, etc. Optional and type-specific.
- **subpath**: extra subpath within a package, relative to the package root.
  Optional.


Components are designed such that they for a hierarchy from the most significant
on the left to the least significant components on the right.


A `purl` must NOT contain a URL Authority i.e. there is no support for
`username`, `password`, `host` and `port` components. A `namespace` segment may
sometimes look like a `host` but its interpretation is specific to a `type`.


Some `purl` examples
~~~~~~~~~~~~~~~~~~~~

::

    pkg:vcs/git/https://bitbucket.com/birkenfeld/pygments-main@244fd47e07d1014f0aed9c

    pkg:distr/deb/debian/curl@7.50.3-1?arch=i386&distro=jessie

    pkg:ctr/docker/cassandra@sha256:244fd47e07d1004f0aed9c
    pkg:ctr/docker/customer/dockerimage@sha256:244fd47e07d1004f0aed9c?repository_url=gcr.io

    pkg:pl/gem/jruby-launcher@1.1.2?platform=java
    pkg:pl/gem/ruby-advisory-db-check@0.12.4

    pkg:vcs/git/https://github.com/package-url/purl-spec@244fd47e07d1004f0aed9c

    pkg:pl/go/google.golang.org/genproto#googleapis/api/annotations

    pkg:pl/mvn/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources
    pkg:pl/mvn/org.apache.xmlgraphics/batik-anim@1.9.1?repository_url=repo.spring.io/release

    pkg:pl/npm/%40angular/animation@12.3.1
    pkg:pl/npm/foobar@12.3.1

    pkg:pl/nuget/EnterpriseLibrary.Common@6.0.1304

    pkg:pl/pypi/django@1.11.1

    pkg:distr/rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
    pkg:distr/rpm/opensuse/curl@7.56.1-1.1.?arch=i386&distro=opensuse-tumbleweed

(NB: some checksums are truncated for brevity)


A `purl` is a URL
~~~~~~~~~~~~~~~~~

- A `purl` is a valid URL and URI that conforms to the URL definitions or
  specifications at:

  - https://tools.ietf.org/html/rfc3986
  - https://en.wikipedia.org/wiki/URL#Syntax
  - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
  - https://url.spec.whatwg.org/

- This is a valid URL because it is a locator even though it has no Authority
  URL component: each `type` has a default repository location when defined.

- The `purl` components are mapped to these URL components:

  - `purl` `scheme`: this is a URL `scheme` with a constant value: `pkg`
  - `purl` `type`, `namespace`, `name` and `version` components: these are
    collectively mapped to a URL `path`
  - `purl` `qualifiers`: this maps to a URL `query`
  - `purl` `subpath`: this is a URL `fragment`
  - In a `purl` there is no support for a URL Authority (e.g. NO
    `username`, `password`, `host` and `port` components).

- Special URL schemes as defined in https://url.spec.whatwg.org/ such as
  `file://`, `https://`, `http://` and `ftp://` are NOT valid `purl` types.
  They are valid URL or URI schemes but they are not `purl`.
  They may be used to reference URLs in separate attributes outside of a `purl`
  or in a `purl` qualifier.

- Version control system (VCS) URLs such `git://`, `svn://`, `hg://` or as
  defined in Python pip or SPDX download locations are NOT valid `purl` types.
  They are valid URL or URI schemes but they are not `purl`.
  They are a closely related, compact and uniform way to reference vcs URLs.
  They may be used as references in separate attributes outside of a `purl` or
  in a `purl` qualifier.


Rules for each `purl` component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A `purl` string is an ASCII URL string composed of seven components.

Some components are allowed to use other characters beyond ASCII: these
components must then be UTF-8-encoded strings and percent-encoded as defined in
the "Character encoding" section.

The rules for each component are:

- **scheme**:

  - The `scheme` is a constant with the value "pkg"
  - Since a `purl` never contains a URL Authority, its `scheme` must not be
    suffixed with double slash as in 'pkg://' and should use instead
    'pkg:'. Otherwise this would be an invalid URI per rfc3986 at
    https://tools.ietf.org/html/rfc3986#section-3.3::

        If a URI does not contain an authority component, then the path
        cannot begin with two slash characters ("//").

    It is therefore incorrect to use such '://' scheme suffix as the URL would
    no longer be valid otherwise. In its canonical form, a `purl` must
    NOT use such '://' `scheme` suffix but only ':' as a `scheme` suffix. 
  - `purl` parsers must accept URLs such as 'pkg://' and must ignore the '//'.
  - `purl` builders must not create invalid URLs with such double slash '//'.
  - The `scheme` is followed by a ':' separator
  - For example these two purls are strictly equivalent and the first is in
    canonical form. The second `purl` with a '//' is an acceptable `purl` but is
    an invalid URI/URL per rfc3986::

            pkg:pl/ruby/gem/ruby-advisory-db-check@0.12.4
            pkg://pl/ruby/gem/ruby-advisory-db-check@0.12.4


- **group**
  - The package `group` is composed only of ASCII letters and numbers, '.', '+'
    and '-' (period, plus, and dash)
  - The `group` cannot start with a number
  - The `group` cannot contains spaces
  - The `group` must NOT be percent-encoded
  - The `group` is case insensitive. The canonical form is lowercase

- **type**:
  - One or more components, each one is has the same requirements as to `group`. Unless stated otherwise, consists of 1 component.

- **namespace**:

  - The optional `namespace` contains zero or more segments, separated by slash
    '/'
  - Leading and trailing slashes '/' are not significant and should be stripped
    in the canonical form. They are not part of the `namespace`
  - Each `namespace` segment must be a percent-encoded string
  - When percent-decoded, a segment:

    - must not contain a '/'
    - must not be empty

  - A URL host or Authority must NOT be used as a `namespace`. Use instead a
    `repository_url` qualifier. Note however that for some types, the
    `namespace` may look like a host.


- **name**:

  - The `name` is prefixed by a '/' separator when the `namespace` is not empty
  - This '/' is not part of the `name`
  - A `name` must be a percent-encoded string


- **version**:

  - The `version` is prefixed by a '@' separator when not empty
  - This '@' is not part of the `version`
  - A `version` must be a percent-encoded string

  - A `version` is a plain and opaque string. Some package `types` use versioning
    conventions such as semver for NPMs or nevra conventions for RPMS. A `type`
    may define a procedure to compare and sort versions, but there is no
    reliable and uniform way to do such comparison consistently.


- **qualifiers**:

  - The `qualifiers` string is prefixed by a '?' separator when not empty
  - This '?' is not part of the `qualifiers`
  - This is a query string composed of zero or more `key=value` pairs each
    separated by a '&' ampersand. A `key` and `value` are separated by the equal
    '=' character
  - These '&' are not part of the `key=value` pairs.
  - `key` must be unique within the keys of the `qualifiers` string
  - `value` cannot be an empty string: a `key=value` pair with an empty `value`
    is the same as no key/value at all for this key
  - For each pair of `key` = `value`:

    - The `key` must be composed only of ASCII letters and numbers, '.', '-' and
      '_' (period, dash and underscore)
    - A `key` cannot start with a number
    - A `key` must NOT be percent-encoded
    - A `key` is case insensitive. The canonical form is lowercase
    - A `key` cannot contains spaces
    - A `value` must be a percent-encoded string
    - The '=' separator is neither part of the `key` nor of the `value`


- **subpath**:

  - The `subpath` string is prefixed by a '#' separator when not empty
  - This '#' is not part of the `subpath`
  - The `subpath` contains zero or more segments, separated by slash '/'
  - Leading and trailing slashes '/' are not significant and should be stripped
    in the canonical form
  - Each `subpath` segment must be a percent-encoded string
  - When percent-decoded, a segment:

    - must not contain a '/'
    - must not be any of '..' or '.'
    - must not be empty

  - The `subpath` must be interpreted as relative to the root of the package


Character encoding
~~~~~~~~~~~~~~~~~~

For clarity and simplicity a `purl` is always an ASCII string. To ensure that
there is no ambiguity when parsing a `purl`, separator characters and non-ASCII
characters must be UTF-encoded and then percent-encoded as defined at::

    https://en.wikipedia.org/wiki/Percent-encoding

Use these rules for percent-encoding and decoding `purl` components:

- the `type` must NOT be encoded and must NOT contain separators

- the '#', '?', '@' and ':' characters must NOT be encoded when used as
  separators. They may need to be encoded elsewhere

- the ':' `scheme` and `type` separator does not need to and must NOT be encoded.
  It is unambiguous unencoded everywhere

- the '/' used as `type`/`namespace`/`name` and `subpath` segments separator
  does not need to and must NOT be percent-encoded. It is unambiguous unencoded
  everywhere

- the '@' `version` separator must be encoded as `%40` elsewhere
- the '?' `qualifiers` separator must be encoded as `%3F` elsewhere
- the '=' `qualifiers` key/value separator must NOT be encoded
- the '#' `subpath` separator must be encoded as `%23` elsewhere

- All non-ASCII characters must be encoded as UTF-8 and then percent-encoded

It is OK to percent-encode `purl` components otherwise except for the `type`.
Parsers and builders must always percent-decode and percent-encode `purl`
components and component segments as explained in the "How to parse" and "How to
build" sections.


How to build `purl` string from its components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building a `purl` ASCII string works from left to right, from `type` to
`subpath`.

Note: some extra type-specific normalizations are required.
See the "Known types section" for details.

To build a `purl` string from its components:


- Start a `purl` string with the "pkg:" `scheme` as a lowercase ASCII string

- Append the `group` string  to the `purl` as a lowercase ASCII string

  - Append '/' to the `purl`

- Append the `type` components as lowercase ASCII strings separated by '/' to the `purl`

- If the `namespace` is not empty:

  - Strip the `namespace` from leading and trailing '/'
  - Split on '/' as segments
  - Apply type-specific normalization to each segment if needed
  - UTF-8-encode each segment if needed in your programming language
  - Percent-encode each segment
  - Join the segments with '/'
  - Append this to the `purl`
  - Append '/' to the `purl`
  - Strip the `name` from leading and trailing '/'
  - Apply type-specific normalization to the `name` if needed
  - UTF-8-encode the `name` if needed in your programming language
  - Append the percent-encoded `name` to the `purl`

- If the `namespace` is empty:

  - Apply type-specific normalization to the `name` if needed
  - UTF-8-encode the `name` if needed in your programming language
  - Append the percent-encoded `name` to the `purl`

- If the `version` is not empty:

  - Append '@' to the `purl`
  - UTF-8-encode the `version` if needed in your programming language
  - Append the percent-encoded version to the `purl`

- If the `qualifiers` are not empty and not composed only of key/value pairs
  where the `value` is empty:

  - Append '?' to the `purl`
  - Build a list from all key/value pair:

    - discard any pair where the `value` is empty.
    - UTF-8-encode each `value` if needed in your programming language
    - If the `key` is `checksums` and this is a list of `checksums` join this
      list with a ',' to create this qualifier `value`
    - create a string by joining the lowercased `key`, the equal '=' sign and
      the percent-encoded `value` to create a qualifier

  - sort this list of qualifier strings lexicographically
  - join this list of qualifier strings with a '&' ampersand
  - Append this string to the `purl`

- If the `subpath` is not empty and not composed only of empty, '.' and '..'
  segments:

  - Append '#' to the `purl`
  - Strip the `subpath` from leading and trailing '/'
  - Split this on '/' as segments
  - Discard empty, '.' and '..' segments
  - Percent-encode each segment
  - UTF-8-encode each segment if needed in your programming language
  - Join the segments with '/'
  - Append this to the `purl`


How to parse a `purl` string in its components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parsing a `purl` ASCII string into its components works from right to left,
from `subpath` to `type`.

Note: some extra type-specific normalizations are required.
See the "Known types section" for details.

To parse a `purl` string in its components:

- Split the `purl` string once from right on '#'

  - The left side is the `remainder`
  - Strip the right side from leading and trailing '/'
  - Split this on '/'
  - Discard any empty string segment from that split
  - Discard any '.' or  '..' segment from that split
  - Percent-decode each segment
  - UTF-8-decode each segment if needed in your programming language
  - Join segments back with a '/'
  - This is the `subpath`

- Split the `remainder` once from right on '?'

  - The left side is the `remainder`
  - The right side is the `qualifiers` string
  - Split the `qualifiers` on '&'. Each part is a `key=value` pair
  - For each pair, split the `key=value` once from left on '=':

    - The `key` is the lowercase left side
    - The `value` is the percent-decoded right side
    - UTF-8-decode the `value` if needed in your programming language
    - Discard any key/value pairs where the value is empty
    - If the `key` is `checksums`, split the `value` on ',' to create
      a list of `checksums`

  - This list of key/value is the `qualifiers` object

- Split the `remainder` once from left on ':'

  - The left side lowercased is the `scheme`
  - The right side is the `remainder`

- Strip the `remainder` from leading and trailing '/'

  - Split this once from left on '/'
  - The left side lowercased is the `group`
  - The right side is the `remainder`

- Determine the minimal count of `type` components for this group.

- Do the following for each `type` component:

  - Strip the `remainder` from leading and trailing '/'

    - Split this once from left on '/'
    - The left side lowercased is the `type[i]`
    - The right side is the `remainder`

- Split the `remainder` once from right on '@'

  - The left side is the `remainder`
  - Percent-decode the right side. This is the `version`.
  - UTF-8-decode the `version` if needed in your programming language
  - This is the `version`

- Split the `remainder` once from right on '/'

  - The left side is the `remainder`
  - Percent-decode the right side. This is the `name`
  - UTF-8-decode this `name` if needed in your programming language
  - Apply type-specific normalization to the `name` if needed
  - This is the `name`

- Split the `remainder` on '/'

  - Discard any empty segment from that split
  - Percent-decode each segment
  - UTF-8-decode the each segment if needed in your programming
    language
  - Apply type-specific normalization to each segment if needed
  - Join segments back with a '/'
  - This is the `namespace`


Known `purl` groups and types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are known `purl` package type definitions. More should be added. See
candidate list further down.

Sources:
^^^^^^^^^

This are special groups. They are special because:

- many packages, especially the ones for interpretable languages, are often distributed in a form of source code that is just packed at client side into an installable package, often no real building is involved;
- many distros have the workflow that first a source code package is created, and then from that source package a binary one is built.

So these groups can be used within other types, including of the groups of `Sources` kind itself, wor which it makes sense. The high-level semantics is usually that other package manager should try to install a package of its own type, building it if needed, ignoring the packages of other types. The exact semantics is clarified for the types, if needed.

- `releases` - for release storage platforms - the websites allowing people to upload an archive and other people to fetch them and get their history of releases. `type` identifies the platform. Followed by the full URI to the repo if it is a standalone installation or only a partial identifier, if it is on the service by the company that had created the system.

  - `gh` - GitHub. Followed by the repo identifier.
  - `gl` - GitLab and Hectapod.
  - `lp` - Launchpad
  - `srht` - SourceHut
  - `bitbucket`
  - `srfg` - SourceForge
  - `FOSSHub`
  - `MirrorBrainz`

- `vcs` - defines source code in a repo of a Version Control System.
  
  - `git` - for Git
  - `hg` - for Mercurial
  - `pjl` - for Pijul
  - `bzr` - for Bazaar
  - `fsl` - for Fossil
  - `svn` - for Subversion
  - `cvs` - for CVS
  - `pfc` - for Perforce
  
  They are very similar to each other
  
    - The `uri` is the repository URI.
    - The `refspec` is any identifier that is used in the VCS to identify a version, i.e. a tag, a commit hash, a branch name, a revision.
    - Examples::

          pkg:vcs/git/https://github.com/pygments/pygments@master
          pkg:vcs/git/https://git.fsfe.org/dxtr/bitwarderl@cc55108da32

- `distr` - defines a package manger used in distros. Has type of 2 components. The first one is the type of package.

  - `src` - source code package. The semantics when used as a virtual type is to fetch source code from there and build it.
  - `bin` - prebuilt package that intended to be installed, not necessarily binary in contents. 
  
  The second one is the type of package manager.

  - `deb` for Debian, Debian derivatives and Ubuntu packages:

    - There is no default package repository: this should be implied either from
      the `distro` `qualifiers` `key` or using a base url as a `repository_url`
      `qualifiers` `key`
    - The `namespace` is the "vendor" name such as "debian" or "ubuntu".
      It is not case sensitive and must be lowercased.
    - The `name` is not case sensitive and must be lowercased.
    - The `version` is the package version.
    - `arch` is the `qualifiers` `key` for a package architecture
    - Examples::

          pkg:distr/bin/deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
          pkg:distr/bin/deb/debian/dpkg@1.19.0.4?arch=amd64&distro=stretch
          pkg:distr/bin/deb/ubuntu/dpkg@1.19.0.4?arch=amd64

  - `rpm` for RPMs:

    - There is no default package repository: this should be implied either from
      the `distro` `qualifiers` `key` or using a repository base url as a
      `repository_url` `qualifiers` `key`
    - the `namespace` is the vendor such as fedora or opensuse
      It is not case sensitive and must be lowercased.
    - the `name` is the RPM name and is case sensitive.
    - the `version` is the combined version and release of an
      RPM
    - `epoch` (optional for RPMs) is a qualifier as it's not required for
      unique identification, but when the epoch exists we strongly
      encourage using it
    - `arch` is the `qualifiers` `key` for a package architecture
    - Examples::

          pkg:distr/bin/rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
          pkg:distr/bin/rpm/centerim@4.22.10-1.el6?arch=i686&epoch=1&distro=fedora-25


- `pl` - defines a package in a package manager for a programming language. Type is of 2 components, the first one identifies the programming language, the second one identifies the standard on repository and its packages.

  - `**/distr/bin`  - a distro package which when installed, automatically installs a package into the systemwide location.
    - The impl of a package manager MUST install it using the package manager supportjng this format directly. For example, installing a package `pkg:lang/py/distr/bin/deb/debian/python3-pip` will de-facto install the same package as `pkg:lang/py/pip/pip`.
    - Implementations of package managers CAN and should refuse to process the package if the package does any other effects considered by the implementation as unneeded for installation of package of this type, i.e. for the example above the implementation can refuse to install any files to the dirs other than `/usr/lib/python*`, `/usr/etc` and `/usr/bin` and verify that any files installed into `/usr/bin` match the template of a python script generated by `setuptools`.

  - `**/distro/src`  - Source code for packages. Should be built and installed if the impl is a package manager.

  - `rust/cargo` a Cargo package for Rust:

    - The default repository is `https://crates.io/`
    - The `name` is the repository name.
    - The `version` is the package version.
    - Examples::

          pkg:pl/rust/cargo/rand@0.7.2
          pkg:pl/rust/cargo/clap@2.33.0
          pkg:pl/rust/cargo/structopt@0.3.11


  - `php/composer` for Composer PHP packages:

    - The default repository is `https://packagist.org`
    - The `namespace` is the vendor.
    - Note: private, local packages may have no name. In this casse you cannot
      create a `purl` for these.
    - Examples::

          pkg:pl/php/composer/laravel/laravel@5.5.0

  - `ruby/gems` for Rubygems:

    - The default repository is `https://rubygems.org`
    - The `platform` `qualifiers` `key` is used to specify an alternative platform
      such as `java` for JRuby. The implied default is `ruby` for Ruby MRI.
    - Examples::

          pkg:pl/ruby/gems/ruby-advisory-db-check@0.12.4
          pkg:pl/ruby/gems/jruby-launcher@1.1.2?platform=java

  - `go/golang` for Go packages

    - There is no default package repository: this is implied in the namespace
      using the `go get` command conventions
    - The `namespace` and `name` must be lowercased.
    - The `subpath` is used to point to a subpath inside a package
    - The `version` is often empty when a commit is not specified and should be
      the commit in most cases when available.
    - Examples::

          pkg:pl/go/vcs/git/google.golang.org/genproto#googleapis/api/annotations
          pkg:pl/go/vcs/git/github.com/gorilla/context@234fd47e07d1004f0aed9c
          pkg:pl/go/vcs/git/github.com/gorilla/context@234fd47e07d1004f0aed9c#api

  - `java/mvn` for Maven JARs and related artifacts

    - The default repository is `https://repo.maven.apache.org/maven2`
    - The group id is the `namespace` and the artifact id is the `name`
    - Known `qualifiers` keys are: `classifier` and `type` as defined in the
      POM documentation. Note that Maven uses a concept / coordinate called packaging
      which does not map directly 1:1 to a file extension. In this use case, we need
      to construct a link to one of many possible artifacts. Maven itself uses type 
      in a dependency declaration when needed to disambiguate between them.
    - Examples::

          pkg:pl/java/mvn/org.apache.xmlgraphics/batik-anim@1.9.1
          pkg:pl/java/mvn/org.apache.xmlgraphics/batik-anim@1.9.1?type=pom
          pkg:pl/java/mvn/org.apache.xmlgraphics/batik-anim@1.9.1?classifier=sources
          pkg:pl/java/mvn/org.apache.xmlgraphics/batik-anim@1.9.1?type=zip&classifier=dist
          pkg:pl/java/mvn/net.sf.jacob-projec/jacob@1.14.3?classifier=x86&type=dll
          pkg:pl/java/mvn/net.sf.jacob-projec/jacob@1.14.3?classifier=x64&type=dll

  - `js/npm` for Node NPM packages:

    - The default repository is `https://registry.npmjs.org`
    - The `namespace` is used for the scope of a scoped NPM package.
    - Per the package.json spec, new package "must not have uppercase letters in
      the name", therefore the must be lowercased.
    - Examples::

          pkg:pl/js/npm/foobar@12.3.1
          pkg:pl/js/npm/%40angular/animation@12.3.1
          pkg:pl/js/npm/mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git@4345abcd34343

  - `dotnet/nuget` for NuGet .NET packages:

    - The default repository is `https://www.nuget.org`
    - There is no `namespace` per se even if the common convention is to use
      dot-separated package names where the first segment is `namespace`-like.
      TBD: should we split the first segment as a namespace?
    - Examples::

          pkg:pl/dotnet/EnterpriseLibrary.Common@6.0.1304

  - `erlg/hex` for Hex packages for Erlang

    - The default repository is `https://repo.hex.pm`.
    - The `namespace` is optional; it may be used to specify the organization for
      private packages on hex.pm. It is not case sensitive and must be lowercased.
    - The `name` is not case sensitive and must be lowercased.
    - Examples::

          pkg:erlg/hex/jason@1.1.2
          pkg:erlg/hex/acme/foo@2.3.4
          pkg:erlg/hex/phoenix_html@2.13.3#priv/static/phoenix_html.js
          pkg:erlg/hex/bar@1.2.3?repository_url=https://myrepo.example.com

  - `py/pypi` for Python packages in PyPI-like registries:

    - The default repository is `https://pypi.python.org`
    - PyPi treats '-' and '_' as the same character and is not case sensitive.
      Therefore a Pypi package `name` must be lowercased and underscore '_'
      replaced with a dash '-'
    - Examples::

          pkg:pl/py/pypi/django@1.11.1
          pkg:pl/py/pypi/django-allauth@12.23


- `ctr` - for self-sufficient container registries and VMs

  - `docker` for Docker images

    - The default repository is `https://hub.docker.com`
    - The `namespace` is the registry/user/organization if present
    - The version should be the image id sha256 or a tag. Since tags can be moved,
      a sha256 image id is preferred.
    - Examples::

          pkg:ctr/docker/cassandra@latest
          pkg:ctr/docker/smartentry/debian@dc437cc87d10
          pkg:ctr/docker/customer/dockerimage@sha256%3A244fd47e07d10?repository_url=gcr.io

Build systems
^^^^^^^^^^^^^^^

Build systems modify the behavior of `Source` URIs.

The type is a build system identifier.

- `build` - for build systems that invoke compilers directly to build binaries. Is followed by URI part of a kind "Source". Meaning: this URI contains a build script for this build system, build scripts for other build systems must be ignored. Used to select a build system in the cases it cannot be automatically detected.

  - `autotools`
  - `meson`
  - `cmake`
  - `make`
  - `premake`
  - `fastbuild`
  - `bazel`
  - `ant`

- `metabuild` - the URI contains a metabuild system recipy. Metabuild systems build and publish packages.

  - `prebuilder`
  - `debhelper`
  - `portage`
  - `aur`
  - `nix` for Nixos packages:
  - `guix` for Guix packages:

Other groups
^^^^^^^^^^^^^^

- `generic` - for plain, generic packages that do not fit anywhere else such as
  for "upstream -from-distro" packages. In particular this is handy for a plain
  version control repository such as a bare git repo.

  - There is no default repository. A `download_url` and `checksum` may be
    provided in `qualifiers` or as separate attributes outside of a `purl` for
    proper identification and location.
  - When possible another or a new purl `type` should be used instead of using
    the `generic` type and eventually contributed back to this specification
  - as for other `type`, the `name` component is mandatory. In the worst case
    it can be a file or directory name.
  - Examples (truncated for brevity)::

       pkg:generic/openssl@1.1.10g
       pkg:generic/openssl@1.1.10g?download_url=https://openssl.org/source/openssl-1.1.0g.tar.gz&checksum=sha256:de4d501267da


Other candidate types to define:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `distro`

  - `alpine` for Alpine Linux apk packages:
  - `android/(gplay|fdroid|amazon|yandex)` for Android apk packages:
  - `arch` for Arch Linux packages:
  - `brew` for Homebrew packages:
  - `chocolatey` for Chocolatey packages
  - `conan` for Conan C/C++ packages:
  - `openwrt` for OpenWRT packages:
  - `appstore` for Apple iOS apps:

- `pl`

  - `cloj/jars` for Clojure packages:
  - `cpan/cpan` for CPAN Perl packages:
  - `raku/vcs/...` for Raku module packages:
  - `cran/cran` for CRAN R packages:
  - `ctan` for CTAN TeX packages:
  - `dub/dub` for D packages:
  - `elm/elm` for Elm packages:
  - `haskel/hackage` for Haskell packages:
  - `haxe/haxe` for Haxe packages:
  - `julia/julia` for Julia packages:
  - `js/bower` for Bower JavaScript packages:
  - `lua/rocks` for LuaRocks packages:
  - `nim/nim` for Nim packages:
  - `php` - for PHP packages:

    - `pear` for Pear
    - `pecl` for PECL

  - `swift/swift` for Swift packages:
  - `ocaml/opam` for OCaml packages:
  - `crystal/shard` for Crystal Shards packages:
  - `dart/pub` for Dart packages:

- `plg`

  - `gradle` for Gradle plugins
  - `atom` for Atom packages:
  - `drupal` for Drupal packages:
  - `sublime` for Sublime packages:
  - `vim` for Vim scripts packages:
  - `melpa` for Emacs packages
  - `wordpress` for Wordpress packages:
  - `notepadpp` for Notepad++ plugins:
  - `kde` for KDE apps plugins installeable via installers:
  - `webext` - for browser extensions following a WebExtensions standard. Is followed by a browser identifier.
  - `userscript` - for lightweight browser extension in form of userscripts. Is followed 
    

- `ctr`

  - `snap`
  - `flatpak`

- To be assigned with groups (or maybe removed at all):

  - `apache` for Apache projects packages:
  - `buildroot` for Buildroot packages
  - `carthage` for Cocoapods Cocoa packages:
  - `chef` for Chef packages:
  - `cocoapods` for Cocoapods iOS packages:
  - `coreos` for CoreOS packages:
  - `dtype` for DefinitelyTyped TypeScript type definitions:
  - `eclipse` for Eclipse projects packages:
  - `helm` for Kubernetes packages
  - `meteor` for Meteor JavaScript packages:
  - `osgi` for OSGi bundle packages:
  - `p2` for Eclipse p2 packages:
  - `platformio` for PlatformIO packages:
  - `ebuild` for Gentoo Linux portage packages:
  - `puppet` for Puppet Forge packages:
  - `terraform` for Terraform modules
  - `vagrant` for Vagrant boxes
  - `yocto` for Yocto recipe packages


Known `qualifiers` key/value pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: Do not abuse `qualifiers`: it can be tempting to use many qualifier
keys but their usage should be limited to the bare minimum for proper package
identification to ensure that a `purl` stays compact and readable in most cases.

Additional, separate external attributes stored outside of a `purl` are the
preferred mechanism to convey extra long and optional information such as a
download URL, vcs URL or checksums in an API, database or web form.


With this warning, the known `key` and `value` defined here are valid for use in
all package types:

- `repository_url` is an extra URL for an alternative, non-default package
  repository or registry.  When a package does not come from the default public
  package repository for its `type` a `purl` may be qualified with this extra
  URL. The default repository or registry of a `type` is documented in the
  "Known `purl` types" section.

- `download_url` is an extra URL for a direct package web download URL to
  optionally qualify a `purl`.

- `vcs_url` is an extra URL for a package version control system URL to
  optionally qualify a `purl`. The syntax for this URL should be as defined in
  Python pip or the SPDX specification. See https://github.com/spdx/spdx-spec/blob/cfa1b9d08903/chapters/3-package-information.md#37-package-download-location

  - TODO: incorporate the details from SPDX here.

- `file_name` is an extra file name of a package archive.

- `checksum` is a qualifier for one or more checksums stored as a
  comma-separated list. Each item in the `value` is in form of
  `lowercase_algorithm:hex_encoded_lowercase_value` such as
  `sha1:ad9503c3e994a4f611a4892f2e67ac82df727086`.
  For example (with checksums truncated for brevity) ::

       `checksum=sha1:ad9503c3e994a4f,sha256:41bf9088b3a1e6c1ef1d`


Known implementations
~~~~~~~~~~~~~~~~~~~~~

- in Golang: https://github.com/package-url/packageurl-go
- for .NET: https://github.com/package-url/packageurl-dotnet
- for the JVM: https://github.com/package-url/packageurl-java, https://github.com/sonatype/package-url-java
- in Python: https://github.com/package-url/packageurl-python
- in Rust: https://github.com/package-url/packageurl-rs
- in JS: https://github.com/package-url/packageurl-js


Users, adopters and links
~~~~~~~~~~~~~~~~~~~~~~~~~

 - https://github.com/nexB/scancode-toolkit will report `purl` from parsed
   package manifests using https://github.com/package-url/packageurl-python
   The code lives in the 275 branch for now.
 - `OWASP Dependency-Track <https://www.owasp.org/index.php/OWASP_Dependency_Track_Project>`_: Software Composition Analysis (SCA) platform
 - `CycloneDX <https://github.com/CycloneDX>`_: A lightweight software bill-of-material (BOM) specification
 - `OSS Index <https://ossindex.sonatype.org>`_: A free catalog of Open Source Components and scanning tools to help developers identify vulnerable components
 - `Sonatype Nexus Lifecycle <https://www.sonatype.com/product-nexus-lifecycle>`_: Enterprise grade Open Source component management


Tests
~~~~~

To support the language-neutral testing of `purl` implementations, a test suite
is provided as JSON document named `test-suite-data.json`. This JSON document
contains an array of objects. Each object represents a test with these key/value
pairs some of which may not be normalized:

- **purl**: a `purl` string. 
- **canonical**: the same `purl` string in canonical, normalized form
- **type**: the `type` corresponding to this `purl`.
- **namespace**: the `namespace` corresponding to this `purl`.
- **name**: the `name` corresponding to this `purl`.
- **version**: the `version` corresponding to this `purl`.
- **qualifiers**: the `qualifiers` corresponding to this `purl` as an object of
  {key: value} qualifier pairs.
- **subpath**: the `subpath` corresponding to this `purl`.
- **is_invalid**: a boolean flag set to true if the test should report an
  error

To test `purl` parsing and building, a tool can use this test suite and for
every listed test object, run these tests:

- parsing the test canonical `purl` then re-building a `purl` from these parsed
  components should return the test canonical `purl`

- parsing the test `purl` should return the components parsed from the test
  canonical `purl`

- parsing the test `purl` then re-building a `purl` from these parsed components
  should return the test canonical `purl`

- building a `purl` from the test components should return the test canonical `purl`


License
~~~~~~~

This document is licensed under the MIT license
