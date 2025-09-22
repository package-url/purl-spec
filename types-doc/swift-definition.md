<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: swift

- **Type Name:** Swift packages
- **Description:** Swift packages
- **Schema ID:** `https://packageurl.org/types/swift-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:swift/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository, this should be implied from namespace.

## Namespace definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Note:** `The namespace is source host and user/organization and is required.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** repository name

## Version definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Native Label:** package version

## Examples

- `pkg:swift/github.com/Alamofire/Alamofire@5.4.3`
- `pkg:swift/github.com/RxSwiftCommunity/RxFlow@2.12.4`
