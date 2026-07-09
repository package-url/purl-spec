<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: getit

- **Type Name:** GetIt
- **Description:** Embarcadero GetIt Package Manager (Delphi & C++Builder)
- **Schema ID:** `https://packageurl.org/types/getit-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:getit/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://getitnow.embarcadero.com/
- **Note:** The repository itself is hosted on version specific REST servers, accessible via RAD Studio IDE or the CLI tool GetItCmd.exe.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `GetIt packages do not use a namespace.`

## Name definition

- **Case Sensitive:** Yes
- **Native Label:** Id
- **Note:** `The name corresponds to the unique identifier (Id) of the GetIt package.`

## Version definition

- **Native Label:** version
- **Note:** `The version of the GetIt package as defined in the GetIt catalog.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| platform | Optional |  |  | Target platforms supported by the package (e.g., win32, win64, macos, linux, ios, android, none). Comma-separated if multiple. |
| category | Optional |  |  | GetIt catalog category or categories (e.g., libraries, components, tools, ide-plugins, trial, promoted). Comma-separated if multiple. |

## Examples

- `pkg:getit/Abbrevia-12-64bit@2025.03`
- `pkg:getit/Abbrevia-12-64bit@2025.03?platform=x86,x64&category=components`
- `pkg:getit/GroqCloudAPIwrapper@1.0`
- `pkg:getit/AWSSDKforDelphi-12-1.4.0@1.4.0?platform=x86,x64&category=libraries,promoted`
