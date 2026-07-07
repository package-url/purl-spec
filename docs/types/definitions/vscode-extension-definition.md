<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: vscode-extension

- **Type Name:** VS Code Extension packages
- **Description:** VS Code Extension packages
- **Schema ID:** `https://packageurl.org/types/vscode-extension-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:vscode-extension/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://marketplace.visualstudio.com/vscode-extension

## Namespace definition

- **Requirement:** Required
- **Native Label:** publisher
- **Note:** `The namespace is the publisher or vendor of the extension (e.g., 'redhat', 'microsoft'). This corresponds to the 'Publisher' property of the 'Identity' element in the package's .vsixmanifest file.`

## Name definition

- **Requirement:** Required
- **Native Label:** name
- **Note:** `The extension name. This corresponds to the 'Id' property of the 'Identity' element in the package's .vsixmanifest file.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The extension version. This corresponds to the 'Version' property of the 'Identity' element in the package's .vsixmanifest file.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| platform | Optional | targetPlatform | universal | The target platform for the extension. Common values include 'universal', 'linux-x64', 'linux-arm64', 'darwin-x64', 'darwin-arm64', 'win32-x64', 'win32-arm64', etc. |

## Examples

- `pkg:vscode-extension/ms-python/python@2023.25.10292213`
- `pkg:vscode-extension/muhammad-sammy/csharp@2.15.30?repository_url=https://open-vsx.org`
- `pkg:vscode-extension/golang/go@0.39.1?platform=win32-x64`

## Reference URLs

- `https://open-vsx.org/`
- `https://github.com/eclipse/openvsx`
- `https://code.visualstudio.com/api/working-with-extensions/publishing-extension#platformspecific-extensions`
