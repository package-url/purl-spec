<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: cocoapods

- **Type Name:** CocoaPods
- **Description:** CocoaPods pods
- **Schema ID:** `https://packageurl.org/types/cocoapods-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:cocoapods/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://cdn.cocoapods.org/

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Case Sensitive:** Yes
- **Native Label:** pod name
- **Note:** `The name is the pod name and is case sensitive, cannot contain whitespace, a plus (+) character, or begin with a period (.).`

## Version definition

- **Native Label:** package version
- **Note:** `The version is the package version.`

## Subpath definition

- **Note:** `The purl subpath is used to represent a pods subspec (if present).`

## Examples

- `pkg:cocoapods/AFNetworking@4.0.1`
- `pkg:cocoapods/MapsIndoors@3.24.0`
- `pkg:cocoapods/ShareKit@2.0#Twitter`
- `pkg:cocoapods/GoogleUtilities@7.5.2#NSData+zlib`
