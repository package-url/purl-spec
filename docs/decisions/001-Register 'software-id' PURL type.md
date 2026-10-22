---
status: proposed
date: 2026-10-21
---

# Decision: Add new PURL type 'software-id'

## Context / Problem

The current set of registered PURL `types` cover a wide range of package
ecosystems, but it is difficult to use PURL to identify non-ecosystem-based
software packages, particularly C/C++ packages and other standalone open
source software that does not reside in an incorporated package registry and
commercial or other software that is not distributed through a package manager
or available with a currently registered PURL `type`. Until now the primary
option for this type of software has been the `generic` PURL type which is
highly problematic because arbitrary PURL component values make it
hard to create identical or even similar PURLs for the same package
independently.

One reason for this difficulty is that PURL was originally designed for open
source ecosystems with package repositories (often centralized) that structure
the naming, identification and location of their packages.

The proposed 'software-id' PURL `type` community discussions have converged
from two use cases:

- C/C++ and other standalone open source projects that do not use a public
  package repository or registry, e.g., such as packages that are not hosted at
  Maven, npm, GitHub, or PyPI. This includes for example the packages of the
  Linux Kernel, some packages of the Apache Software Foundation, and a
  significant set of essential software that powers the modern internet.

- Commercial or proprietary software including internal use only software.

*Note: for the remainder of this document we use the simpler term "commercial"
to reference "commercial" or other "proprietary" software.*

For these two use cases, there is eventually a much larger number of package
naming authorities than with structured package ecosystems that we track as
registered PURL `types`. There is a finite number of programming languages and
related ecosystems, but there are thousands or possibly millions of standalone
projects and commercial software products. A path to accommodate this volume
is using internet domains to avoid centralized registrations of hundreds or
thousands of new PURL `types`.

Some key similarities between the use cases are that each publisher
manages internally consistent naming conventions and version or release
numbering schemes for its software and is responsible for ensuring the
uniqueness of these names and versions for their own software. Many software
publishers also have complex organizational structures for their commercial
products or open source projects.

Both use cases demand a decentralized, federated solution for software
publishers to define their own PURLs consistently for use in their software
supply chains without external dependencies on a centralized naming authority.

## Solution

The solution is to register a new PURL `type` named 'software-id' that uses
internet domains for decentralized PURL definitions, federated through simple
conventions and backed by an optional shared and aggregated registry hosted at
`packageurl.org`.

This PURL `type` covers:

- *Standalone open source projects* (e.g., the Linux Kernel)
- *Open source foundations* (e.g., the Apache Software Foundation)
- *Commercial and proprietary software* (e.g., Acme Database Server)
- *Internally developed applications* not in a registered package type

### PURL Components for the 'software-id' `type`

| Component  | Requirement | Description                         |
| -----------|-------------|-------------------------------------|
| type       | Required    | Constant value: 'software-id'       |
| namespace  | Required    | First namespace segment is an internet domain. Other segments are optional and defined by that domain's organization. |
| name       | Required    | Package name as defined in spec.    |
| version    | Optional    | Version as defined in spec.         |
| qualifiers | Optional    | Key-value pairs as defined in spec. |
| subpath    | Optional    | Subpath as defined in spec.         |


### PURL `namespace` component

The special characteristics of the 'software-id PURL `type` are that:

- The `namespace` component is required.
- The first segment of the `namespace` component is required to be an
  internet domain which defines the **authority** for naming its own
  software.

This domain/authority is responsible for the definition of additional
`namespace` segments, name and version conventions, and the uniqueness of
PURLs within its domain. This is very similar to the way that ecosystem
package registries or repositories like PyPI, Maven or npm are responsible for
their naming and versioning rules.

The other `namespace` segments are optional, domain-defined, and may represent
any element of an organizational hierarchy such as a project, sub-project,
publisher name, business unit, or product line.

The `packageurl.org` domain is a special domain to register PURLs for an
organization, community or person that does not have or does not want to
use their own domain **authority** for PURLs. It can also serve as an
aggregator for 'software-id' PURLs.

The definitions for the other PURL components are not special at the level of
the 'software-id' PURL `type` but a domain/authority may define its own
internal rules for these PURL components in its domain.

#### Disambiguation through domain

Since a 'software-id' PURL `namespace` is always qualified by a domain,
different organizations that release software with similar names will be able
to provide unique PURLs. For example, these PURLs have the same `name` and
`version` but different domains in the `namespace` component:

```
pkg:software-id/acme-industries.com/foo/analytics-suite@5.2.1
pkg:software-id/acmerobotics.org/foo/analytics-suite@5.2.1
```

Each domain acts as a PURL registry that enforces uniqueness. The shared
`packageurl.org` registry enforces uniqueness during the registration
process, where each registration are files published at a `.well-known` URI.

#### Flexible namespacing

The PURL `namespace` component supports multiple slash-separated segments
(with no specific limit) so that the **authority** for a 'software-id' PURL
domain can document deep software naming hierarchies as needed. A `namespace`
segment can be used to represent a project or team, a business unit or a
product line, or any other organization element. The structure or hierarchy of
these `namespace` segments is defined by the **authority** for this software.

The PURL `type` definition for 'software_id' does not prescribe the meaning of
the `namespace` segments. These are determined (and optionally documented) at
the domain level by the publisher. For example:

```
pkg:software-id/packageurl.org/baz/foo/bar@123
pkg:software-id/kernel.org/linux@6.18.57
pkg:software-id/apache.org/logging/log4j-core@2.21.0
pkg:software-id/acme.com/AcmeApplication@1.0.0
pkg:software-id/acme.com/AcmeRobotics/robot-os@2.3.0
pkg:software-id/acme.com/AcmeRobotics/Industrial/motion-controller@4.1.0
```

#### PURL discovery and resolution

The requirement that the first  `namespace` segment for a 'software-id' PURL
is a domain name makes it possible to discover and resolve software package
PURLs at a domain address with:

- A `.well-known/purl` [URI](https://en.wikipedia.org/wiki/Well-known_URI),
  served at that domain and containing the definitions and references about the
  PURLs defined at that domain, and a PURL catalog. This well-known URI will be
  registered with [IANA](https://www.iana.org/assignments/well-known-uris).

- The shared `packageurl.org` domain serving a `.well-known/purl` URI of
  registered PURL `namespaces` and providing a centralized registry for
  open source projects or other organizations that want to standardize their
  PURLs without having to host their own `.well-known/purl` URI, either because
  they do not control a domain or they prefer centralized registration.

The `packageurl.org` domain will host the shared registry of PURLs prefixed
with `pkg:software-id/packageurl.org/` and also serve as an aggregator for
other domains to make discovery easier with mirrored snapshots of their
`./well-known/purl` PURL definitions and catalogs.

The `packageurl.org` domain will support a simple process to register
`software-id` PURL namespaces. The data of this PURL registry will be stored as
JSON data files in a public git repository, and that data will be served
directly from `packageurl.org/.well-known/purl`.
That git repository is at https://github.com/package-url/purl-registry/

### PURL `qualifiers' component

Some `qualifier-keys` that will likely be useful for a 'software-id' PURL
include:

- 'arch': CPU architecture the software was built for (e.g., 'x86_64',
  'arm64').
- 'edition': The specific edition of a commercial product (e.g., 'community'
  or 'enterprise').
- 'locale': Language of the software as an ISO 639-1 code (e.g., 'en') or a
  full BCP 47 language tag (e.g., 'en-GB').
- 'target': Target software environment (e.g., 'windows', 'java', 'android').

This use of `qualifiers` is common across PURL `types` but highlighted here
because many 'software-id' PURLs may use multiple `qualifiers`.

## Decision Drivers

Some of the decision drivers beyond the [Context / Problem](#context--problem)
section were:

- A PURL should be obvious from observing the software. We do not have a
  manifest or convention yet to make `software-id` self-documenting and
  obvious, but the `software-id` PURL type reduces the search for a
  valid PURL to the domain name or to the shared registry or both.

- A preference for one solution to cover both commercial products and open
  source projects if possible. The reasons for this preference are simplicity
  and the difficulty in some cases of distinguishing between commercial or
  proprietary and open source software.

## Non-goals

These use cases are not suitable for 'software-id':

- Services: Not in scope. There is a separate discussion for a new 'service'
  PURL `type` for online APIs. The domain-based `namespace` structure from the
  'software-id' PURL `type` may, however, be useful for a `service` PURL
  `type`.

- Hardware: Not in scope. The 'software-id' and PURL in general may be used to
  identify software embedded in devices, but it is not intended to describe a
  hardware device or its components. There are already several well-known
  identifiers for hardware artifacts such as [GTIN](https://www.gs1.org/standards/id-keys/gtin)

## Alternatives Considered

### Use 'generic' PURL `type`

The 'generic' PURL `type` is the current way to create a PURL for software
without a registered PURL. Using the 'generic' `type` requires `qualifiers`
for a download URL and it is too easy to create different PURLs for the same
generic package. The 'generic' PURL `type` will remain as an option for use
cases not covered by 'software-id' or other registered PURL `types`.

### Separate PURL `types` for commercial and open source software

There were several discussions about defining separate PURL `types` for
commercial software and for open source software. The main points of
distinction were related to the perception that commercial publishers will
want to define complex and structured `namespace` segments and many
`qualifiers` that may not apply well to open source projects. One example idea
was requiring a publisher segment in the `namespace` after the domain.
The community conclusions were that:

- Defining standard rules for `namespace` or `qualifiers` for all commercial
  publishers is unrealistic, and

- Offering flexibility for each publisher (e.g., the **authority** or domain
  in the 'software-id' `type`) to define its own `namespace` segments and
  `qualifiers` was more practical.

### Requiring use of a TEA Server for verification

Some community members proposed to make the new Transparency Exchange API
specification mandatory for verifying a domain in the 'software-id'
`namespace` and for further retrieving software information from a TEA Server.
TEA has been approved by Ecma TC54 for submission to the Ecma General Assembly
in December 2026. The community agreed that the use of a TEA Server should be
an option, not a requirement.

## Decision Outcome

This new PURL `type` has been under active discussion since early 2025.
This decision is pending final approval by TC54/TG2.

### Community Discussion References

The community discussion of this proposed PURL `type` started in July, 2025
and has been well-documented in the following issues in the `purl-spec`
repository:

- [Add new PURL type for non-packaged software](https://github.com/package-url/purl-spec/issues/516)
- [FOSS vs proprietary considerations for new sid PURL type](https://github.com/package-url/purl-spec/issues/784)
- [Define namespace for new "software-id" PURL type](https://github.com/package-url/purl-spec/issues/834)
- [Consider alternative names for new scid PURL type](https://github.com/package-url/purl-spec/issues/835)
- [Register new PURL type: sid for packages that do not have a registry](https://github.com/package-url/purl-spec/issues/837)

There also an "omnibus" discussion thread that summarizes the commentary from
the issues by topic and contains additional commentary:
[Design for new PURL type: 'software-id'](https://github.com/package-url/purl-spec/discussions/841)

### 'software-id' `type` name

Two proposed PURL `type` names for this new PURL `type` were 'sid' as an
acronym for "Software ID" and 'scid' for "Software Component IDentification".
The community agreed to use the PURL `type` name 'software-id' to make the
`type` name obvious and clear without creating a new acronym. There is some
potential for confusion with "SWID tags" which are already registered as the
'swid' PURL `type`, and using the longer 'software-id' descriptive name should
be less confusing than acronyms like 'sid' or 'scid'.

### PURL discovery

The PURL approach to discovering 'software-id' `types` is to use static files
located at `.well-known/` location of the domain used as the first segment of
that PURL. (Technically these files could be dynamically generated.)

## More Information

### Interoperable Successor to CPE

One of the design goals of this PURL `type` will be to enable interoperability
with existing systems that utilize legacy identifiers such as CPE. While CPE
provides a rich and structured method of identifying software, it suffers from
centralization, a rigid schema, and reliance on manual human curation to
assign arbitrary names. These characteristics make it difficult to scale in
modern, dynamic environments where new software projects, forks, and
distributions emerge continuously.

In contrast, the PURL format is inherently decentralized and URI-friendly,
enabling toolchains, vendors, and open source communities to generate
identifiers independently without requiring central registry approval. Despite
this shift, 'software-id' PURLs aim to retain high level semantic
compatibility with CPE by using similar fields and qualifiers, ensuring they
can be adopted more easily by the ecosystem that currently rely on CPE names.

| CPE Field    | 'software-id' PURL Component | Notes                                         |
|--------------|------------------------------|-----------------------------------------------|
| `part`       | PURL assumes software        | CPE has 'a'/application, 'o'/OS, 'h'/hardware |
| `vendor`     | namespace                    | Always domain-qualified                       |
| `product`    | name                         | Software project, product, or component name  |
| `version`    | version                      | Version string                                |
| `update`     | (not directly mapped)        | Could be embedded in `version` or ignored     |
| `edition`    | qualifier-key: 'edition'     | Directly mapped                               |
| `language`   | qualifier-key: 'locale'      | Supports ISO 639-1 and BCP 47                 |
| `sw_edition` | qualifier-key: 'edition'     | May be combined under `edition`               |
| `target_sw`  | qualifier-key: 'target'      | Target environment (e.g., 'java', 'windows')  |
| `target_hw`  | qualifier-key: 'arch'        | CPU architecture (e.g., 'x86_64', 'arm64')    |

'software-id' PURLs maps tpCPE parts `a` (application) and `o` (operating
system). Hardware identification (CPE part `h`) is out of scope.

### SWID

While SWID historically been used in asset and inventory contexts to identify
installed software, it is:

- overly complex for general use,
- tightly coupled to specific enterprise and government implementations, and
- requires fields such as `tagId` that are not always meaningful or available
  in modern DevOps and security pipelines.

SWID used to have tagvault, which would have provided a global registry for
commercial and non-packaged software, but the company behind it folded.
