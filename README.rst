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
  
- Sonatype Lifecycle uses a format id followed by format specific coordinates. https://help.sonatype.com/display/NXIQ/Component+Details+API+-+v2  

Solution
========

A `purl` or package URL is an attempt to standardize existing approaches to
reliably identify and locate software packages.

A `purl` is a URL string used to identify and locate a software package in a
mostly universal and uniform way across programing languages, package managers,
packaging conventions, tools, APIs and databases.

Such a package URL is useful to reliably reference the same software package
using a simple and expressive syntax and conventions based on familiar URLs.


purl
~~~~~

`purl` stands for **package URL**.

A `purl` is a URL composed of six components::

    type:namespace/name@version?qualifiers#subpath

Components are separated by a specific character for unambiguous parsing.

The defintion for each components is:

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


Components are designed such that they for a hierarchy from the most significant
on the left left to the least significant components to the right.


A `purl` must NOT contain a URL Authority i.e. there is no support for
`username`, `password`, `host` and `port` components. A `namespace` segment may
sometimes look like a `host` but its interpretation is specific to a `type`.


Some `purl` examples
~~~~~~~~~~~~~~~~~~~~

::

    bitbucket:birkenfeld/pygments-main@244fd47e07d1014f0aed9c

    deb:debian/curl@7.50.3-1?arch=i386&distro=jessie

    docker:cassandra@sha256:244fd47e07d1004f0aed9c
    docker:gcr.io/customer/dockerimage@sha256:244fd47e07d1004f0aed9c

    gem:jruby-launcher@1.1.2?platform=java
    gem:ruby-advisory-db-check@0.12.4

    github:package-url/purl-spec@244fd47e07d1004f0aed9c

    golang:google.golang.org/genproto#googleapis/api/annotations

    maven:org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources
    maven:org.apache.xmlgraphics/batik-anim@1.9.1?repository_url=repo.spring.io/release

    npm:%40angular/animation@12.3.1
    npm:foobar@12.3.1

    nuget:EnterpriseLibrary.Common@6.0.1304

    pypi:django@1.11.1

    rpm:fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
    rpm:opensuse/curl@7.56.1-1.1.?arch=i386&distro=opensuse-tumbleweed

(NB: some checksums are truncated for brevity)


A `purl` is a URL
~~~~~~~~~~~~~~~~~

- A `purl` is a valid URL and URI that conforms to the URL definitions or
  specifications at:

  - https://tools.ietf.org/html/rfc3986
  - https://en.wikipedia.org/wiki/URL#Syntax
  - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
  - https://url.spec.whatwg.org/

- The `purl` components are mapped to these URL components:

  - `purl` `type`: this is a URL `scheme`
  - `purl` `namespace`, `name` and `version` components: these are
    collectively mapped to a URL `path`
  - `purl` `qualifiers`: this maps to a URL `query`
  - `purl` `subpath`: this is a URL `fragment`
  - In a `purl` there is no support for a URL Authority (e.g. NO
    `username`, `password`, `host` and `port` components).

- Special URL schemes as defined in https://url.spec.whatwg.org/ such as
  `file://`, `https://`, `http://` and `ftp://` are NOT valid `purl` types. They
  may be used to reference URLs in separate attributes outside of a `purl` or in
  a `purl` qualifier.

- Version control system (VCS) URLs such `git://`, `svn://`, `hg://` or as
  defined in Python pip or SPDX download locations are NOT valid `purl` types.
  They are a closely related, compact and uniform way to reference vcs URLs.
  They may be used as references in separate attributes outside of a `purl` or
  in a `purl` qualifier.


Rules for each `purl` component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A `purl` string is an ASCII URL string composed of six components.

Some components are allowed to use other characters beyond ASCII: these
components must then be UTF-8-encoded strings and percent-encoded as defined in
the "Character encoding" section.

The rules for each component are:

- **type**:

  - The package `type` is composed only of ASCII letters and numbers, '.', '+'
    and '-' (period, plus, and dash)
  - The `type` cannot start with a number
  - The `type` cannot contains spaces
  - The `type` must NOT be percent-encoded
  - The `type` is case insensitive. The canonical form is lowercase
  - Since a `purl` never contains a URL Authority, its `type` must not be
    suffixed with double slash as in 'docker://' and should use instead
    'docker:'. Otherwise this would be an invalid URI per rfc3986 at
    https://tools.ietf.org/html/rfc3986#section-3.3::

        If a URI does not contain an authority component, then the path
        cannot begin with two slash characters ("//").

    While it is acceptable to use such '://' suffix, its is not significant and
    not needed for unambiguous parsing even if it makes a `purl` look like a
    familiar web URL. In its canonical form, a `purl` must NOT use such '://'
    `type` suffix. 
  - `purl` parsers must accept URLs with such '://' and must ignore the '//'.
  - `purl` builders must not create invalid URLs with such double slash '//'.
  - The `type` is followed by a ':' separator
  - For example these two purls are strictly equivalent and the first is in
    canonical form. The second `purl` with a '//' is an acceptable `purl` but is
    an invalid URI/URL per rfc3986::

            gem:ruby-advisory-db-check@0.12.4
            gem://ruby-advisory-db-check@0.12.4


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

  - A `version` is a plain and opaque string. Some package `type` use versioning
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
    - A `value` must be must be a percent-encoded string
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
  separators. The may need to be encoded elsewhere

- the ':' `type` separator does not need to and must NOT be encoded. It is
  unambiguous unencoded everywhere

- the '/' used as `namespace`/`name` and `subpath` segments separator does not
  need to and must NOT be percent-encoded. It is unambiguous unencoded
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

- Start a `purl` string with the `type` as a lowercase ASCII string

  - Append ':' to the `purl`

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

  - The left side lowercased is the `type`
  - The right side is the `remainder`

- Strip the `remainder` from leading and trailing '/'

  - Split this once from right on '/'
  - The left side is the `remainder`
  - Percent-decode the right side
  - UTF-8-decode the `name` if needed in your programming language
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


Known `purl` types
~~~~~~~~~~~~~~~~~~~~

These are known `purl` package type definitions. More should be added. See
candidate list further down.


- `bitbucket` for Bitbucket-based packages:

  - The default repository is `bitbucket.org`
  - The `namespace` is the user or organization. It is not case sensitive and
    must be lowercased.
  - The `name` is the repository name. It is not case sensitive and must be
    lowercased.
  - The `version` is a commit or tag
  - Examples::

        bitbucket:birkenfeld/pygments-main@244fd47e07d1014f0aed9c


- `composer` for Composer PHP packages:

  - The default repository is `packagist.org`
  - The `namespace` is the vendor.
  - Note: private, local packages may have no name. In this casse you cannot
    create a `purl` for these.
  - Examples::

        composer:laravel/laravel@5.5.0


- `deb` for Debian, Debian derivatives and Ubuntu packages:

  - There is no default package repository: this should be implied either from
    the `distro` `qualifiers` `key` or using a base url as a `repository_url`
    `qualifiers` `key`
  - The `namespace` is the "vendor" name such as "debian" or "ubuntu".
    It is not case sensitive and must be lowercased.
  - The `name` is not case sensitive and must be lowercased.
  - The `version` is is the package version.
  - `arch` is the `qualifiers` `key` for a package architecture
  - Examples::

        deb:debian/curl@7.50.3-1?arch=i386&distro=jessie
        deb:debian/dpkg@1.19.0.4?arch=amd64&distro=stretch
        deb:ubuntu/dpkg@1.19.0.4?arch=amd64

- `docker` for Docker images

  - The default repository is `hub.docker.com`
  - The `namespace` is the registry/user/organization if present
  - The version should be the image id sha256 or a tag. Since tags can be moved,
    a sha256 image id is preferred.
  - Examples::

        docker:cassandra@latest
        docker:smartentry/debian@dc437cc87d10
        docker:gcr.io/customer/dockerimage@sha256:244fd47e07d10


- `gem` for Rubygems:

  - The default repository is `rubygems.org`
  - The `platform` `qualifiers` `key` is used to specify an alternative platform
    such as `java` for JRuby. The implied default is `ruby` for Ruby MRI.
  - Examples::

        gem:ruby-advisory-db-check@0.12.4
        gem:jruby-launcher@1.1.2?platform=java


- `generic` for plain, generic packages that do not fit anywhere else such as
  for "upstream -from-distro" packages. In particular this is handy for a plain
  version control repository such as a bare git repo.

  - Their is no default repository. A `download_url` and `checksum` may be
    provided in `qualifiers` or as separate attributes outside of a `purl` for
    proper identification and location.
  - When possible another or a new purl `type` should be used instead of using
    the `generic` type and eventually contributed back to this specification
  - as for other `type`, the `name` component is mandatory. In the worst case
    it can be a file or directory name.
  - Examples (truncated for brevity)::

       generic:openssl@1.1.10g
       generic:openssl@1.1.10g?download_url=https://openssl.org/source/openssl-1.1.0g.tar.gz&checksum=sha256:de4d501267da3931090
       generic:bitwarderl?vcs_url=https://git.fsfe.org/dxtr/bitwarderl@cc55108da32042a0e385bd8e


- `github` for Github-based packages:

  - The default repository is `github.com`
  - The `namespace` is the user or organization. It is not case sensitive and
    must be lowercased.
  - The `name` is the repository name. It is not case sensitive and must be
    lowercased.
  - The `version` is a commit or tag
  - Examples::

        github:package-url/purl-spec@244fd47e07d1004f0aed9c
        github:package-url/purl-spec@244fd47e07d1004f0aed9c#everybody/loves/dogs


- `golang` for Go packages

  - There is no default package repository: this is implied in the namespace
    using the `go get` command conventions
  - The `namespace` and `name` must be lowercased.
  - The `subpath` is used to point to a subpath inside a package
  - The `version` is often empty when a commit is not specified and should be
    the commit in most cases when available.
  - Examples::

        golang:github.com/gorilla/context@234fd47e07d1004f0aed9c
        golang:google.golang.org/genproto#googleapis/api/annotations
        golang:github.com/gorilla/context@234fd47e07d1004f0aed9c#api


- `maven` for Maven JARs and related artifacts

  - The default repository is `repo1.maven.org`
  - The group id is the `namespace` and the artifact id is the `name`
  - Known `qualifiers` keys are: `classifier` and `type` as defined in the
    POM documentation. Note that Maven uses a concept / coordinate called packaging
    which does not map directly 1:1 to a file extension. In this use case, we need
    to construct a link to one of many possible artifacts. Maven itself uses type 
    in a dependency declaration when needed to disambiguate between them.
  - Examples::

        maven:org.apache.xmlgraphics/batik-anim@1.9.1
        maven:org.apache.xmlgraphics/batik-anim@1.9.1?type=pom
        maven:org.apache.xmlgraphics/batik-anim@1.9.1?classifier=sources
        maven:org.apache.xmlgraphics/batik-anim@1.9.1?type=zip&classifier=dist
        maven:net.sf.jacob-projec/jacob@1.14.3?classifier=x86&type=dll
        maven:net.sf.jacob-projec/jacob@1.14.3?classifier=x64&type=dll


- `npm` for Node NPM packages:

  - The default repository is `registry.npmjs.org`
  - The `namespace` is used for the scope of a scoped NPM package.
  - Per the package.json spec, new package "must not have uppercase letters in
    the name", therefore the must be lowercased.
  - Examples::

        npm:foobar@12.3.1
        npm:%40angular/animation@12.3.1
        npm:mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git@4345abcd34343


- `nuget` for NuGet .NET packages:

  - The default repository is `nuget.org`
  - There is no `namespace` per se even if the common convention is to use
    dot-separated package names where the first segment is `namespace`-like.
    TBD: should we split the first segment as a namespace?
  - Examples::

        nuget:EnterpriseLibrary.Common@6.0.1304


- `pypi` for Python packages:

  - The default repository is `pypi.python.org`
  - PyPi treats '-' and '_' as the same character and is not case sensitive.
    Therefore a Pypi package `name` must be lowercased and underscore '_'
    replaced with a dash '-'
  - TBD: we could specify a `format` `qualifiers` `key` to specify a package
    format with values of `egg`, `wheel` , `sdist`, `exe` or may be a file
    extension?
  - TBD: we could specify a  `markers` `qualifiers` `key` to specify PEP 508
    environment markers but this is extra complexity. See
    https://www.python.org/dev/peps/pep-0508/
  - Examples::

        pypi:django@1.11.1
        pypi:django-allauth@12.23


- `rpm` for RPMs:

  - There is no default package repository: this should be implied either from
    the `distro` `qualifiers` `key` or using a repository base url as a
    `repository_url` `qualifiers` `key`
  - the `namespace` is the vendor such as fedora or opensuse
    It is not case sensitive and must be lowercased.
  - the `name` is the RPM name and is case sensitive.
  - the `version` is the combined epoch (if not 0), version and release of an
    RPM.
  - `arch` is the `qualifiers` `key` for a package architecture
  - Examples::

        rpm:fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
        rpm:opensuse/curl@7.56.1-1.1.?arch=i386&distro=opensuse-tumbleweed


Other candidate types to define:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `alpine` for Alpine Linux apk packages:
- `apache` for Apache projects packages:
- `android` for Android apk packages:
- `arch` for Arch Linux packages:
- `atom` for Atom packages:
- `bower` for Bower JavaScript packages:
- `brew` for Homebrew packages:
- `buildroot` for Buildroot packages
- `cargo` for Rust packages:
- `carthage` for Cocoapods Cocoa packages:
- `chef` for Chef packages:
- `clojars` for Clojure packages:
- `cocoapods` for Cocoapods iOS packages:
- `conan` for Conan C/C++ packages:
- `coreos` for CoreOS packages:
- `cpan` for CPAN Perl packages:
- `cran` for CRAN R packages:
- `ctan` for CTAN TeX packages:
- `crystal` for Crystal Shards packages:
- `drupal` for Drupal packages:
- `dtype` for DefinitelyTyped TypeScript type definitions:
- `dub` for D packages:
- `elm` for Elm packages:
- `eclipse` for Eclipse projects packages:
- `gitea` for Gitea-based packages:
- `gitlab` for Gitlab-based packages:
- `guix` for Guix packages:
- `hackage` for Haskell packages:
- `haxe` for Haxe packages:
- `hex` for Erlang and Elixir packages
- `julia` for Julia packages:
- `lua` for LuaRocks packages:
- `melpa` for Emacs packages
- `meteor` for Meteor JavaScript packages:
- `nim` for Nim packages:
- `nix` for Nixos packages:
- `opam` for OCaml packages:
- `openwrt` for OpenWRT packages:
- `osgi` for OSGi bundle packages:
- `p2` for Eclipse p2 packages:
- `pear` for Pear PHP packages:
- `pecl` for PECL PHP packages:
- `perl6` for Perl 6 module packages:
- `platformio` for PlatformIO packages:
- `ebuild` for Gentoo Linux portage packages:
- `pub` for Dart packages:
- `puppet` for Puppet Forge packages:
- `sourceforge` for Sourceforge-based packages:
- `sublime` for Sublime packages:
- `swift` for Swift packages:
- `vim` for Vim scripts packages:
- `wordpress` for Wordpress packages:
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
  Python pip or the SPDX specification. See https://github.com/spdx/spdx-
  spec/blob/cfa1b9d08903/chapters/3-package-information.md#37-package-download-
  location- TODO: incorporate the details from SPDX here.

- `file_name` is an extra file name of a package archive.

- `checksum` is a qualifier for one or more checksums stored as a
  comma-separated list. Each item in the `value` is in form of
  `lowercase_algorithm:hex_encoded_lowercase_value` such as
  `sha1:ad9503c3e994a4f611a4892f2e67ac82df727086`.
  For example (with checksums truncated for brevity) ::

       `checksum=sha1:ad9503c3e994a4f,sha256:41bf9088b3a1e6c1ef1d`


Known implementations
~~~~~~~~~~~~~~~~~~~~~

This list is TBD!

- in JavaScript:
- in Golang: https://github.com/package-url/packageurl-go
- for .NET:
- for the JVM:
- in Perl:
- in Python: https://github.com/package-url/packageurl-python
- in Ruby:


Users and adopters
~~~~~~~~~~~~~~~~~~

This list is TBD!

 - https://github.com/nexB/scancode-toolkit will report `purl` from parsed
   package manifests using https://github.com/package-url/packageurl-python
   The code lives in the 275 branch for now.


Tests
~~~~~

TBD!

To support the language-neutral testing of `purl` implementations, a test suite
is provided as JSON document. This document contains an array of objects. Each
object represents a test with these key/value pairs some of which may not be
normalized:

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

This document is dedicated to the public domain
