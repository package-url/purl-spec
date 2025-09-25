<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: bsd

- **Type Name:** BSD
- **Description:** BSD Operating System variant packages, primarily focused on FreeBSD with extensibility for other BSD variants such as OpenBSD, DragonFly BSD. Note: since NetBSD's package manager is designed for cross-platform use, it should use its own dedicated PURL type.
- **Schema ID:** `https://packageurl.org/types/bsd-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:bsd/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** The default repository is http://pkg.freebsd.org for FreeBSD. Other BSD variants may use different repositories as appropriate.

## Namespace definition

- **Requirement:** Required
- **Native Label:** vendor
- **Note:** `The namespace is the BSD variant name such as "freebsd", "openbsd", or "dragonflybsd". It is not case sensitive and must be lowercased.`

## Name definition

- **Case Sensitive:** Yes
- **Native Label:** name
- **Note:** `The name is the package name and is case sensitive.`

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
- `pkg:bsd/freebsd/python311@3.11.13?distro=14.3`
