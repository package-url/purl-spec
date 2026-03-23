## Proposal: Add new PURL type `sid` (**S**oftware **ID**entification)

### Background

The current list of PURL types covers a wide range of package ecosystems. 
However, there remains a significant gap in the ability to identify 
**non-ecosystem** software components, particularly **commercial**, 
**proprietary**, and **standalone open source** software that is not 
distributed through a package manager or authoritatively available on a 
repository with a supported PURL type, such as GitHub.

### Proposal

Introduce a new PURL type: `sid`, an acronym for **Software IDentification**, 
pronounced /sɪd/.

This PURL type is intended to cover:
- **Standalone open source projects** (e.g., the Linux Kernel)
- **Commercial and proprietary software** (e.g., Acme Database Server)
- **Internally developed applications** that do not belong to a recognized 
package ecosystem
- **Binary-only or installable software** where no manifest-based or 
registry-driven packaging exists

```
pkg:sid/<domain>/<authority>/<component>@<version>?arch=<arch>&edition=<edition>&target=<target>&locale=<locale>
```

### Field Breakdown

| Field       | PURL Component | Requirement | Description                                                                 |
|-------------|----------------|----------|-----------------------------------------------------------------------------|
| `authority`    | namespace       | Required     | The first segment of the namespace serves as the authority. When the segment contains a dot, it is treated as a domain-qualified namespace representing the internet domain of the publishing entity. Domain-qualified namespaces are self-asserted and do not require registration in the PURL registry. <br> When the first segment does not contain a dot, it is a registry-based namespace that must be registered in the PURL registry. A registry-based namespace that is not registered in the PURL registry is invalid. <br> Additional namespace segments beyond the domain may represent the human readable name of the publisher, organizational structure such as business units, product lines, or divisions, or both. |
| `component`   | name            | Required     | Name of the software component. |
| `version`   | version         | Optional | Version string identifying the specific release, tag, or snapshot of the product.  |
| `arch`      | qualifiers       | Optional | CPU architecture the software was built for (e.g., `x86_64`, `arm64`).  |
| `edition`   | qualifiers       | Optional | Specific edition of the product (e.g., `community`, `enterprise`).  |
| `target`    | qualifiers      | Optional | Target software environment (e.g., `windows`, `java`, `android`). |
| `locale`    | qualifiers       | Optional | Language of the software, expressed as an ISO 639-1 code (e.g., `en`) or a full BCP 47 language tag (e.g., `en-GB`). |
|  | subpath | Optional | The subpath optionally identifies a specific module, subcomponent, or file within the broader software product. |

### The Namespace

The namespace for the **sid** PURL type requires an authority as the first 
segment. Additional segments are optional and may represent any organizational 
hierarchy such as the publisher name, business units, product lines, or 
divisions.

---

#### 1. Authority as the Namespace Anchor

The first segment of the namespace serves as the primary anchor for identity 
and discovery. It takes one of two forms.

A domain-qualified namespace contains a dot in the first segment, indicating 
an internet domain name. The domain identifies the entity asserting the 
software's metadata and enables decentralized verification through mechanisms 
such as .well-known/ files or TEA Discovery. While domain names are leased 
rather than owned, and may change hands over time, they provide a resolvable, 
globally unique starting point that no other field can offer. Domain-qualified 
namespaces are self-asserted and do not require registration in the PURL 
registry.

A registry-based namespace does not contain a dot in the first segment. It 
must be registered in the PURL registry, which serves as the authoritative 
source of truth for that namespace. A registry-based namespace that is not 
registered is invalid. This path is intended for projects that do not control 
a domain or prefer centralized registration, such as long-standing open source
 projects maintained by individuals or informal groups.

---

#### 2. Publisher as Optional Context

The optional publisher segment provides a human recognizable name for the 
entity that made the software available for use. Including a publisher is 
recommended when disambiguation is needed, for example when a single domain 
distributes software on behalf of multiple organizations. However, many 
publishers operate under a single identity tied directly to their domain, 
making a separate publisher segment redundant in those cases.

---

#### 3. Flexible Namespace Segments

The namespace supports multiple slash separated segments beyond the domain and
 optional publisher. These additional segments allow organizations to 
 represent internal structure such as business units, product lines, or 
 divisions. The specification does not prescribe the meaning of these 
 segments. Their use and interpretation are determined by the publishing 
 entity. For example:

```
pkg:sid/acme.com/AcmeApplication@1.0.0
pkg:sid/acme.com/Acme%20Robotics/robot-os@2.3.0 pkg:sid/acme.com/Acme%20Robotics/Industrial/motion-controller@4.1.0 pkg:sid/distributor.com/AcmeCorp/appsuite@1.0.0
```

---

#### 4. Disambiguation Through Domain

For domain-qualified namespaces, organizations with identical or similar names
 are disambiguated by their domain. For example:

```
pkg:sid/acme-industries.com/analytics-suite@5.2.1
pkg:sid/acmerobotics.org/robot-os@2.3.0
pkg:sid/foo/bar@4.2.1
```

Both organizations may call themselves "Acme," but the domain provides clear 
differentiation without relying on a publisher segment.
For registry-based namespaces, the PURL registry enforces uniqueness. Each 
registered namespace is distinct, and conflicts are resolved through the 
registration process.

---

### Interoperable Successor to CPE

One of the design goals of this PURL type is to enable interoperability 
with existing systems that utilize legacy identifiers such as CPE. While CPE 
provides a structured method of identifying software, it suffers from 
centralization, a rigid schema, and a heavy reliance on manual human curation.
 These characteristics make it difficult to scale in modern, dynamic 
 environments where new software products, forks, and distributions emerge 
 continuously. In contrast, the PURL format is inherently decentralized and 
 URI-friendly, enabling toolchains, vendors, and open source communities to 
 generate identifiers independently without requiring central registry 
 approval. Despite this shift, `sid` PURLs aim to retain semantic 
 compatibility with CPE by using comparable fields and qualifiers, ensuring 
 they can be adopted by inventory, vulnerability, and compliance systems that 
 currently rely on CPE naming conventions.

| CPE Field     | `sid` PURL Equivalent        | Notes                                                                 |
|---------------|-------------------------------|-----------------------------------------------------------------------|
| `part`        | (implicit in PURL context)     | CPE uses `a` (application), `o` (OS), `h` (hardware); `scid` PURL assumes software |
| `vendor`      | `authority    `                      | Domain of the publishing entity. For registry-based namespaces, the registered namespace serves as the authority. The optional publisher segment provides the human readable name.                   |
| `product`     | `component`                     | Software project, product, or component name                                         |
| `version`     | `version`                     | Version string                                                       |
| `update`      | (not directly mapped)          | Could be embedded in `version` or excluded for simplicity            |
| `edition`     | `edition` (qualifier)         | Directly mapped                                                      |
| `language`    | `locale` (qualifier)          | `locale` supports ISO 639-1 and BCP 47                               |
| `sw_edition`  | `edition` (qualifier)         | May be combined under `edition` in PURL                             |
| `target_sw`   | `target` (qualifier)          | Target software environment (e.g., `java`, `windows`)               |
| `target_hw`   | `arch` (qualifier)            | CPU architecture (e.g., `x86_64`, `arm64`)                           |
| `other`       | (not mapped)                  | Use additional PURL qualifiers           |

`sid` PURLs align with CPE parts `a` (application) and `o` (operating 
system). Hardware identification (CPE part `h`) is out of scope. Established 
standards such as GS1 GMN and GTIN already serve that purpose.

**NB**: This document replaces the core content of: https://github.com/package-url/purl-spec/issues/516.
See the new Discussion item [Design for PURL type for software without a registry](https://github.com/package-url/purl-spec/discussions/841) for a recap of the commentary on issue 
516 organized by topic. You can comment on each topic there using the "threaded"
comments feature of Discussions.