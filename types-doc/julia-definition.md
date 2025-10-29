<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: julia

- **Type Name:** Julia Package
- **Description:** Julia packages
- **Schema ID:** `https://packageurl.org/types/julia-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:julia/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com/JuliaRegistries/General

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** name
- **Note:** `The name is the package name (without a `.jl` suffix). The name is case sensitive.`

## Version definition

- **Native Label:** version
- **Note:** `The version is the package version.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| uuid | Required | uuid |  | The Julia package UUID. |

## Examples

- `pkg:julia/Dates@1.9.0?uuid=ade2ca70-3891-5945-98fb-dc099432e06a`
- `pkg:julia/Dates?uuid=ade2ca70-3891-5945-98fb-dc099432e06a`
- `pkg:julia/RegisterQD@0.3.1?uuid=ac24ea0c-1830-11e9-18d4-81f172323054`
- `pkg:julia/RegisterQD@0.3.1?uuid=ac24ea0c-1830-11e9-18d4-81f172323054&repository_url=https://github.com/HolyLab/HolyLabRegistry`
