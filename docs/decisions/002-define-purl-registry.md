---
status: proposed
date: 2026-11-20
---

# Define PURL registry

## Terminology

We use the following specific terminology in this document:
- "consumer" means means an organization or person who consumes software
  using PURLs to identify software packages.
- "package" means any software artefact. A common synonym is component.
- "publisher" means an organization, community or person who publishes or
  distributes software.

## Context / Problem

One of the biggest challenges for universal PURL adoption is to define
PURLs for software packages that do not reside in a structured ecosystem
defined by a public package manager or package repository (aka registry) that
can provide unique identifiers and metadata for all of its packages.

This challenge applies in particular to two large software domains:
- C/C++ and other standalone open source projects, such as the Linux Kernel,
  some packages of the Apache Software Foundation, and a significant set of
  essential software that powers the modern internet.
- Commercial or proprietary software including internal use only software.

The Package-URL community is creating a new 'software-id' PURL `type` as the
primary structure to address this challenge. It is documented in the
`purl-spec` decision document: [001-add-software-id-PURL-type](
https://github.com/package-url/purl-spec/blob/main/docs/decisions/001-add-software-id-PURL-type.md).
The decision document includes links to key background discussions and issues
for the 'software-id' PURL `type`.

The key unique feature of the 'software-id' PURL `type` is the definition
of the `namespace` PURL component. This `namespace` definition has two key
elements:
- *Disambiguation through domain*: For 'software-id' PURLs the first segment
  of the `namespace` component is always an internet domain. Different
  software publishers will be able to provide unique PURLs for their software
  packages using their domain.
- *Flexible namespace segments*: The PURL `namespace` component supports
   multiple slash-separated segments (with no specific limit) so that a
   software publisher who owns a domain used for 'software-id' PURLs can
   document deep software naming hierarchies as needed.

Implementation of the 'software-id' PURL `type` requires some way to provide
the missing infrastructure for software consumers to discover and validate
PURLs that a package manager system provides for its software. The proposed
solution is to define the structure of a PURL registry that can be hosted by
any software publisher.

## Solution

A PURL registry is a registry of software package PURLs that is maintained by
a publisher using an internet domain as the first `namespace` segment for
their 'software-id' `type` PURLs. The purpose is to support the use of the
'software-id' PURL `type` by providing a way for software publishers to
advertise their use of 'software-id' PURLs and provide software consumers with
their PURL data.

The key high level requirements for PURL registries are:
- A federated approach to support an unlimited number of registries.
- A simple process for a publisher to "advertise" (register) their use of
  'software-id' PURLs and provide PURL data at their domain.
- A `/.well-known/purl.json` URI contains the definitions and references for
  the PURLs defined at the corresponding domain.
- All data is keyed by PURL.
- Neutrality towards any build or CI/CD system.
- An alternate solution for a software publisher that does not have control of
  a domain for their own PURL registry.

The proposed PURL registry solution has three levels:
- PURL registry
- PURL directory for publishers to advertise their use of PURLs
- Package-URL hosted PURL registry for publishers who do not have a domain

### PURL registry

The key functions of a PURL registry are to:
- Define the structure for one or more 'software-id' PURL subtypes for a
  domain.
- Provide a list of valid PURLs for the domain.

The reason for these requirements is to enable the public to verify the
validity of a 'software-id' PURL from a publisher. This is essential
information for software identification using PURL.

A PURL registry may be public or private - e.g., access to the endpoint may
require authentication. Some publishers may restrict access to their PURL
data to customers or require some form of registration to access the data.

Software publishers are encouraged, but not required, to provide package
metadata or download information (or both) for their PURLs. Larger
organizations (commercial or open source) will likely implement their own
internal mechanisms to make package metadata or downloads available to
consumers.

A PURL registry is based on the use of a `/.well-known/purl.json` [URI](https://en.wikipedia.org/wiki/Well-known_URI)
endpoint at the domain used for the first `namespace` segment of the
'software-id' PURLs maintained by the publisher at that domain. The endpoint
provides consumers with:
  - A definition of any 'software-id' subtypes for PURLs maintained at that
    domain.
  - A list of valid PURLs.

### `/.well-known/purl.json` endpoint

The `purl.json`file contains:
- One or more definitions for 'software-id' subtypes. A 'software-id' subtype
  is an extension of the 'software-id' PURL `type` definition where:
    - the base PURL `type` is always 'software-id'
    - the first segment of the PURL `namespace` is always the publisher's
      domain or subdomain
    - the publisher may define the structure of additional `namespace`
      segments at the domain or subdomain level
    - the publisher may define the structure of other PURL components for the
      subtype: `name`, `version`, `qualifiers`, and `subpath`
- A list of URL(s) documenting one or more lists of valid PURLs for the domain
  or a subdomain where:
  - Each list is a JSON array of PURLs
  - Each PURL in a list shall be valid, but does not necessarily include data
    for all components

  The reason for a list of URLs instead of a list of PURL values in the
  `purl.json` file itself is to support publishers with large PURL catalogs,
  possibly with many hundred or thousand PURLs, This approach is similar to
  pagination. There is no limit on the list length.

  A publisher may also use their `purl.json` file to advertise any `type` of
  PURL for their software - e.g., PURLs for packages covered by a package
  manager to make it easier for consumers to discover their software.

The `purl.json` file will be specified according to [JSON Schema version 2020-12](https://json-schema.org/draft/2020-12/json-schema-core).

#### Example

The following example illustrates key elements of the planned schema for a
`purl.json` file.

```
[
 {
    "package_type": "software-id",
    "software_id_domain": "acme.com",
    "software_id_definition": "https://www.acme.com/foo/bar/acme.com-purl-software-id.json",
    "purls" : [
      "https://www.acme.com/foo/bar/all-acme-software-id-purls.json"
    ]
  },
  {
    "package_type": "software-id",
    "software_id_domain": "apps.acme.com",
    "software_id_definition": "https://www.apps.acme.com/foo/bar/acme.com-purl-software-id.json",
    "purls" : [
      "https://www.apps.acme.com/foo/bar/all-apps-purls.json"
    ]
 },
   {
    "package_type": "software-id",
    "purls" : [
      "https://www.acme.com/foo/bar/list-of-software-id-purls-part1.json",
      "https://www.acme.com/foo/bar/list-of-software-id-part2.json",
      ...
      "https://www.acme.com/foo/bar/list-of-software-id-purls-part1000.json"
    ]
  }
  {
    "package_type": "npm",
    "purls" : [
      "https://www.acme.com/foo/bar/list-of-npm-purls-part1.json",
      "https://www.acme.com/foo/bar/list-of-npm-purls-part2.json",
      ...
      "https://www.acme.com/foo/bar/list-of-npm-purls-part100.json"
    ]
  }
]
```

### PURL directory

The PURL directory is a central directory where a publisher can register to
document their use of 'software-id' PURLs at their domain.  The directory is
maintained by the Package-URL community.

The directory will be implemented as dedicated Git repository with:
- Simple YAML or similar files to document:
  - the domain registered for a 'software-id' `namespace`
  - description
  - homepage URL
  - contact information
- There will be a simple issue and PR process to submit, approve or update
  a registration with basic verification that a requestor is authorized to
  register a `namespace` domain by the domain owner.

Registration is optional but strongly encouraged to avoid conflicts and to
enable software consumers to quickly identify active PURL registries.

### Package-URL hosted PURL registry

The Package-URL community will host a shared PURL registry providing a free
central registry for open source projects or other organizations that want to
standardize their PURLs without using their own domain because they do not own
a domain, or because they have one and prefer not to use it for this purpose.

PURLs from the Package-URL hosted registry will all start with
`pkg:software-id/packageurl.org/` where 'software-id' is the PURL `type` and
'packageurl.org' is the first `namespace` segment. The Package-URL community
will define:
- A Git-based process for registering each software publisher who wants to use
  the Package-URL hosted registry.
- A PURL subtype definition for:
  - identifying each unique publisher within the `namespace` component, and
  - optionally defining rules for the other PURL component data for a
    publisher.
- The data structure for the information will be stored at and served from the
  `www.packageurl.org/.well-known/purl.json` URI.

Other organizations have the option to establish a PURL registry to host
multiple software publishers at their domain. The structure of the Package-URL
hosted PURL registry should be useful as a template for use by other PURL
registries.

## Out of scope
- Support for extending the PURL registry to other PURL `types`.
- Definition of software package metadata - the "missing manifest".
- Mirrored snapshots of `./well-known/purl.json` data from public PURL
  registries.

## Alternative considered

## Decision outcome

## Open questions

1. Is there a better name for "PURL directory"?
  - Catalog?

2. Is there a requirement that a PURL registry domain must be only a top-level
   domain? Referencing back to the example above could there be separate
   PURL registries for `acme.com` and `apps.acme.com`?

3. Should we support multiple top-level domains within a `purl.json` file?
    - Defining multiple top-level domains within a top-level domain will
      likely be confusing to software consumers, but this may be necessary to
      support the use case where the organization or person who owns the
      registry domain changes.

4. How would a publisher use a TEA server with the `purl.json` endpoint?

5. How would the PURL registry support other future PURL `types`?

6. What infrastructure do we need to provide scalability and security for
   public access to packageurl.org`. This may require Cloudflare or another
   CDN.

## More information

### ASF example

An example of a 'software-id' PURL for Apache Software Foundation projects is:
`pkg:software-id/apache.org/<asf-namespace>/<name>@<version>`

Where:
- The `namespace` domain is fixed to `'apache.org'.
- <asf-namespace> is an ASF-internal segment (most likely the PMC/TLP, e.g.
  logging, commons) which we can finalize within the ASF.
- <name> and <version> follow the usual PURL semantics.

The two primary two software consumer-facing use cases are:
- looking up the correct PURL for a file shown on an ASF download page, and
- including that PURL in an SBOM so it can be matched against vulnerability
  data.

