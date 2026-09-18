<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: spack

- **Type Name:** spack
- **Description:** spack packages
- **Schema ID:** `https://packageurl.org/types/spack-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:spack/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com/spack/spack-packages
- **Note:** The default repository for spack packages

## Namespace definition

- **Requirement:** Required
- **Note:** `The spack namespace as given by `spack find -N``

## Name definition

- **Requirement:** Required
- **Note:** `The package's name`

## Version definition

- **Requirement:** Optional
- **Note:** `The spack version using the standard version syntax (https://spack.readthedocs.io/en/latest/spec_syntax.html#version-specifier)`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| daghash | Optional |  |  | The spack hash of the installation as given by 'spack find -l' |

## Examples

- `pkg:spack/builtin/zlib@1.3.2`
- `pkg:spack/mynamespace/gmake@4.4.1?daghash=os2kltnpbfyz7yxpdaoxtbzocsp223q3`
