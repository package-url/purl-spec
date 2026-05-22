<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: hex

- **Type Name:** Hex
- **Description:** Hex packages
- **Schema ID:** `https://packageurl.org/types/hex-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:hex/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://repo.hex.pm

## Namespace definition

- **Requirement:** Optional
- **Native Label:** organization for private packages
- **Note:** `The namespace is optional; it may be used to specify the organization for private packages on hex.pm. It is not case sensitive and must be lowercased.`

## Name definition

- **Requirement:** Required
- **Native Label:** name
- **Note:** `The name is not case sensitive and must be lowercased.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version

## Examples

- `pkg:hex/jason@1.1.2`
- `pkg:hex/acme/foo@2.3.`
- `pkg:hex/phoenix_html@2.13.3#priv/static/phoenix_html.js`
- `pkg:hex/bar@1.2.3?repository_url=https://myrepo.example.com`
