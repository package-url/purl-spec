<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: bsd

- **Type Name:** BSD
- **Description:** BSD Operating System variant packages
- **Schema ID:** `https://packageurl.org/types/bitname-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:bsd/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** The default repository varies among BSD Operating System variants. The default repositories are http://pkg.freebsd.org for FreeBSD, https://cdn.openbsd.org/pub/OpenBSD for OpenBSD, and https://cdn.netbsd.org/pub/NetBSD for NetBSD.

## Namespace definition

- **Requirement:** Required
- **Native Label:** vendor
- **Note:** `The namespace is the "vendor" name such as "freebsd", "openbsd", or "netbsd". It is not case sensitive and must be lowercased.`

## Name definition

- **Native Label:** name
- **Note:** `The name is the component name. It must be lowercased.`

## Version definition

- **Native Label:** version
- **Note:** `The version is the version of the package.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| arch | Optional |  |  | The target architecture for the package. |
| distro | Optional |  |  | The BSD release version or distribution variant. |
| epoch | Optional |  |  | The package epoch number used for version comparison when normal version ordering is insufficient. |

## Examples

- `pkg:bsd/freebsd/emacs@30.1_2?distro=14.3&epoch=3`
- `pkg:bsd/openbsd/php-apache@8.4.8?distro=7.7&arch=amd64`
- `pkg:bsd/netbsd/mysql-server@5.0.24?distro=10.1&arch=arm64`
