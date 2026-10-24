<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: smartsetup

- **Type Name:** TMS Smart Setup
- **Description:** Projects and packages managed by TMS Smart Setup for the Delphi/RAD Studio ecosystem
- **Schema ID:** `https://packageurl.org/types/smartsetup-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:smartsetup/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://www.smartsetup.org/
- **Note:** Smart Setup resolves products from configurable servers. The default repository, https://www.smartsetup.org/, is the central Smart Setup registry that routes to the underlying sub-registries — the public open-source registry and vendor-operated servers, such as those published by TMS. Product ids are unique across servers; the repository_url qualifier identifies a specific non-default server or source repository.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `There is no namespace. The vendor or owner identifier is part of the native dotted Smart Setup product id.`

## Name definition

- **Requirement:** Required
- **Native Label:** product id
- **Note:** `The name is the full native Smart Setup product id, a dotted identifier such as 'tms.biz.aurelius' or 'sglienke.spring4d'. It must be lowercased.`

## Version definition

- **Requirement:** Optional
- **Normalization rules:**
  - Use the version string exactly as published by the Smart Setup server for the product; do not pad or truncate version segments.
- **Native Label:** version
- **Note:** `The version is the native version identifier understood by Smart Setup for the product, such as a server-published product version. The native version identifier is preserved rather than imposing an additional versioning scheme.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional |  |  | A non-default Smart Setup package server or source repository from which the product is obtained, when it is not the default community registry. |

## Examples

- `pkg:smartsetup/tms.biz.aurelius@5.26`
- `pkg:smartsetup/tms.webcore@2.9.9.3`
- `pkg:smartsetup/sglienke.spring4d`
- `pkg:smartsetup/tms.biz.bcl`

## Reference URLs

- `https://doc.tmssoftware.com/smartsetup/`
- `https://github.com/tmssoftware/smartsetup`
- `https://github.com/tmssoftware/smartsetup-registry`
