<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: vcpkg

- **Type Name:** Vcpkg C/C++ packages
- **Description:** Packages from the vcpkg C/C++ package manager.
- **Schema ID:** `https://packageurl.org/types/vcpkg-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:vcpkg/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com/microsoft/vcpkg/
- **Note:** The absolute URL of the vcpkg registry where the package is available. If omitted, the default registry `https://github.com/microsoft/vcpkg` is assumed. For filesystem registries or [overlay ports](https://learn.microsoft.com/vcpkg/concepts/overlay-ports), the URL uses the `file` scheme.

## Namespace definition

- **Requirement:** Prohibited

## Name definition

- **Requirement:** Required
- **Native Label:** package-name
- **Note:** `The vcpkg package name.`

## Version definition

- **Requirement:** Optional
- **Native Label:** package-version
- **Note:** `The vcpkg package version.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| port_version | Optional | port_version |  | The vcpkg [port-version](https://learn.microsoft.com/vcpkg/reference/vcpkg-json#port-version). If omitted, the purl refers to port-version 0. |
| repository_revision | Optional | repository_revision |  | The full 40-character commit hash of the vcpkg registry baseline. For git registries this is the `baseline` field in `vcpkg-configuration.json`. A baseline fixes the state of the whole registry rather than a single port, and the same port version can be reached from many baselines, so the exact port recipe is pinned by the `vcs_url` git-tree instead. If omitted, the purl refers to the latest revision available. |
| triplet | Optional | triplet |  | The vcpkg [triplet](https://learn.microsoft.com/vcpkg/concepts/triplets) describing the target build configuration (architecture, operating system, and CRT/library linkage), for example `x64-windows` or `arm64-osx`. It describes the build target and does not affect package identity. |

## Examples

- `pkg:vcpkg/bzip2@1.0.8?port_version=6`
- `pkg:vcpkg/zlib@1.3.1?triplet=x64-linux&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Fmicrosoft%2Fvcpkg%40b5d3197b1a8a3f4c2d9e0f1a2b3c4d5e6f708192`
- `pkg:vcpkg/ffmpeg@5.1.2?repository_url=https:%2F%2Fgithub.com%2Fazure-sdk%2Fvcpkg`
- `pkg:vcpkg/zlib@1.3.1?repository_url=https:%2F%2Fgithub.com%2Fazure-sdk%2Fvcpkg&triplet=x64-linux&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Fazure-sdk%2Fvcpkg%40b5d3197b1a8a3f4c2d9e0f1a2b3c4d5e6f708192`
- `pkg:vcpkg/llvm@15.0.7?repository_url=file:%2F%2F%2FC:%2Flocal-registry%2Fvcpkg`
- `pkg:vcpkg/bzip2@1.0.8?port_version=6&repository_revision=84a143e4caf6b70db57f28d04c41df4a85c480fa&triplet=x64-linux`

## Note

A purl may carry extra qualifiers that describe the context in which the package is used, such as build configuration or platform. Parsers must tolerate these and may ignore any they do not expect. The `vcs_url` common qualifier carries the port's version-control URL in pip VCS form, for example `git+https://github.com/microsoft/vcpkg@<git-tree>`. Its git-tree pins the exact port recipe. The `features` qualifier, a comma-separated list of enabled vcpkg feature names, records which optional features were enabled at build time; it is informational and not currently normative.
