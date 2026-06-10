<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: nix

- **Type Name:** Nix
- **Description:** Nix Packages
- **Schema ID:** `https://packageurl.org/types/nix-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:nix/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com/NixOS/nixpkgs

## Namespace definition

- **Requirement:** Required
- **Native Label:** origin
- **Note:** `The namespace is the source origin of the package ecosystem, such as nixpkgs, nixos-hardware, or a custom flake name.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** attribute path
- **Note:** `The exact, case-sensitive attribute path of the package within the target package set.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The upstream version of the nix package.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| commit | Optional | commit_hash |  | The Git commit hash (hexadecimal) identifying the exact revision of the origin repository from which the package is evaluated. |
| system | Optional | system |  | The target system architecture and operating system platform tuple for which the package is built (e.g., x86_64-linux, aarch64-darwin). |
| output | Optional | output |  | The specific multi-output derivation name of the package (e.g., out, dev, lib, bin, man). Defaults to 'out' if omitted. |

## Examples

- `pkg:nix/nixpkgs/haskellPackages._3d-graphics-examples@0.0.0.2`
- `pkg:nix/nixpkgs/imlib2@1.12.6?commit=ea04e1fdd523987348c468e8cb53cc36c575d629`
- `pkg:nix/nixpkgs/imlib2@1.12.6?commit=ea04e1fdd523987348c468e8cb53cc36c575d629&system=x86_64-linux&output=dev`
