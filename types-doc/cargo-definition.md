<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: cargo

- **Type Name:** Cargo
- **Description:** Cargo packages for Rust
- **Schema ID:** `https://packageurl.org/types/cargo-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:cargo/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://crates.io/

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** name
- **Note:** `The name is the repository name.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The version is the package version.`

## Examples

- `pkg:cargo/rand@0.7.2`
- `pkg:cargo/clap@2.33.0`
- `pkg:cargo/structopt@0.3.11`
