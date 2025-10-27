<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: psgallery

- **Type Name:** PowerShell Gallery
- **Description:** PowerShell Gallery packages
- **Schema ID:** `https://packageurl.org/types/powershell-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:psgallery/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://www.powershellgallery.com

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Native Label:** version
- **Note:** `The `name` is not case sensitive and must be lowercased.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The `version` is not case sensitive and must be lowercased.`

## Examples

- `pkg:psgallery/pswindowsupdate@2.2.1.5`
- `pkg:psgallery/powershellget@3.0.22-beta22`
- `pkg:psgallery/aws.tools.cloudwatch@4.1.820`

## Note

There is no namespace per se even if the common convention is to use dot-separated package names where the first segment is namespace-like.
