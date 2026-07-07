<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: spack

- **Type Name:** spack
- **Description:** spack packages
- **Schema ID:** `https://packageurl.org/types/spack-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:spack/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com/spack/spack-packages
- **Note:** The default repository for spack packages

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `spack packages do not use namespaces`

## Name definition

- **Requirement:** Required
- **Note:** `The package's name`

## Version definition

- **Requirement:** Optional
- **Note:** `The spack version using the standard spec syntax`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| sha | Required |  |  | The hash of the installation as given by 'spack find -l' |

## Examples

- `pkg:spack/zlib?sha=u463uoum2lujbc2ug4fpbersp4jev2yl`
- `pkg:spack/gmake@4.4.1?sha=os2kltnpbfyz7yxpdaoxtbzocsp223q3`
