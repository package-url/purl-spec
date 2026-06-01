<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: alpm

- **Type Name:** Arch Linux package
- **Description:** Arch Linux packages and other users of the libalpm/pacman package manager.
- **Schema ID:** `https://packageurl.org/types/alpm-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:alpm/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository; this should be implied either from the distro qualifiers key  or using a repository base url as  repository_url qualifiers key.

## Namespace definition

- **Requirement:** Required
- **Normalization rules:**
  - It is not case sensitive and must be lowercased.
- **Native Label:** vendor
- **Note:** `The namespace is the vendor such as arch, arch32, archarm, manjaro or msys.`

## Name definition

- **Requirement:** Required
- **Native Label:** name
- **Note:** `The name is the package name. It is not case sensitive and must be lowercased.`

## Version definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Normalization rules:**
  - normalize version as specified in vercmp(8) at https://man.archlinux.org/man/vercmp.8#DESCRIPTION as part of alpm.
- **Native Label:** version
- **Note:** `The version is the version of the package as specified in vercmp(8) at (https://man.archlinux.org/man/vercmp.8#DESCRIPTION as part of alpm.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| arch | Optional | arch |  | The arch is the qualifiers key for a package architecture. |

## Examples

- `pkg:alpm/arch/pacman@6.0.1-1?arch=x86_64`
- `pkg:alpm/arch/python-pip@21.0-1?arch=any`
- `pkg:alpm/arch/containers-common@1:0.47.4-4?arch=x86_64`
