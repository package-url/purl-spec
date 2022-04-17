Package URL Type definitions
============================

Each package manager, platform, type, or ecosystem has its own conventions and
protocols to identify, locate, and provision software packages.

The package **type** is the component of a package URL that is used to capture
this information with a short string such as ``maven``, ``npm``, ``nuget``, ``gem``,
``pypi``, etc.


These are known ``purl`` package type definitions.

Known ``purl`` type definitions are formalized here independent of the core
Package URL specification. See also a candidate list further down.

Definitions can also include types reserved for future use.

See also https://github.com/package-url/purl-spec and
<PURL-SPECIFICATION.rst>`_ for the Package URL specification.


Known ``purl`` types
~~~~~~~~~~~~~~~~~~~~

bitbucket
---------
``bitbucket`` for Bitbucket-based packages:

- The default repository is ``https://bitbucket.org``
- The ``namespace`` is the user or organization. It is not case sensitive and
  must be lowercased.
- The ``name`` is the repository name. It is not case sensitive and must be
  lowercased.
- The ``version`` is a commit or tag
- Examples::

      pkg:bitbucket/birkenfeld/pygments-main@244fd47e07d1014f0aed9c

cocoapods
---------
``cocoapods`` for Cocoapods:

- The default repository is ``https://cdn.cocoapods.org/``
- The ``name`` is the pod name and is case sensitive, cannot contain whitespace, a plus (+) character, or begin with a period (.).
- The ``version`` is the package version.
- The purl subpath is used to represent a pods subspec (if present)
- Examples::

      pkg:cocoapods/AFNetworking@4.0.1
      pkg:cocoapods/MapsIndoors@3.24.0
      pkg:cocoapods/ShareKit@2.0#Twitter
      pkg:cocoapods/GoogleUtilities@7.5.2#NSData+zlib

cargo
-----
``cargo`` for Rust:

- The default repository is ``https://crates.io/``
- The ``name`` is the repository name.
- The ``version`` is the package version.
- Examples::

      pkg:cargo/rand@0.7.2
      pkg:cargo/clap@2.33.0
      pkg:cargo/structopt@0.3.11

composer
--------
``composer`` for Composer PHP packages:

- The default repository is ``https://packagist.org``
- The ``namespace`` is the vendor.
- Note: private, local packages may have no name. In this case you cannot
  create a ``purl`` for these.
- Examples::

      pkg:composer/laravel/laravel@5.5.0

conan
-----
``conan`` for Conan C/C++ packages:

- The default repository is ``https://center.conan.io``
- The ``namespace`` is the user if present
- The ``name`` is the package name.
- The ``version`` is the package version.
- The qualifier ``channel`` must be not empty if namespace is present
- Examples::

      pkg:conan/cctz@2.3
      pkg:conan/bincrafters/cctz@2.3?channel=stable

conda
-----
``conda`` for Conda packages:

- The default repository is ``https://repo.anaconda.com``
- The ``name`` is the package name
- The ``version`` is the package version
- The qualifiers: ``build`` is the build string.
  ``channel`` is the package stored location.
  ``subdir`` is the associated platform.
  ``type`` is the package type.
- Examples::

      pkg:conda/absl-py@0.4.1?build=py36h06a4308_0&channel=main&subdir=linux-64&type=tar.bz2

cran
-----
``cran`` for CRAN R packages:

- The default repository is ``https://cran.r-project.org``
- The ``name`` is the package name and is case sensitive, but there cannot be two packages on CRAN with the same name ignoring case.
- The ``version`` is the package version.
- Examples::

      pkg:cran/A3@1.0.0
      pkg:cran/rJava@1.0-4
      pkg:cran/caret@6.0-88

deb
---
``deb`` for Debian, Debian derivatives, and Ubuntu packages:

- There is no default package repository: this should be implied either from
  the ``distro`` qualifiers key or using a base url as a ``repository_url``
  qualifiers key
- The ``namespace`` is the "vendor" name such as "debian" or "ubuntu".
  It is not case sensitive and must be lowercased.
- The ``name`` is not case sensitive and must be lowercased.
- The ``version`` is the version of the binary (or source) package.
- ``arch`` is the qualifiers key for a package architecture. The special value
  ``arch=source`` identifies a Debian source package that usually consists of a
  Debian Source control file (.dsc) and corresponding upstream and Debian
  sources. The ``dpkg-query`` command can print the ``name`` and ``version`` of
  the corresponding source package of a binary package::

    dpkg-query -f '${source:Package} ${source:Version}' -W <binary package name>

- Examples::

      pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
      pkg:deb/debian/dpkg@1.19.0.4?arch=amd64&distro=stretch
      pkg:deb/ubuntu/dpkg@1.19.0.4?arch=amd64
      pkg:deb/debian/attr@1:2.4.47-2?arch=source
      pkg:deb/debian/attr@1:2.4.47-2%2Bb1?arch=amd64

docker
------
``docker`` for Docker images

- The default repository is ``https://hub.docker.com``
- The ``namespace`` is the registry/user/organization if present
- The version should be the image id sha256 or a tag. Since tags can be moved,
  a sha256 image id is preferred.
- Examples::

      pkg:docker/cassandra@latest
      pkg:docker/smartentry/debian@dc437cc87d10
      pkg:docker/customer/dockerimage@sha256%3A244fd47e07d10?repository_url=gcr.io

gem
---
``gem`` for Rubygems:

- The default repository is ``https://rubygems.org``
- The ``platform`` qualifiers key is used to specify an alternative platform
  such as ``java`` for JRuby. The implied default is ``ruby`` for Ruby MRI.
- Examples::

      pkg:gem/ruby-advisory-db-check@0.12.4
      pkg:gem/jruby-launcher@1.1.2?platform=java

generic
-------
``generic`` for plain, generic packages that do not fit anywhere else such as
for "upstream-from-distro" packages. In particular this is handy for a plain
version control repository such as a bare git repo.

- There is no default repository. A ``download_url`` and ``checksum`` may be
  provided in `qualifiers` or as separate attributes outside of a ``purl`` for
  proper identification and location.
- When possible another or a new purl ``type`` should be used instead of using
  the ``generic`` type and eventually contributed back to this specification
- as for other ``type``, the ``name`` component is mandatory. In the worst case
  it can be a file or directory name.
- Examples (truncated for brevity)::

     pkg:generic/openssl@1.1.10g
     pkg:generic/openssl@1.1.10g?download_url=https://openssl.org/source/openssl-1.1.0g.tar.gz&checksum=sha256:de4d501267da
     pkg:generic/bitwarderl?vcs_url=git%2Bhttps://git.fsfe.org/dxtr/bitwarderl%40cc55108da32


github
------
``github`` for Github-based packages:

- The default repository is ``https://github.com``
- The ``namespace`` is the user or organization. It is not case sensitive and
  must be lowercased.
- The ``name`` is the repository name. It is not case sensitive and must be
  lowercased.
- The ``version`` is a commit or tag
- Examples::

      pkg:github/package-url/purl-spec@244fd47e07d1004
      pkg:github/package-url/purl-spec@244fd47e07d1004#everybody/loves/dogs

golang
------
``golang`` for Go packages

- There is no default package repository: this is implied in the namespace
  using the ``go get`` command conventions
- The ``namespace`` and `name` must be lowercased.
- The ``subpath`` is used to point to a subpath inside a package
- The ``version`` is often empty when a commit is not specified and should be
  the commit in most cases when available.
- Examples::

      pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c
      pkg:golang/google.golang.org/genproto#googleapis/api/annotations
      pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c#api

hackage
-------
``hackage`` for Haskell packages

- The default repository is `https://hackage.haskell.org`.
- The `version` is package version.
- The `name` is case sensitive and use kebab-case
- Examples::

        pkg:hackage/a50@0.5
        pkg:hackage/AC-HalfInteger@1.2.1
        pkg:hackage/3d-graphics-examples@0.0.0.2

hex
---
``hex`` for Hex packages

- The default repository is ``https://repo.hex.pm``.
- The ``namespace`` is optional; it may be used to specify the organization for
  private packages on hex.pm. It is not case sensitive and must be lowercased.
- The ``name`` is not case sensitive and must be lowercased.
- Examples::

      pkg:hex/jason@1.1.2
      pkg:hex/acme/foo@2.3.
      pkg:hex/phoenix_html@2.13.3#priv/static/phoenix_html.js
      pkg:hex/bar@1.2.3?repository_url=https://myrepo.example.com


maven
-----
``maven`` for Maven JARs and related artifacts

- The default repository is ``https://repo.maven.apache.org/maven2``
- The group id is the ``namespace`` and the artifact id is the ``name``
- Known qualifiers keys are: ``classifier`` and ``type`` as defined in the
  POM documentation. Note that Maven uses a concept / coordinate called packaging
  which does not map directly 1:1 to a file extension. In this use case, we need
  to construct a link to one of many possible artifacts. Maven itself uses type
  in a dependency declaration when needed to disambiguate between them.
- Examples::

      pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1
      pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=pom
      pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?classifier=sources
      pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=zip&classifier=dist
      pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x86&type=dll
      pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x64&type=dll


npm
---
``npm`` for Node NPM packages:

- The default repository is ``https://registry.npmjs.org``
- The ``namespace`` is used for the scope of a scoped NPM package.
- Per the package.json spec, new package "must not have uppercase letters in
  the name", therefore the must be lowercased.
- Examples::

      pkg:npm/foobar@12.3.1
      pkg:npm/%40angular/animation@12.3.1
      pkg:npm/mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git%404345abcd34343

nuget
-----
``nuget`` for NuGet .NET packages:

- The default repository is ``https://www.nuget.org``
- There is no ``namespace`` per se even if the common convention is to use
  dot-separated package names where the first segment is ``namespace``-like.
- Examples::

      pkg:nuget/EnterpriseLibrary.Common@6.0.1304

oci
------------
``oci`` for all artifacts stored in registries that conform to the
`OCI Distribution Specification <https://github.com/opencontainers/distribution-spec>`_,
including container images built by Docker and others:

- There is no canonical package repository for OCI artifacts. Therefore
  ``oci`` purls must be registry agnostic by default. To specify the repository,
  provide a ``repository_url`` value.
- OCI purls do not contain a ``namespace``, although, ``repository_url`` may
  contain a namespace as part of the physical location of the package.
- The ``name`` is not case sensitive and must be lowercased. The name is the
  last fragment of the repository name. For example if the repository
  name is ``library/debian`` then the ``name`` is ``debian``.
- The ``version`` is the ``sha256:hex_encoded_lowercase_digest`` of the
  artifact and is required to uniquely identify the artifact.
- Optional qualifiers may include:

  - ``arch``: key for a package architecture, when relevant
  - ``repository_url``: A repository URL where the artifact may be found, but not
    intended as the only location. This value is encouraged to identify a
    location the content may be fetched
  - ``tag``: artifact tag that may have been associated with the digest at the time
- Examples::

      pkg:oci/debian@sha256:<digest>?repository_url=docker.io/library/debian&arch=amd64&tag=latest
      pkg:oci/debian@sha256:<digest>?repository_url=ghcr.io/debian&tag=bullseye
      pkg:oci/static@sha256:<digest>?repository_url=gcr.io/distroless/static&tag=latest
      pkg:oci/hello-wasm@sha256:<digest>?tag=v1

pub
----
``pub`` for Dart and Flutter packages:

- The default repository is ``https://pub.dartlang.org``
- Pub normalizes all package names to be lowercase and using underscores. The only allowed characters are `[a-z0-9_]`. 
- More information on pub naming and versioning is available in the [pubspec documentation](https://dart.dev/tools/pub/pubspec)
- Examples::

      pkg:pub/characters@1.2.0
      pkg:pub/flutter@0.0.0

pypi
----
``pypi`` for Python packages:

- The default repository is ``https://pypi.python.org``
- PyPi treats ``-`` and ``_`` as the same character and is not case sensitive.
  Therefore a Pypi package ``name`` must be lowercased and underscore ``_``
  replaced with a dash ``-``
- Examples::

      pkg:pypi/django@1.11.1
      pkg:pypi/django-allauth@12.23

rpm
---
``rpm`` for RPMs:

- There is no default package repository: this should be implied either from
  the ``distro`` qualifiers key  or using a repository base url as 
  ``repository_url`` qualifiers key
- the ``namespace`` is the vendor such as fedora or opensuse
  It is not case sensitive and must be lowercased.
- the ``name`` is the RPM name and is case sensitive.
- the ``version`` is the combined version and release of an
  RPM
- ``epoch`` (optional for RPMs) is a qualifier as it's not required for
  unique identification, but when the epoch exists we strongly
  encourage using it
- ``arch`` is the qualifiers key for a package architecture
- Examples::

      pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
      pkg:rpm/centerim@4.22.10-1.el6?arch=i686&epoch=1&distro=fedora-25

swift
-----
``swift`` for Swift packages:

- There is no default package repository: this should be implied from ``namespace``
- The ``namespace`` is source host and user/organization.
- The ``name`` is the repository name.
- The ``version`` is the package version.
- Examples::

      pkg:swift/github.com/Alamofire/Alamofire@5.4.3
      pkg:swift/github.com/RxSwiftCommunity/RxFlow@2.12.4

Other candidate types to define:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``alpine`` for Alpine Linux apk packages:
- ``apache`` for Apache projects packages:
- ``android`` for Android apk packages:
- ``arch`` for Arch Linux packages:
- ``atom`` for Atom packages:
- ``bower`` for Bower JavaScript packages:
- ``brew`` for Homebrew packages:
- ``buildroot`` for Buildroot packages
- ``carthage`` for Cocoapods Cocoa packages:
- ``chef`` for Chef packages:
- ``chocolatey`` for Chocolatey packages
- ``clojars`` for Clojure packages:
- ``cocoapods`` for Cocoapods iOS packages:
- ``coreos`` for CoreOS packages:
- ``cpan`` for CPAN Perl packages:
- ``ctan`` for CTAN TeX packages:
- ``crystal`` for Crystal Shards packages:
- ``drupal`` for Drupal packages:
- ``dtype`` for DefinitelyTyped TypeScript type definitions:
- ``dub`` for D packages:
- ``elm`` for Elm packages:
- ``eclipse`` for Eclipse projects packages:
- ``gitea`` for Gitea-based packages:
- ``gitlab`` for Gitlab-based packages:
- ``gradle`` for Gradle plugins
- ``guix`` for Guix packages:
- ``haxe`` for Haxe packages:
- ``helm`` for Kubernetes packages
- ``julia`` for Julia packages:
- ``lua`` for LuaRocks packages:
- ``melpa`` for Emacs packages
- ``meteor`` for Meteor JavaScript packages:
- ``nim`` for Nim packages:
- ``nix`` for Nixos packages:
- ``opam`` for OCaml packages:
- ``openwrt`` for OpenWRT packages:
- ``osgi`` for OSGi bundle packages:
- ``p2`` for Eclipse p2 packages:
- ``pear`` for Pear PHP packages:
- ``pecl`` for PECL PHP packages:
- ``perl6`` for Perl 6 module packages:
- ``platformio`` for PlatformIO packages:
- ``ebuild`` for Gentoo Linux portage packages:
- ``puppet`` for Puppet Forge packages:
- ``sourceforge`` for Sourceforge-based packages:
- ``sublime`` for Sublime packages:
- ``terraform`` for Terraform modules
- ``vagrant`` for Vagrant boxes
- ``vim`` for Vim scripts packages:
- ``wordpress`` for Wordpress packages:
- ``yocto`` for Yocto recipe packages:


License
~~~~~~~

This document is licensed under the MIT license
