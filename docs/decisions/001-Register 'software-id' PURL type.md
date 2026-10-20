---
status: proposed
date: 2026-10-19
---

# Decision: Add new PURL type 'software-id'

## Context / Problem

The current set of registered PURL `types` covers a wide range of package
ecosystems. However, there remains a significant gap in the capability to use
PURL to identify *non-ecosystem* software components, particularly
*commercial*, *proprietary*, or *standalone open source* software that is not
distributed through a package manager or authoritatively available on a
repository with a supported PURL `type`, such as 'generic' or 'git'.

One reason for the gap is that many concepts in the PURL specification were
originally based on:
- Software package managers and repositories (mostly open source) that provide
  a clear mechanism for identifying and locating software components.
- Open source software where the code and other artifacts are available from a
  public resource.

The community discussions about the 'software-id' PURL `type` have converged
from two "use cases":
- Commercial or proprietary software including first-party (e.g., internal use
  only) software.
- Standalone open source projects that do not use public package management
  systems or repositories (e.g., Maven, npm, PyPI, etc.).

Some key similarities between the use cases are:
- The software publisher uses first-party systems to identify and distribute
  its software. First-party means internal system(s); these are public for
  open source projects and typically private for commercial or proprietary
  products.
- Many software publishers have complex organizational structures for a large
  number of products (commercial or proprietary) or projects (open source).

Some key differences between the use cases are:
- A commercial or proprietary software publisher may frequently change its
  product names or product line structure.
- Open source projects are less likely to make frequent changes to project
  names or project groups because major planned changes are normally discussed
  and decided publicly.
- Access to software from a commercial software publisher usually requires
  access to a private resource such as a customer portal.

The key common requirement between the use cases is that they both require
a solution where a software publisher can define PURLs for products or
projects that will be recognized by customers or consumers of its software
without using a third-party database, repository or package manager.

See [More Information](#community-discussion-references) for links to the most
important GitHub issues and discussions about the `software-id' PURL `type`.

## Solution

Introduce a new PURL type` named 'software-id'.

This PURL `type` is intended to cover:
- *Standalone open source projects* (e.g., the Linux Kernel)
- *Commercial and proprietary software* (e.g., Acme Database Server)
- *Internally developed applications* that do not belong to a recognized
  package ecosystem
- *Binary-only or installable software* where no manifest-based or
  registry-driven packaging exists


### PURL Components

| PURL Component | Requirement  | Description                               |
| -------------- |--------------|-------------------------------------------|
| type           | Required     | constant value: 'software-id'             |
| namespace      | Required     | The first segment of the namespace defines the "authority" for this 'software-id'. When the segment contains a dot, it is treated as a domain-qualified namespace representing the internet domain of the publishing entity. When the first segment does not contain a dot, it is a registry-based namespace that must be registered in the PURL registry.  |
| name            | Required    | Name of the software component or package. |
| version         | Optional    | Version string identifying the specific release, tag, or snapshot of the product.  |
| qualifiers      | Optional    | Key-value pairs to define additional characteristics of the software such as the architecture, edition or locale.|
| subpath         | Optional    | The subpath optionally identifies a specific module, subcomponent, or file within the broader software product. |

The most unique aspect of the 'software-id` PURL` type at the PURL component
level is the use of the `namespace` component to define an **authority** that
is responsible for the definition of PURLs instead  of a third-party package
registry or repository as that authority.

### Namespace

The `namespace` for the 'software-id' PURL `type` represents an **authority**
in the first segment. Additional segments are optional and may represent any
element of an organizational hierarchy such as a publisher name, business
units, product lines, or sub-projects.

#### 1. "Authority" as the namespace anchor
The first segment of the `namespace` defines the **authority** for the
identity and discovery of a software component or package for this PURL
`type`. It takes one of two forms:

- A domain-qualified `namespace` contains a dot in the first segment,
  indicating an internet domain name. The domain identifies the **authority**
  asserting the software's metadata and enables decentralized verification
  through mechanisms such as `.well-known/` files or TEA Discovery. While
  domain names are leased rather than owned, and may change hands over time,
  they provide a resolvable, globally unique starting point that no other
  field can offer. Domain-qualified `namespaces` are self-asserted and do not
  require registration in the PURL registry.

- A registry-based `namespace` does not contain a dot in the first segment. It
  must be registered in the PURL registry, which serves as the authoritative
  identity for that `namespace`. A registry-based `namespace` that is
  not registered is invalid. This form is intended for projects that do not
  control a domain or prefer centralized registration, such as long-standing
  open source projects maintained by individuals or informal groups.

#### 2. Disambiguation through domain
For domain-qualified namespaces, organizations with identical or similar names
are disambiguated by their domain. For example:

```
pkg:software-id/acme-industries.com/analytics-suite@5.2.1
pkg:software-id/acmerobotics.org/robot-os@2.3.0
```

Both organizations may call themselves "Acme," but the domain provides clear
differentiation without relying on a publisher segment in the `namespace`.
For registry-based `namespaces`, the PURL registry enforces uniqueness. Each
registered `namespace` is distinct, and conflicts are resolved through the
registration process.

#### 3. Flexible namespace segments for domain-qualified namespaces
The PURL `namespace` component supports multiple slash-separate segments (with
no specific limit) so the **authority** for a 'software-id' PURL may want to
include a publisher name as the first `namespace` segment after
the domain to document a human recognizable name for the **authority**.
Including a publisher name is recommended when disambiguation is needed, for
example when a single domain distributes software on behalf of multiple
organizations. However, many publishers operate under a single identity tied
directly to their domain, making a separate publisher segment redundant in
those cases.

Additional `namespace` segments allow an **authority** to represent internal
organization elements such as business units, product lines, divisions, etc.
The PURL `type` definition for `software_id' does not prescribe the meaning of
these segments. Their use and interpretation are determined by the publishing
**authority**. For example:

```
pkg:software-id/acme.com/AcmeApplication@1.0.0
pkg:software-id/acme.com/Acme%20Robotics/robot-os@2.3.0
pkg:software-id/acme.com/Acme%20Robotics/Industrial/motion-controller@4.1.0
pkg:software-id/distributor.com/AcmeCorp/appsuite@1.0.0
```

### Qualifiers
The PURL `qualifiers` component provides a flexible way to provide additional
identity or discovery information in a PURL using `key-value` pairs. Some
`qualifier-keys` that will likely be useful for a 'software-id' PURL include:
- 'arch': CPU architecture the software was built for (e.g., 'x86_64',
  'arm64').
- 'edition': The specific edition of a product (e.g., 'community' or
   'enterprise').
- locale': Language of the software, expressed as an ISO 639-1 code (e.g.,
  'en') or a full BCP 47 language tag (e.g., 'en-GB').
- 'target': Target software environment (e.g., 'windows', 'java', android').

This use of `qualifiers` is common across PURL `types` but highlighted here
because `software-id' PURL `types` are likely to use several `qualifiers`.

## Decision Drivers

Some of the key decision drivers in addition to the topics covered in the
[Context / Problem](#context--problem) section were:

- Any PURL `type` definition should follow the "intrinsic" principle that a
  PURL can be generated in a deterministic, reproducible manner without
  requiring access to a central database or registry that defines valid PURLs.
  This is implemented with the concept of a self-asserted **authority** in the
  `namespace` component with flexibiity for each **authority** to define the
  level of detail.
- A preference for one solution to cover both commercial or proprietary
  products and open source projects if possible. The reasons for this
  preference are simplicity and the difficulty in some cases of
  distinguishing between commercial or proprietary and open source software.

## Non-goals
The following use cases are not suitable for tracking with 'software-id':
- Services: There is a separate discussion of adding a new 'PURL `type` for
  services such as those provided via an API. One of the key differences
  between software and services is that a service does not have artifact that
  it is distinct from the delivery of the service. There may be some useful
  similarities between 'software-id' and a new `service' PURL `type` such as
  use of the `namespace` component for artifact identification.
- Hardware: There are already several well-known identifiers for hardware
  artifacts such as [GTIN](https://www.gs1.org/standards/id-keys/gtin). The
  'software-id' or other PURL `types` may be used to identify software that is
  "embedded" on a device, but not the device itself. See also the [CycloneDX
  HBOM](https://cyclonedx.org/capabilities/hbom/) for examples of how to
  identify hardware components.

## Alternatives Considered

### Use 'generic' PURL `type`
The 'generic' PURL type is the current primary way to create a PURL for
software that is not distributed through a package manager or authoritatively
available on a repository with a supported PURL. Using the 'generic' `type`
requires using `qualifiers` to provide any details beyond the software `name`
and `version`. `Qualifiers` are `key=value` pairs which do not scale well and
do not support the important vulnerability or dependency management use cases
for PURL. The 'generic' PURL `type` will remain available for use cases not
covered by the 'software-id' or other existing PURL `types`.

### Separate PURL `types` for commercial or proprietary and open source
software
There were several discussions about defining separate PURL `types` for
commercial or proprietary software and for open source software. The main
points of distinction were related to the perception that publishers of
commercial or proprietary software would want to define more complex
organizational elements in the `namespace` component and more standardized
`qualifiers` that would not translate well to open source projects. One
example was the idea of requiring a publisher name segment in the `namespace`
after the domain. The community conclusions were that:
- Defining standard rules for`namespace` or `qualifiers` for all commercial or
  proprietary software was unrealistic, and
- Offering flexibility for each publisher (**authority**) to define its own
  `namespace` and `qualifiers` information was more realistic.

## Decision Outcome

This new PURL `type` has been other active discussion since early 2025.
This decision is pending final approval by TC54/TG2.

### `Type` name
Two proposed PURL `type` names for this new PURL `type` were 'sid' as an
acronym for "Software ID" and 'scid' for "Software Component IDentification".
We agreed on the PURL `type` name 'software-id' to make the PURL `type`name
clear without a new acronym. There is some potential for confusion with
"SWID tags" which are already registered as the 'swid' PURL `type`, but using
the full descriptive name should be less confusing than acronyms like 'sid' or
'scid'.


## More Information

### Community Discussion References

The community discussion of this proposed PURL `type` started in July, 2025
and has been well-documented in the following issues in the `purl-spec`
repository:
- [Add new PURL type for non-packaged software](https://github.com/package-url/purl-spec/issues/516)
- [FOSS vs proprietary considerations for new sid PURL type](https://github.com/package-url/purl-spec/issues/784)
- [Define namespace for new "software-id" PURL type](https://github.com/package-url/purl-spec/issues/834)
- [Consider alternative names for new scid PURL type](https://github.com/package-url/purl-spec/issues/835)
- [Register new PURL type: sid for packages that do not have a registry](https://github.com/package-url/purl-spec/issues/837)

There also an "omnibus" discussion that summarizes the commentary from the
issues by topic and contains additional commentary: [Design for new PURL type: 'software-id'](https://github.com/package-url/purl-spec/discussions/841).


### Interoperable Successor to CPE

One of the design goals of this PURL `type` is to enable interoperability
with existing systems that utilize legacy identifiers such as CPE. While CPE
provides a structured method of identifying software, it suffers from
centralization, a rigid schema, and reliance on manual human curation.
These characteristics make it difficult to scale in modern, dynamic
environments where new software products, forks, and distributions emerge
continuously. In contrast, the PURL format is inherently decentralized and
URI-friendly, enabling toolchains, vendors, and open source communities to
generate identifiers independently without requiring central registry
approval. Despite this shift, 'software-id' PURLs aim to retain semantic
compatibility with CPE by using comparable fields and qualifiers, ensuring
they can be adopted by inventory, vulnerability, and compliance systems that
currently rely on CPE naming conventions.

| CPE Field     | 'software-id' PURL Component        | Notes                                                                 |
|---------------|-------------------------------|-----------------------------------------------------------------------|
| `part`        | (implicit in PURL context)     | CPE uses 'a' (application), 'o' (OS), 'h' (hardware); 'software-id' PURL assumes software |
| `vendor`      | namespace              | Domain or registry-based |
| `product`     | name                   | Software project, product, or component name                                         |
| `version`     | version                | Version string                                                       |
| `update`      | (not directly mapped)  | Could be embedded in `version` or excluded for simplicity            |
| `edition`     | qualifier-key: 'edition' | Directly mapped                |
| `language`    | qualifier-key: 'locale'  | Supports ISO 639-1 and BCP 47  |
| `sw_edition`  | qualifier-key: 'edition' | May be combined under `edition` |
| `target_sw`   | qualifier-key: 'target'| Target software environment (e.g., 'java', 'windows')               |
| `target_hw`   | qualifier-key: 'arch'  | CPU architecture (e.g., 'x86_64', 'arm64')                           |

'software-id' PURLs align with CPE parts `a` (application) and `o` (operating
system). Hardware identification (CPE part `h`) is out of scope. Established
standards such as GS1 GMN and GTIN already serve that purpose.

### SWID
While SWID historically been used in asset and inventory contexts to identify
installed software, it is:

- overly complex for general use,
- tightly coupled to specific enterprise and government implementations, and
- requires fields such as `tagId` that are not always meaningful or available
  in modern DevOps and security pipelines.

SWID used to have tagvault, which would have provided a global registry for
commercial and non-packaged software, but the company behind it folded.
