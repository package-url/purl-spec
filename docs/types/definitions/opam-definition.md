<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: opam

- **Type Name:** Opam package
- **Description:** Opam packages
- **Schema ID:** `https://packageurl.org/types/opam-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:opam/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://opam.ocaml.org

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** name
- **Note:** `The name is case sensitive.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The version is package version.`

## Examples

- `pkg:opam/ocaml-base-compiler@5.2.0`
- `pkg:opam/git@3/16.1`
