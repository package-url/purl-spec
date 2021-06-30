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

deb
---
``deb`` for Debian, Debian derivatives, and Ubuntu packages:

- There is no default package repository: this should be implied either from
  the ``distro`` qualifiers key or using a base url as a ``repository_url``
  qualifiers key
- The ``namespace`` is the "vendor" name such as "debian" or "ubuntu".
  It is not case sensitive and must be lowercased.
- The ``name`` is not case sensitive and must be lowercased.
- The ``version`` is the package version.
- ``arch`` is the qualifiers key for a package architecture
- Examples::

      pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
      pkg:deb/debian/dpkg@1.19.0.4?arch=amd64&distro=stretch
      pkg:deb/ubuntu/dpkg@1.19.0.4?arch=amd64

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
     pkg:generic/bitwarderl?vcs_url=https://git.fsfe.org/dxtr/bitwarderl@cc55108da32


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
      pkg:npm/mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git@4345abcd34343

nuget
-----
``nuget`` for NuGet .NET packages:

- The default repository is ``https://www.nuget.org``
- There is no ``namespace`` per se even if the common convention is to use
  dot-separated package names where the first segment is ``namespace``-like.
  TBD: should we split the first segment as a namespace?
- Examples::

      pkg:nuget/EnterpriseLibrary.Common@6.0.1304

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
- the ``namespace`` is the vendor such as fedora or opensus
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
----
``swift`` for Swift packages:

- There is currently no default repository for Swift packages.
- The ``namespace`` is used for the scope of a Swift package.
  It is not case sensitive and must be lowercased.

  - A package scope consists of alphanumeric characters and hyphens.
    Hyphens may not occur at the beginning or end,
    nor consecutively within a scope.
  - The maximum length of a package scope is 39 characters.
  - A valid package scope matches the following regular expression pattern
    ``\A[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}\z``

- The ``name`` is the name declared in the Swift package manifest.
  It is case and normalization insensitive,
  and must be normalized using Unicode Normalization Form KC (NFKC)
  and then transformed with locale-independent case folding.

  - The maximum length of a package name is 128 characters.
  - A valid package name matches the following regular expression pattern
    ``\A\p{XID_Start}\p{XID_Continue}{0,127}\z``

- The ``version`` is the version of the package release,
  and must be a valid SemVer version number.
- Examples::

      pkg:swift/alamofire/Alamofire@5.4.3
      pkg:swift/flight-school/Money@1.3.0
      pkg:swift/realm/SwiftLint@0.43.1

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
- ``conan`` for Conan C/C++ packages:
- ``coreos`` for CoreOS packages:
- ``cpan`` for CPAN Perl packages:
- ``cran`` for CRAN R packages:
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
- ``hackage`` for Haskell packages:
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
- ``pub`` for Dart packages:
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
