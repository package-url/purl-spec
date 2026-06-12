<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: ips

- **Type Name:** IPS
- **Description:** Image Packaging System (IPS) packages used in illumos and Solaris distributions.
- **Schema ID:** `https://packageurl.org/types/ips-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:ips/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository. The publisher in the namespace or a repository_url qualifier should be used to identify the source of the package.

## Namespace definition

- **Requirement:** Optional
- **Normalization rules:**
  - It is not case sensitive and must be lowercased.
- **Native Label:** publisher
- **Note:** `The namespace is the IPS publisher name.`

## Name definition

- **Requirement:** Required
- **Normalization rules:**
  - It is not case sensitive and must be lowercased.
- **Native Label:** package name
- **Note:** `The name is the IPS package name. If the package name contains slashes, they must be percent-encoded as %2f.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The version is the IPS package version FMRI component.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| arch | Optional |  |  | The CPU architecture of the package. |

## Examples

- `pkg:ips/openindiana.org/system%2flibrary@0.5.11,5.11-2023.0.0.20163:20230504T155427Z`
- `pkg:ips/omnios/runtime%2fperl-532@5.32.1,5.11-151038.0:20210503T104523Z`
- `pkg:ips/library%2fpython%2fnumpy@1.21.2,5.11-151038.0:20210503T104523Z`
