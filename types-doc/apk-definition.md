<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: apk

- **Type Name:** APK-based packages
- **Description:** Alpine Linux APK-based packages
- **Schema ID:** `https://packageurl.org/types/bitbucket-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:apk/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository; this should be implied either from the distro qualifiers key  or using a repository base url as repository_url qualifiers key.

## Namespace definition

- **Requirement:** Required
- **Native Label:** vendor
- **Note:** `The namespace is the vendor such as alpine or openwrt. It is not case sensitive and must be lowercased.`

## Name definition

- **Native Label:** name
- **Note:** `The name is the package name. It is not case sensitive and must be lowercased.`

## Version definition

- **Native Label:** version
- **Note:** `The version is a package version as expected by apk.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| arch | Optional |  |  | The arch is the qualifiers key for a package architecture. |

## Examples

- `pkg:apk/alpine/curl@7.83.0-r0?arch=x86`
- `pkg:apk/alpine/apk@2.12.9-r3?arch=x86`

## Note

not to be confused with Android packages with a .apk extension.
