
# Package-URL (PURL) Specification

Software ecosystems have evolved into highly interconnected networks of
components, packages, and dependencies. Managing this complexity demands a
robust, uniform mechanism to identify and track software packages across
diverse ecosystems and tools. Package-URL (PURL) was developed to address
this challenge by providing a simple, consistent, and flexible approach to
identifying software packages with precision and clarity.

PURL introduces a standardized URL-based syntax that uniquely identifies
software packages, independent of their ecosystem or distribution channel.
Unlike traditional identification methods, PURL embeds critical metadata
directly into its structure, enabling efficient, accurate package
identification at scale. This standardization ensures interoperability
between tools and ecosystems, fostering greater collaboration and reducing
ambiguity in software supply chain management.

Challenges addressed by PURL:

- **Ambiguity in Package Identification:** With diverse naming conventions
across ecosystems, identifying software packages reliably has historically
been a challenge. PURL eliminates this ambiguity by creating a universal
identifier with a predictable structure.
- **Cross-Ecosystem Interoperability:** Developers, organizations, and tools
often work across multiple ecosystems, each with its own package management
systems. PURL harmonizes these differences, enabling seamless
interoperability.
- **Enhanced Traceability and Risk Management:** In an era where supply chain
security is critical, PURL provides the foundation for identifying and
tracing packages to their origins, dependencies, and potential
vulnerabilities.
- **Tooling and Automation:** By standardizing package identification, PURL
simplifies tooling development, automation, and integration for tasks such
as software composition analysis, vulnerability management, and license
 compliance.

PURL is an Ecma standard: [ECMA-427](https://tc54.org/purl/), and is
 in process to also become an ISO standard.

## Why use PURL?

A PURL is useful to reliably reference the same software package
using a simple and expressive syntax and conventions based on familiar URLs.

PURL is used as a standard identifier for software components in:
- A CycloneDX or SPDX SBOM
- Most software vulnerability databases such as [OSV](https://osv.dev/), 
[Sonatype OSS Index](https://ossindex.sonatype.org/), and [VulnerablCode](https://public2.vulnerablecode.io/)
- Many package repositories, such as [Crates.io](https://crates.io/) and 
[Packagist](https://packagist.org/)

PURL was recently added to the standard [CVE Record Format v5.2.0](https://github.com/CVEProject/cve-schema/releases/tag/v5.2.0).

## Getting started

A PURL is a URL composed of seven components:

    scheme:type/namespace/name@version?qualifiers#subpath

Components are separated by a specific character for unambiguous parsing.

The definition for each component is:

| Component  | Requirement | Description|
| ---------- | ----------- |:------------------------------------------------------ |
| scheme     | Required    | The URL scheme with the constant value of "pkg". One of the primary reasons for this single scheme is to facilitate the future official registration of the "pkg" scheme for Package-URLs. |
| type       | Required    | The package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc. |
| namespace  | Optional    | A name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization. Namespace is type-specific. |
| name       | Required    | The name of the package. |
| version    | Optional    | The version of the package.  |
| qualifiers | Optional    | Qualifier data for a package such as OS, architecture, repository, etc. Qualifiers are type-specific. |
| subpath    | Optional    | Subpath within a package, relative to the package root. |

Components are designed such that they form a hierarchy from the most 
significant component on the left to the least significant component on the 
right.

### Some PURL examples

    pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
    pkg:docker/cassandra@sha256:244fd47e07d1004f0aed9c
    pkg:gem/jruby-launcher@1.1.2?platform=java
    pkg:golang/google.golang.org/genproto#googleapis/api/annotations
    pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?repository_url=repo.spring.io%2Frelease&packaging=sources
    pkg:npm/%40angular/animation@12.3.1
    pkg:nuget/EnterpriseLibrary.Common@6.0.1304
    pkg:pypi/django@1.11.1
    pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25
    pkg:rpm/opensuse/curl@7.56.1-1.1.?arch=i386&distro=opensuse-tumbleweed

(NB: the checksum for the docker example is truncated for brevity)

### PURL specification

The PURL specification consists of a core syntax definition and specific
PURL type definitions:

The core PURL syntax is defined in the Package-URL Specification / [ECMA-427](https://tc54.org/purl/). See ECMA-427 *Clause 5 Package-URL specification* 
for syntax details.

Each package manager, platform, type, or ecosystem has its own conventions
and protocols to identify, locate, and provision software packages. The 
package **type** is the component of a Package-URL that is used to capture 
this information with a short string such as **maven**, **npm** and **pypi**. 

See ECMA-427 *Clause 6 Package-URL Type Definition Schema* for PURL type 
definition details.

## Package-URL type definitions

PURL type definitions are maintained in a set of JSON Schema files with a
separate file for each PURL **type**. and a simple index of all currently registered PURL types. You can find comprehensive PURL type information in 
this repository as follows:

- One JSON file for each PURL type definition at:
  https://github.com/package-url/purl-spec/tree/main/types

- Markdown documentation, generated from each PURL type JSON definition at:
  https://github.com/package-url/purl-spec/tree/main/types-doc

- The JSON Index listing of all registered PURL types at:
  https://github.com/package-url/purl-spec/tree/main/purl-types-index.json

## Adopters

PURL (Package-URL) - [ECMA-427](https://ecma-tc54.github.io/ECMA-427/) - has been adopted by other specifications and is supported by many tools.
- See [PURL-Adoption-Specifications](https://www.packageurl.org/#:~:text=PURL%20Adoption%20%2D%20Specifications) for the list of these specifications.
- See [PURL-Adoption-Tools](https://www.packageurl.org/#:~:text=PURL%20v1.0-,Software%20Tools) for the list of these tools.

If you want to add a tool or specification that supports PURL please create an issue in the [Package-URL website repostory](https://github.com/package-url/www.packageurl.org/issues). There are separate issue templates for 'Add a Tool' and 'Add a Specification" because the data fields are different.

**NB** There is a "staging website" for Package-URL at: https://package-url.github.io/www.packageurl.org/ that will have the most recent information about specifications and tools that have adopted PURL. We normally update the "production" website at: https://www.packageurl.org/ weekly.

## Support

If you have a specific problem, suggestion or bug, please submit a 
[GitHub issue](https://github.com/package-url/purl-spec/issues).

For quick questions or socializing, join the PURL community discussions 
at:
- [AboutCode Slack](https://aboutcode-org.slack.com/archives/C08LBQMA7DE)
- [CycloneDX Slack](https://cyclonedx.slack.com/archives/C06KTE3BWEB)
- [Gitter](https://matrix.to/#/#package-url_Lobby:gitter.im)

## License

Copyright (c) the purl authors

License for the **purl-spec** software: 

- SPDX-License-Identifier: MIT

License for the ECMA-427 standard:
- SPDX-License-Identifier: LicenseRef-scancode-ecma-standard-copyright-2024