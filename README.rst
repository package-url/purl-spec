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
  https://links.sonatype.com/products/nxiq/doc/component-identifier


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


Components are designed such that they form a hierarchy from the most significant component
on the left to the least significant component on the right.


A `purl` must NOT contain a URL Authority i.e. there is no support for
`username`, `password`, `host` and `port` components. A `namespace` segment may
sometimes look like a `host` but its interpretation is specific to a `type`.


Some `purl` examples
~~~~~~~~~~~~~~~~~~~~

::

    pkg:bitbucket/birkenfeld/pygments-main@244fd47e07d1014f0aed9c

    pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie

    pkg:docker/cassandra@sha256:244fd47e07d1004f0aed9c
    pkg:docker/customer/dockerimage@sha256:244fd47e07d1004f0aed9c?repository_url=gcr.io

    pkg:gem/jruby-launcher@1.1.2?platform=java
    pkg:gem/ruby-advisory-db-check@0.12.4

    pkg:github/package-url/purl-spec@244fd47e07d1004f0aed9c

    pkg:golang/google.golang.org/genproto#googleapis/api/annotations

    pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources
    pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?repository_url=repo.spring.io/release

    pkg:npm/%40angular/animation@12.3.1
    pkg:npm/foobar@12.3.1

    pkg:nuget/EnterpriseLibrary.Common@6.0.1304

    pkg:pypi/django@1.11.1

    pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
    pkg:rpm/opensuse/curl@7.56.1-1.1.?arch=i386&distro=opensuse-tumbleweed

(NB: some checksums are truncated for brevity)


Specification details
~~~~~~~~~~~~~~~~~~~~~

The `purl` specification consists of a core syntax definition and independent
type definitions:

- `Package URL core <PURL-SPECIFICATION.rst>`_: Defines a versioned and
  formalized format, syntax, and rules used to represent and validate `purl`.

- `Type definitions <PURL-TYPES.rst>`_: Defines `purl` types (e.g. maven, npm,
  cargo, rpm, etc) independent of the core specification. Definitions also
  include types reserved for future use.


Known implementations
~~~~~~~~~~~~~~~~~~~~~

- in Golang: https://github.com/package-url/packageurl-go
- for .NET: https://github.com/package-url/packageurl-dotnet
- for the JVM: https://github.com/package-url/packageurl-java,
  https://github.com/sonatype/package-url-java
- in Python: https://github.com/package-url/packageurl-python
- in Rust: https://github.com/package-url/packageurl-rs
- in JS: https://github.com/package-url/packageurl-js


Users, adopters and links
~~~~~~~~~~~~~~~~~~~~~~~~~
- `Scancode Toolkit <https://github.com/nexB/scancode-toolkit>`_: Reports
  `purl` from parsed package manifests using https://github.com/package-url/packageurl-python
- `OWASP Dependency-Track <https://www.owasp.org/index.php/OWASP_Dependency_Track_Project>`_: 
  Open source component analysis platform
- `CycloneDX <https://github.com/CycloneDX>`_: A lightweight software
  bill-of-material (SBOM) specification
- `SPDX <https://spdx.dev>`_: A data exchange standard for human-readable and 
  machine-processable software bill-of-materials (SBOM)
- `OSS Index <https://ossindex.sonatype.org>`_: A free catalog of Open Source
  Components and scanning tools to help developers identify vulnerable components
- `Sonatype Nexus Lifecycle <https://www.sonatype.com/product-nexus-lifecycle>`_:
  Enterprise grade Open Source component management


License
~~~~~~~

This document is licensed under the MIT license
