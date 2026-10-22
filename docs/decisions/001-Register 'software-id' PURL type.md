from pygments.lexers.configs import ApacheConfLexer
---
status: proposed
date: 2026-10-20
---

# Decision: Add new PURL type 'software-id'

## Context / Problem

The registered PURL `types` cover a wide range of package ecosystems, but it is
difficult to use PURL to identify *non- ecosystem*-based software packages,
particularly C/C++ packages and other standalone open source software that may
not live in an incorporated package registry; and commercial or other software
that is not distributed through a package manager or available with supported
PURL `type`. For these until now, the last resort has been the `generic` PURL
type, fraught with the problems of arbitrary PURL components values making it
hard to create identical PURLs for the same package independently.

One reason for the difficulty is that PURL was originally targetted to open
source ecosystems with (often centralized) package repositories that organize
the naming, identification and location of their packages.

The proposed `software-id` PURL `type` community discussions have converged from
two use cases:

- C/C++ and other standalone open source projects that do not use public package
  repositories or registries, e.g., such as packages not hosted at Maven, not at
  npm, not on GitHub, or not at PyPI. This includes for example the packages of
  the Linux Kernel, the Apache Software Foundation, and a significant set of
  essential software that powers the modern internet.

- Commercial or proprietary software including internal use only software.

For these two cases, there is eventually a much larger number of package naming
authorities than with structured package ecosystems that we track as registered
PURL `types`: there is a finite number of programming languages and backing
ecosystems, but there are possibly millions of standalone projects and
commercial software publishers. A path to accomodate this volume is reusing the
internet domains, without the need to registered millions of new PURL `type`.

Some key similarities between these two use cases are that each publisher
manages internally consistent naming conventions, and version or release
numbering schemes, and ensure uniqueness of these names withing their confines.
Many software publishers also have complex organizational structures for many
products (commercial or proprietary) similarly to larger open source foundations
hosting many projects.

Both use cases demand a decentralized, federated solution to define their own
PURLs consistently for use in their software supply chains without external
dependencies on some centralized naming authority.

## Solution

Introduce a new PURL `type` named `software-id` reusing the internet domains
for decentralized name assignments, federated through simple conventions, and
backed by an optional shared and aggregated registry hosted at `packageurl.org`.

This PURL `type` covers:

- *Standalone open source projects* (e.g., the Linux Kernel)
- *Open source foundations* (e.g., the Apache Software Foundation)
- *Commercial and proprietary software* (e.g., Acme Database Server)
- *Internally developed applications* not in a registered package type

### PURL Components for the `software-id` type

| Component  | Requirement | Description                         |
| -----------|-------------|-------------------------------------|
| type       | Required    | Constant value: `software-id`       |
| namespace  | Required    | First namespace segment is an internet domain. Other segments are optional and defined by that domain's organization. |
| name       | Required    | Package name as defined in spec.    |
| version    | Optional    | Version as defined in spec.         |
| qualifiers | Optional    | Key-value pairs as defined in spec. |
| subpath    | Optional    | Subpath as defined in spec.         |


### Namespace

The key aspect of the `software-id` PURL `type` is that:

 - The `namespace` component is required
 - The first segment of the `namespace` component is required and must be
   and internet domain aka. the **authority**. 

This domain/authority is responsible for the definition of futher namespace
segments, the name and version conventions and uniqueness in that domain, the
same way ecosystem package registries or repositories like pypi, maven or npm
are responsible for naming rules and uniqueness.

This domain also serves as the optional registry of its PURLs namespaces, names
and versions. The other namespace segments are optional, domain-defined, and may
represent any element of an organizational hierarchy such as a project, sub-
project, publisher name, business units, or product lines.

The `packageurl.org` is the special domain to register PURLs that do not a have
domain, and also serves as an aggregator for `software-id` PURLs.

For instance, the `packageurl.org` domain requires extra namespace segments as
in the "foo" example below:

    `pkg:software-id/packageurl.org/foo/bar@123`


#### Domain name anchoring and PURL resolution

Since the `namespace` `software-id` first segment is a domain name, it becomes
possible to discover software package PURLs at that domain:

- With a `.well-known/` [URI](https://en.wikipedia.org/wiki/Well-known_URI)
  at `purl.json` contaning the extra data about this domain hosted PURL
  namespaces, names or versions.

- With the shared `packageurl.org` domain serving a `.well-known/purl.json` with
  pre-registered PURL namespaces, names or versions. `packageurl.org` serves as
  a shared registry as a convenience, and as an aggregator for other domains to
  make discovery easier. This registry is intended for projects or organizations
  that do not control a domain or prefer centralized registration.

#### Disambiguation through domain

Since a `software-id` PURL namespace is always qualified by a domain, different
organizations that release software with similar names are releasing unique
PURLs, never ambiguous. For example, these different PURLs have the same name:

```
pkg:software-id/acme-industries.com/foo/analytics-suite@5.2.1
pkg:software-id/acmerobotics.org/foo/analytics-suite@5.2.1
```

Each domain acts as a PURL registry that enforces uniqueness. The shared
`packageurl.org` centralized registry enforces uniqueness at the registration
process, where each registration is a unique set of files and directory.

#### Flexible namespacing

The PURL `namespace` component supports multiple extra slash-separate segments (with
no specific limit) so that the **authority** for a 'software-id' PURL domain
can document as deep naming hierarchies as needed. This can be user to represent a project or team, 
or a business unit, multiple product lines, divisions, etc.

The PURL `type` definition for `software_id` does not prescribe the meaning of
these segments. These are determined (and optionally documented) at the domain
level instead, by the publisher. For example:

```
pkg:software-id/kernel.org/linux@6.18.57
pkg:software-id/apache.org/logging/log4j-core@2.21.0
pkg:software-id/acme.com/AcmeApplication@1.0.0
pkg:software-id/acme.com/AcmeRobotics/robot-os@2.3.0
pkg:software-id/acme.com/AcmeRobotics/Industrial/motion-controller@4.1.0
```

### Name, Version, Qualifiers and Subpath

The other PURL components are not special for this PURL type.

Some `qualifier` keys that will likely be useful for a 'software-id' PURL include:

- 'arch': CPU architecture the software was built for (e.g., 'x86_64', 'arm64').
- 'edition': The specific edition of a commercial product (e.g., 'community' or 'enterprise').
- 'locale': Language of the software asan ISO 639-1 code (e.g., 'en') or a full BCP 47 language tag (e.g., 'en-GB').
- 'target': Target software environment (e.g., 'windows', 'java', 'android').

This use of `qualifiers` is common across PURL `types` but highlighted here
because some `software-id` PURLs may to use multiple `qualifiers` like with
commercial software.

## Decision Drivers

Some of the additional decision drivers beyond the [Context / Problem](#context--problem) section were:

- A PURL should be obvious, by observing the software.  We do not have a
  manifest or convention yet to make `software-id` self-documenting and obvious,
  but at least the `software-id` PURL type reduces the search for a proper PURL
  to the domain name or to the shared registry or both. 

- A preference for one solution to cover both commercial or proprietary
  products and open source projects if possible. The reasons for this
  preference are simplicity and the difficulty in some cases of
  distinguishing between commercial or proprietary and open source software.

## Non-goals

These use cases are not suitable for 'software-id':

- Services: Not in scope. There is a separate discussion for a new service 'PURL
  `type` like for online APIs. There may be some similarities between
  'software-id' domain-based `namespace` and that of a `service` PURL type.

- Hardware: Not in scope. The 'software-id' and PURL in general is find to
  identify embedded software in devices.

## Alternatives Considered

### Use 'generic' PURL `type`

The 'generic' PURL type is the current way to create a PURL for software without
a registered PURL. Using the 'generic' `type` requires `qualifiers` for a
download URL, and it is too easy to create different PURLs for the same generic
package. 'generic' will remain as a last resort for use cases not covered by the
'software-id' or other registered PURL `types`.

### Separate PURL `types` for proprietary and open source software

There were several discussions about defining separate PURL `types` for
commercial or proprietary software and for open source software. The main points
of distinction were related to the perception that commercial publishers would
want to define complex/richer/structured `namespace` segments and multiple
standardized `qualifiers` and that these that would not apply well to open
source projects. One example idea was requiring a publisher segment
in the `namespace` after the domain. The community conclusions were that:

- Defining standard rules for`namespace` or `qualifiers` for all commercial or
  proprietary software was unrealistic, and

- Offering flexibility for each publisher (e.g., the **authority** or domain in
  the `software-id` type) to define its own `namespace` segments and
  `qualifiers` was more practical.


## Decision Outcome

This new PURL `type` has been under active discussion since early 2025.
This decision is pending final approval by TC54/TG2.

### 'software-id' `type` name

Two proposed PURL `type` names for this new PURL `type` were 'sid' as an acronym
for "Software ID" and 'scid' for "Software Component IDentification". The
community agreed to use the PURL `type` name 'software-id' to make the `type`
name obvious and clear without creating a new acronym. There is some potential
for confusion with "SWID tags" which are already registered as the 'swid' PURL
`type`, and using the longer 'software-id' descriptive name should be less
confusing than acronyms like 'sid' or 'scid'.


### Requiring using a TEA Server for verification

Some community members proposed to make the new Transparency Exchange API spec
mandatory for verifying a domain in the 'software-id' `namespace` and for
further retrieving software information from a TEA Server. TEA has been approved
by Ecma TC54 for submission to the Ecma General Assembly in December 2026. The
community agreed that requiring the use of TEA/Server was too demanding as it
implies to deploy extra infrastructure, although it could be recommended as an
option. 

### PURL discovery

The PURL approach to discovering `software-id` types is using static files
located at `.well-known/` location of the domain used as the first segment of
that PURL.

(Technically these files can be dynamically generated as an option.)



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

There also an "omnibus" discussion thread that summarizes the commentary from
the issues by topic and contains additional commentary:
[Design for new PURL type: 'software-id'](https://github.com/package-url/purl-spec/discussions/841)


### Interoperable Successor to CPE

One of the design goals of this PURL `type` will be to enable interoperability
with existing systems that utilize legacy identifiers such as CPE. While CPE
provides a rich and structured method of identifying software, it suffers from
centralization, a rigid schema, and reliance on manual human curation to assign
aribitrary names. These characteristics make it difficult to scale in modern,
dynamic environments where new software projects, forks, and distributions
emerge continuously. 

In contrast, the PURL format is inherently decentralized and URI-friendly,
enabling toolchains, vendors, and open source communities to generate
identifiers independently without requiring central registry approval. Despite
this shift, 'software-id' PURLs aim to retain high level semantic compatibility
with CPE by using similar fields and qualifiers, ensuring they can be adopted
more easily by the ecosystem that currently rely on CPE names.

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
