<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: bitnami

- **Type Name:** Bitnami
- **Description:** Bitnami-based packages
- **Schema ID:** `https://packageurl.org/types/bitname-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:bitnami/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://downloads.bitnami.com/files/stacksmith

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Native Label:** name
- **Note:** `The name is the component name. It must be lowercased.`

## Version definition

- **Native Label:** full package version, including version and revision
- **Note:** `The version is the full Bitnami package version, including version and revision.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| arch | Optional |  | amd64 | The arch is the qualifiers key for a package architecture. Available values are amd64 (default) and arm64. |
| distro | Optional |  |  | The distro is the qualifiers key for the distribution associated to the package. |

## Examples

- `pkg:bitnami/wordpress?distro=debian-12`
- `pkg:bitnami/wordpress@6.2.0?distro=debian-12`
- `pkg:bitnami/wordpress@6.2.0?arch=arm64&distro=debian-12`
- `pkg:bitnami/wordpress@6.2.0?arch=arm64&distro=photon-4`
