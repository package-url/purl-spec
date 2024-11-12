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
`<PURL-SPECIFICATION.rst>`_ for the Package URL specification.


Known ``purl`` types
~~~~~~~~~~~~~~~~~~~~

alpm
----
``alpm`` for Arch Linux and other users of the libalpm/pacman package manager.

- There is no default package repository: this should be implied either from
  the ``distro`` qualifiers key  or using a repository base url as
  ``repository_url`` qualifiers key.
- The ``namespace`` is the vendor such as ``arch``, ``arch32``, ``archarm``,
  ``manjaro`` or ``msys``. It is not case sensitive and must be lowercased.
- The ``name`` is the package name. It is not case sensitive and must be lowercased.
- The ``version`` is the version of the package as specified in [`vercmp(8)`](https://man.archlinux.org/man/vercmp.8#DESCRIPTION) as part of alpm.
- The ``arch`` is the qualifiers key for a package architecture.
- Examples::

      pkg:alpm/arch/pacman@6.0.1-1?arch=x86_64
      pkg:alpm/arch/python-pip@21.0-1?arch=any
      pkg:alpm/arch/containers-common@1:0.47.4-4?arch=x86_64

apk
---
``apk`` for APK-based packages:

- There is no default package repository: this should be implied either from
  the ``distro`` qualifiers key  or using a repository base url as
  ``repository_url`` qualifiers key.
- The ``namespace`` is the vendor such as ``alpine`` or ``openwrt``. It is not
  case sensitive and must be lowercased.
- The ``name`` is the package name. It is not case sensitive and must be
  lowercased.
- The ``version`` is a package version as expected by apk.
- The ``arch`` is the qualifiers key for a package architecture.
- Examples::

      pkg:apk/alpine/curl@7.83.0-r0?arch=x86
      pkg:apk/alpine/apk@2.12.9-r3?arch=x86

bitbucket
---------
``bitbucket`` for Bitbucket-based packages:

- The default repository is ``https://bitbucket.org``.
- The ``namespace`` is the user or organization. It is not case sensitive and
  must be lowercased.
- The ``name`` is the repository name. It is not case sensitive and must be
  lowercased.
- The ``version`` is a commit or tag.
- Examples::

      pkg:bitbucket/birkenfeld/pygments-main@244fd47e07d1014f0aed9c

bitnami
-------
``bitnami`` for Bitnami-based packages:

- The default repository is ``https://downloads.bitnami.com/files/stacksmith``.
- The ``name`` is the component name. It must be lowercased.
- The ``version`` is the full Bitnami package version, including version and revision.
- The ``arch`` is the qualifiers key for a package architecture. Available values: ``amd64`` (default) and ``arm64``.
- The ``distro`` is the qualifiers key for the distribution associated to the package.
- Examples::

      pkg:bitnami/wordpress?distro=debian-12
      pkg:bitnami/wordpress@6.2.0?distro=debian-12
      pkg:bitnami/wordpress@6.2.0?arch=arm64&distro=debian-12
      pkg:bitnami/wordpress@6.2.0?arch=arm64&distro=photon-4

cocoapods
---------
``cocoapods`` for CocoaPods:

- The default repository is ``https://cdn.cocoapods.org/``.
- The ``name`` is the pod name and is case sensitive, cannot contain whitespace, a plus (`+`) character, or begin with a period (`.`).
- The ``version`` is the package version.
- The purl subpath is used to represent a pods subspec (if present).
- Examples::

      pkg:cocoapods/AFNetworking@4.0.1
      pkg:cocoapods/MapsIndoors@3.24.0
      pkg:cocoapods/ShareKit@2.0#Twitter
      pkg:cocoapods/GoogleUtilities@7.5.2#NSData+zlib

cargo
-----
``cargo`` for Rust:

- The default repository is ``https://crates.io/``.
- The ``name`` is the repository name.
- The ``version`` is the package version.
- Examples::

      pkg:cargo/rand@0.7.2
      pkg:cargo/clap@2.33.0
      pkg:cargo/structopt@0.3.11

composer
--------
``composer`` for Composer PHP packages:

- The default repository is ``https://packagist.org``.
- The ``namespace`` is the vendor.
- The ``namespace`` and ``name`` are not case sensitive and must be lowercased.
- Note: private, local packages may have no name. In this case you cannot
  create a ``purl`` for these.
- Examples::

      pkg:composer/laravel/laravel@5.5.0

conan
-----
``conan`` for Conan C/C++ packages. The purl is designed to closely resemble the Conan-native `<package-name>/<package-version>@<user>/<channel>` `syntax for package references <https://docs.conan.io/en/1.46/cheatsheet.html#package-terminology>`_.

- ``name``: The Conan ``<package-name>``.
- ``version``: The Conan ``<package-version>``.
- ``namespace``: The vendor of the package.
- Qualifier ``user``: The Conan ``<user>``. Only required if the Conan package was published with ``<user>``.
- Qualifier ``channel``: The Conan ``<channel>``. Only required if the Conan package was published with Conan ``<channel>``.
- Qualifier ``rrev``: The Conan recipe revision (optional). If omitted, the purl refers to the latest recipe revision available for the given version.
- Qualifier ``prev``: The Conan package revision (optional). If omitted, the purl refers to the latest package revision available for the given version and recipe revision.
- Qualifier ``repository_url``: The Conan repository where the package is available (optional). If omitted, ``https://center.conan.io`` as default repository is assumed.

Additional qualifiers can be used to distinguish Conan packages with different settings or options, e.g. ``os=Linux``, ``build_type=Debug`` or ``shared=True``.

If no additional qualifiers are used to distinguish Conan packages build with different settings or options, then the purl is ambiguous and it is up to the user to work out which package is being referred to (e.g. with context information).

Examples::

      pkg:conan/openssl@3.0.3
      pkg:conan/openssl.org/openssl@3.0.3?user=bincrafters&channel=stable
      pkg:conan/openssl.org/openssl@3.0.3?arch=x86_64&build_type=Debug&compiler=Visual%20Studio&compiler.runtime=MDd&compiler.version=16&os=Windows&shared=True&rrev=93a82349c31917d2d674d22065c7a9ef9f380c8e&prev=b429db8a0e324114c25ec387bfd8281f330d7c5c

conda
-----
``conda`` for Conda packages:

- The default repository is ``https://repo.anaconda.com``.
- The ``name`` is the package name.
- The ``version`` is the package version.
- The qualifiers: ``build`` is the build string.
  ``channel`` is the package stored location.
  ``subdir`` is the associated platform.
  ``type`` is the package type.
- Examples::

      pkg:conda/absl-py@0.4.1?build=py36h06a4308_0&channel=main&subdir=linux-64&type=tar.bz2

cpan
----
``cpan`` for CPAN Perl packages:

- The default repository is ``https://www.cpan.org/``.
- The ``namespace``:
  - To refer to a CPAN distribution name, the ``namespace`` MUST be present. In this case, the namespace is the CPAN id of the author/publisher. It MUST be written uppercase, followed by the distribution name in the ``name`` component. A distribution name may NEVER contain the string ``::``.
  - To refer to a CPAN module, the ``namespace`` MUST be absent. The module name MAY contain zero or more ``::`` strings, and the module name MUST NOT contain a ``-``

- The ``name`` is the module or distribution name and is case sensitive.
- The ``version`` is the module or distribution version.
- Optional qualifiers may include:

  - ``repository_url``: CPAN/MetaCPAN/BackPAN/DarkPAN repository base URL (default is ``https://www.cpan.org``)
  - ``download_url``: URL of package or distribution
  - ``vcs_url``: extra URL for a package version control system
  - ``ext``: file extension (default is ``tar.gz``)

- Examples::

      pkg:cpan/Perl::Version@1.013
      pkg:cpan/DROLSKY/DateTime@1.55
      pkg:cpan/DateTime@1.55
      pkg:cpan/GDT/URI-PackageURL
      pkg:cpan/LWP::UserAgent
      pkg:cpan/OALDERS/libwww-perl@6.76
      pkg:cpan/URI

cran
-----
``cran`` for CRAN R packages:

- The default repository is ``https://cran.r-project.org``.
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
  qualifiers key.
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
``docker`` for Docker images:

- The default repository is ``https://hub.docker.com``.
- The ``namespace`` is the registry/user/organization if present.
- The version should be the image id sha256 or a tag. Since tags can be moved,
  a sha256 image id is preferred.
- Examples::

      pkg:docker/cassandra@latest
      pkg:docker/smartentry/debian@dc437cc87d10
      pkg:docker/customer/dockerimage@sha256%3A244fd47e07d10?repository_url=gcr.io

gem
---
``gem`` for RubyGems:

- The default repository is ``https://rubygems.org``.
- The ``platform`` qualifiers key is used to specify an alternative platform.
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
  the ``generic`` type and eventually contributed back to this specification.
- as for other ``type``, the ``name`` component is mandatory. In the worst case
  it can be a file or directory name.
- Examples (truncated for brevity)::

      pkg:generic/openssl@1.1.10g
      pkg:generic/openssl@1.1.10g?download_url=https://openssl.org/source/openssl-1.1.0g.tar.gz&checksum=sha256:de4d501267da
      pkg:generic/bitwarderl?vcs_url=git%2Bhttps://git.fsfe.org/dxtr/bitwarderl%40cc55108da32


github
------
``github`` for GitHub-based packages:

- The default repository is ``https://github.com``.
- The ``namespace`` is the user or organization. It is not case sensitive and
  must be lowercased.
- The ``name`` is the repository name. It is not case sensitive and must be
  lowercased.
- The ``version`` is a commit or tag.
- Examples::

      pkg:github/package-url/purl-spec@244fd47e07d1004
      pkg:github/package-url/purl-spec@244fd47e07d1004#everybody/loves/dogs

golang
------
``golang`` for Go packages:

- There is no default package repository: this is implied in the namespace
  using the ``go get`` command conventions.
- The ``namespace`` and `name` must be lowercased.
- The ``subpath`` is used to point to a subpath inside a package.
- The ``version`` is often empty when a commit is not specified and should be
  the commit in most cases when available.
- Examples::

      pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c
      pkg:golang/google.golang.org/genproto#googleapis/api/annotations
      pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c#api

hackage
-------
``hackage`` for Haskell packages:

- The default repository is `https://hackage.haskell.org`.
- The `version` is package version.
- The `name` is case sensitive and use kebab-case.
- Examples::

      pkg:hackage/a50@0.5
      pkg:hackage/AC-HalfInteger@1.2.1
      pkg:hackage/3d-graphics-examples@0.0.0.2

hex
---
``hex`` for Hex packages:

- The default repository is ``https://repo.hex.pm``.
- The ``namespace`` is optional; it may be used to specify the organization for
  private packages on hex.pm. It is not case sensitive and must be lowercased.
- The ``name`` is not case sensitive and must be lowercased.
- Examples::

      pkg:hex/jason@1.1.2
      pkg:hex/acme/foo@2.3.
      pkg:hex/phoenix_html@2.13.3#priv/static/phoenix_html.js
      pkg:hex/bar@1.2.3?repository_url=https://myrepo.example.com


huggingface
------
``huggingface`` for Hugging Face ML models

- The default repository is ``https://huggingface.co``.
- The ``namespace`` is the model repository username or organization, if present. It is case sensitive.
- The ``name`` is the model repository name. It is case sensitive.
- The ``version`` is the model revision Git commit hash. It is case insensitive and must be lowercased in the package URL.
- Examples::

      pkg:huggingface/distilbert-base-uncased@043235d6088ecd3dd5fb5ca3592b6913fd516027
      pkg:huggingface/microsoft/deberta-v3-base@559062ad13d311b87b2c455e67dcd5f1c8f65111?repository_url=https://hub-ci.huggingface.co


luarocks
--------
``luarocks`` for Lua packages installed with LuaRocks:

- ``namespace``: The user manifest under which the package is registered.
  If not given, the root manifest is assumed.
  It is case insensitive, but lowercase is encouraged since namespaces
  are normalized to ASCII lowercase.
- ``name``: The LuaRocks package name.
  It is case insensitive, but lowercase is encouraged since package names
  are normalized to ASCII lowercase.
- ``version``: The full LuaRocks package version, including module version
  and rockspec revision.
  It is case sensitive, and lowercase must be used to avoid
  compatibility issues with older LuaRocks versions.
  The full version number is required to uniquely identify a version.
- Qualifier ``repository_url``: The LuaRocks rocks server to be used;
  useful in case a private server is used (optional).
  If omitted, ``https://luarocks.org`` as default server is assumed.

Examples::

      pkg:luarocks/luasocket@3.1.0-1
      pkg:luarocks/hisham/luafilesystem@1.8.0-1
      pkg:luarocks/username/packagename@0.1.0-1?repository_url=https://example.com/private_rocks_server/


maven
-----
``maven`` for Maven JARs and related artifacts:

- The default ``repository_url`` is ``https://repo.maven.apache.org/maven2``.
- The group id is the ``namespace`` and the artifact id is the ``name``.
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
      pkg:maven/groovy/groovy@1.0?repository_url=https://maven.google.com


mlflow
------
``mlflow`` for MLflow ML models (Azure ML, Databricks, etc.)

- The repository is the MLflow tracking URI. There is no default. Examples:

  - Azure ML: ``https://<region>.api.azureml.ms/mlflow/v1.0/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>``
  - Azure Databricks: ``https://adb-<numbers>.<number>.azuredatabricks.net/api/2.0/mlflow``
  - AWS Databricks: ``https://dbc-<alphanumeric>-<alphanumeric>.cloud.databricks.com/api/2.0/mlflow``
  - GCP Databricks: ``https://<numbers>.<number>.gcp.databricks.com/api/2.0/mlflow``

- The ``namespace`` is empty.
- The ``name`` is the model name. Case sensitivity depends on the server implementation:

  - Azure ML: it is case sensitive and must be kept as-is in the package URL.
  - Databricks: it is case insensitive and must be lowercased in the package URL.

- The ``version`` is the model version.
- Known qualifiers keys are: ``model_uuid`` and ``run_id`` as defined in the MLflow documentation.
- Examples::

      pkg:mlflow/creditfraud@3?repository_url=https://westus2.api.azureml.ms/mlflow/v1.0/subscriptions/a50f2011-fab8-4164-af23-c62881ef8c95/resourceGroups/TestResourceGroup/providers/Microsoft.MachineLearningServices/workspaces/TestWorkspace
      pkg:mlflow/trafficsigns@10?model_uuid=36233173b22f4c89b451f1228d700d49&run_id=410a3121-2709-4f88-98dd-dba0ef056b0a&repository_url=https://adb-5245952564735461.0.azuredatabricks.net/api/2.0/mlflow


npm
---
``npm`` for Node NPM packages:

- The default repository is ``https://registry.npmjs.org``.
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

- The default repository is ``https://www.nuget.org``.
- There is no ``namespace`` per se even if the common convention is to use
  dot-separated package names where the first segment is ``namespace``-like.
- Examples::

      pkg:nuget/EnterpriseLibrary.Common@6.0.1304

qpkg
----
``qpkg`` for QNX packages:

- There is no default package repository: this should be implied either from
  the ``namespace`` or using a repository base URL as ``repository_url``
  qualifiers key.
- The ``namespace`` is the vendor of the package. It is not case sensitive and must be
  lowercased.
- Examples::

      pkg:qpkg/blackberry/com.qnx.sdp@7.0.0.SGA201702151847
      pkg:qpkg/blackberry/com.qnx.qnx710.foo.bar.qux@0.0.4.01449T202205040833L

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

  - ``arch``: key for a package architecture, when relevant.
  - ``repository_url``: A repository URL where the artifact may be found, but not
    intended as the only location. This value is encouraged to identify a
    location the content may be fetched.
  - ``tag``: artifact tag that may have been associated with the digest at the time.
- Examples::

      pkg:oci/debian@sha256%3A244fd47e07d10?repository_url=docker.io/library/debian&arch=amd64&tag=latest
      pkg:oci/debian@sha256%3A244fd47e07d10?repository_url=ghcr.io/debian&tag=bullseye
      pkg:oci/static@sha256%3A244fd47e07d10?repository_url=gcr.io/distroless/static&tag=latest
      pkg:oci/hello-wasm@sha256%3A244fd47e07d10?tag=v1

pub
----
``pub`` for Dart and Flutter packages:

- The default repository is ``https://pub.dartlang.org``.
- Pub normalizes all package names to be lowercase and using underscores. The only allowed characters are `[a-z0-9_]`.
- More information on pub naming and versioning is available in the [pubspec documentation](https://dart.dev/tools/pub/pubspec)
- Examples::

      pkg:pub/characters@1.2.0
      pkg:pub/flutter@0.0.0

pypi
----
``pypi`` for Python packages:

- The default repository is ``https://pypi.org``. (Previously  ``https://pypi.python.org``.)
- PyPI treats ``-`` and ``_`` as the same character and is not case sensitive.
  Therefore a PyPI package ``name`` must be lowercased and underscore ``_``
  replaced with a dash ``-``.
- Examples::

      pkg:pypi/django@1.11.1
      pkg:pypi/django-allauth@12.23

rpm
---
``rpm`` for RPMs:

- There is no default package repository: this should be implied either from
  the ``distro`` qualifiers key or using a repository base URL as
  ``repository_url`` qualifiers key.
- The ``namespace`` is the vendor such as Fedora or OpenSUSE.
  It is not case sensitive and must be lowercased.
- The ``name`` is the RPM name and is case sensitive.
- The ``version`` is the combined version and release of an RPM.
- ``epoch`` (optional for RPMs) is a qualifier as it's not required for
  unique identification, but when the epoch exists we strongly
  encourage using it.
- ``arch`` is the qualifiers key for a package architecture.
- Examples::

      pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
      pkg:rpm/centerim@4.22.10-1.el6?arch=i686&epoch=1&distro=fedora-25

swid
-----
``swid`` for ISO-IEC 19770-2 Software Identification (SWID) tags:

- There is no default package repository.
- The ``namespace`` is the optional name and regid of the entity with a role of softwareCreator. If specified, name is required and is the first segment in the namespace. If regid is known, it must be specified as the second segment in the namespace. A maximum of two segments are supported.
- The ``name`` is the name as defined in the SWID SoftwareIdentity element.
- The ``version`` is the version as defined in the SWID SoftwareIdentity element.
- The qualifier ``tag_id`` must not be empty and corresponds to the tagId as defined in the SWID SoftwareIdentity element. Per the SWID specification, GUIDs are recommended. If a GUID is used, it must be lowercase. If a GUID is not used, the tag_id qualifier is case aware but not case sensitive.
- The qualifier ``tag_version`` is an optional integer and corresponds to the tagVersion as defined in the SWID SoftwareIdentity element. If not specified, defaults to 0.
- The qualifier ``patch`` is optional and corresponds to the patch as defined in the SWID SoftwareIdentity element. If not specified, defaults to false.
- The qualifier ``tag_creator_name`` is optional. If the tag creator is different from the software creator, the tag_creator_name qualifier should be specified.
- The qualifier ``tag_creator_regid`` is optional. If the tag creator is different from the software creator, the tag_creator_regid qualifier should be specified.

Use of known qualifiers key/value pairs such as ``download_url`` can be used to specify where the package was retrieved from.

- Examples::

      pkg:swid/Acme/example.com/Enterprise+Server@1.0.0?tag_id=75b8c285-fa7b-485b-b199-4745e3004d0d
      pkg:swid/Fedora@29?tag_id=org.fedoraproject.Fedora-29
      pkg:swid/Adobe+Systems+Incorporated/Adobe+InDesign@CC?tag_id=CreativeCloud-CS6-Win-GM-MUL

swift
-----
``swift`` for Swift packages:

- There is no default package repository: this should be implied from ``namespace``.
- The ``namespace`` is source host and user/organization and is required.
- The ``name`` is the repository name.
- The ``version`` is the package version and is required.
- Examples::

      pkg:swift/github.com/Alamofire/Alamofire@5.4.3
      pkg:swift/github.com/RxSwiftCommunity/RxFlow@2.12.4

Other candidate types to define:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``apache`` for Apache projects packages:
- ``android`` for Android apk packages:
- ``atom`` for Atom packages:
- ``bower`` for Bower JavaScript packages:
- ``brew`` for Homebrew packages:
- ``buildroot`` for Buildroot packages
- ``carthage`` for Cocoapods Cocoa packages:
- ``chef`` for Chef packages:
- ``chocolatey`` for Chocolatey packages
- ``clojars`` for Clojure packages:
- ``coreos`` for CoreOS packages:
- ``ctan`` for CTAN TeX packages:
- ``crystal`` for Crystal Shards packages:
- ``drupal`` for Drupal packages:
- ``dtype`` for DefinitelyTyped TypeScript type definitions:
- ``dub`` for D packages:
- ``elm`` for Elm packages:
- ``eclipse`` for Eclipse projects packages:
- ``gitea`` for Gitea-based packages:
- ``gitlab`` for GitLab-based packages:
- ``gradle`` for Gradle plugins
- ``guix`` for Guix packages:
- ``haxe`` for Haxe packages:
- ``helm`` for Kubernetes packages
- ``julia`` for Julia packages:
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

This document is licensed under the MIT license.
