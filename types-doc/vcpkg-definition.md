<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: vcpkg

- **Type Name:** Vcpkg C/C++ packages
- **Description:** Vcpkg C/C++ packages
- **Schema ID:** `https://packageurl.org/types/vcpkg-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:vcpkg/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com/microsoft/vcpkg/
- **Note:** The absolute URL of the vcpkg registry where the package is available (optional). If omitted, ``https://github.com/microsoft/vcpkg`` as default registry is assumed. For filesystem registries or [overlay ports](https://learn.microsoft.com/vcpkg/concepts/overlay-ports), the URI will have a `file` URI scheme.

## Namespace definition

- **Requirement:** Prohibited

## Name definition

- **Requirement:** Required
- **Native Label:** package-name
- **Note:** `The vcpkg package name.`

## Version definition

- **Requirement:** Required
- **Native Label:** package-version
- **Note:** `The vcpg package version.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| port_version | Optional | port_version |  | A string specifying the [port file revision](https://learn.microsoft.com/vcpkg/reference/vcpkg-json#port-version). If omitted, the purl refers to port file revision 0. |
| repository_revision | Optional | repository_revision |  | The commit hash of the vcpkg registry, potentially abbreviated. If omitted, the purl refers to the latest revision available. |

## Examples

- `pkg:vcpkg/bzip2@1.0.8?port_version=6`
- `pkg:vcpkg/ffmpeg@5.1.2?repository_url=https://github.com/azure-sdk/vcpkg`
- `pkg:vcpkg/llvm@15.0.7?repository_url=file:///C:/local-registry/vcpkg`
- `pkg:vcpkg/bzip2@1.0.8?port_version=6&repository_revision=41dfc53&os=Linux&os_arch=x64&build_type=Debug&linkage=dynamic`

## Note

Additional qualifiers may be present on the purl that provide additional information about the context in which the package is being used, such as build configuration or platform information. These additional qualifiers must be tolerated during parsing and can be ignored if the parser does not expect them.
