<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: vsx

- **Type Name:** VS Code Extension packages
- **Description:** VS Code Extension packages
- **Schema ID:** `https://packageurl.org/types/vsx-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:vsx/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://marketplace.visualstudio.com/vscode

## Namespace definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Native Label:** publisher

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** name

## Version definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Native Label:** version

## Examples

- `pkg:vsix/ms-python/python@2023.25.10292213`
- `pkg:vsix/muhammad-sammy/csharp@2.15.30?repository_url=open-vsx.org`
