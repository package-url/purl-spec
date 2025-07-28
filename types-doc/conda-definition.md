<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: conda

- **Type Name:** Conda
- **Description:** conda is for Conda packages
- **Schema ID:** `https://packageurl.org/types/conda-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:conda/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://repo.anaconda.com

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namspace`

## Name definition

- **Native Label:** name
- **Note:** `The name is the package name.`

## Version definition

- **Native Label:** version
- **Note:** `The version is the package version.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| build | Optional |  |  | the build string. |
| channel | Optional |  |  | the package stored location. |
| subdir | Optional |  |  | the associated platform. |
| type | Optional |  |  | package type. |

## Examples

- `pkg:conda/absl-py@0.4.1?build=py36h06a4308_0&channel=main&subdir=linux-64&type=tar.bz2`
