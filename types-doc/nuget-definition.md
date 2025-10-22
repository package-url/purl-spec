<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: nuget

- **Type Name:** NuGet
- **Description:** NuGet .NET packages
- **Schema ID:** `https://packageurl.org/types/nuget-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:nuget/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://www.nuget.org

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** version
- **Note:** `Technically the name is case-perserving, but case-insensitive, and NuGet packages archives are case-perserving, while some NuGet API calls demand to lowercase the package name.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The NuGet version is semver-like but may contain more than three segments`

## Examples

- `pkg:nuget/EnterpriseLibrary.Common@6.0.1304`

## Note

There is no namespace per se even if the common convention is to use dot-separated package names where the first segment is namespace-like.
