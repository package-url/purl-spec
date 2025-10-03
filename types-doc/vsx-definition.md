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
- **Note:** `The namespace is the publisher or vendor of the extension (e.g., 'redhat', 'microsoft')`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** name

## Version definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Native Label:** version

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| platform | Optional | targetPlatform | universal | The target platform for the extension. Common values include 'universal', 'linux-x64', 'linux-arm64', 'darwin-x64', 'darwin-arm64', 'win32-x64', 'win32-arm64', etc. |

## Examples

- `pkg:vsx/ms-python/python@2023.25.10292213`
- `pkg:vsx/muhammad-sammy/csharp@2.15.30?repository_url=open-vsx.org`
- `pkg:vsx/golang/go@0.39.1?platform=win32-x64`

## Reference URLs

- `https://open-vsx.org/`
- `https://github.com/eclipse/openvsx`
- `https://code.visualstudio.com/api/working-with-extensions/publishing-extension#platformspecific-extensions`
