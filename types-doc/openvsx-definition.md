<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: openvsx

- **Type Name:** OpenVSX
- **Description:** OpenVSX registry for VS Code extensions
- **Schema ID:** `https://packageurl.org/types/openvsx-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:openvsx/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** No
- **Note:** OpenVSX packages are only available from the official OpenVSX registry at https://open-vsx.org

## Namespace definition

- **Requirement:** Required
- **Native Label:** publisher
- **Note:** `The namespace is the publisher or vendor of the extension (e.g., 'redhat', 'microsoft')`

## Name definition

- **Requirement:** Required
- **Native Label:** extension
- **Note:** `The name is the extension identifier`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The semantic version of the extension`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| platform | Optional | targetPlatform | universal | The target platform for the extension. Common values include 'universal', 'linux-x64', 'linux-arm64', 'darwin-x64', 'darwin-arm64', 'win32-x64', 'win32-arm64', etc. |

## Examples

- `pkg:openvsx/redhat/java@1.46.2025091308`
- `pkg:openvsx/redhat/java@1.46.2025091308?platform=linux-x64`
- `pkg:openvsx/my-python/python@2024.10.0?platform=darwin-arm64`
- `pkg:openvsx/golang/go@0.39.1?platform=win32-x64`

## Reference URLs

- `https://open-vsx.org/`
- `https://github.com/eclipse/openvsx`
- `https://code.visualstudio.com/api/working-with-extensions/publishing-extension#platformspecific-extensions`
