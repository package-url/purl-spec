<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: rpm

- **Type Name:** RPM
- **Description:** RPM packages
- **Schema ID:** `https://packageurl.org/types/rpm-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:rpm/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository, this should be implied either from the distro qualifiers key or using a repository base URL as repository_url qualifiers key.

## Namespace definition

- **Requirement:** Required
- **Native Label:** vendor
- **Note:** `The namespace is the vendor such as Fedora or OpenSUSE. It is not case sensitive and must be lowercased.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** name
- **Note:** `The name is the RPM name and is case sensitive.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version-release
- **Note:** `The version is the combined version and release of an RPM.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| epoch | Optional |  |  | (optional for RPMs) is a qualifier as its not required for unique identification, but when the epoch exists we strongly encourage using it. |
| arch | Optional |  |  | the qualifiers key for a package architecture. |

## Examples

- `pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25`
- `pkg:rpm/centerim@4.22.10-1.el6?arch=i686&epoch=1&distro=fedora-25`
