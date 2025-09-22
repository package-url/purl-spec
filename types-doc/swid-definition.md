<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: swid

- **Type Name:** Software Identification (SWID) Tag
- **Description:** PURL type for ISO-IEC 19770-2 Software Identification (SWID) tags.
- **Schema ID:** `https://packageurl.org/types/swid-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:swid/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** No
- **Note:** There is no default package repository.

## Namespace definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Native Label:** softwareCreator
- **Note:** `The namespace is the optional name and regid of the entity with a role of softwareCreator. If specified, name is required and is the first segment in the namespace. If regid is known, it must be specified as the second segment in the namespace. A maximum of two segments are supported.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** SoftwareIdentity/name
- **Note:** `The name is the name as defined in the SWID SoftwareIdentity element.`

## Version definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Native Label:** SoftwareIdentity/version
- **Note:** `The version is the version as defined in the SWID SoftwareIdentity element.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| tag_id | Required |  |  | The qualifier tag_id must not be empty and corresponds to the tagId as defined in the SWID SoftwareIdentity element. Per the SWID specification, GUIDs are recommended. If a GUID is used, it must be lowercase. If a GUID is not used, the tag_id qualifier is case aware but not case sensitive. |
| tag_version | Optional |  |  | The qualifier tag_version is an optional integer and corresponds to the tagVersion as defined in the SWID SoftwareIdentity element. If not specified, defaults to 0. |
| patch | Optional |  |  | The qualifier patch is optional and corresponds to the patch as defined in the SWID SoftwareIdentity element. If not specified, defaults to false. |
| tag_creator_name | Optional |  |  | The qualifier tag_creator_name is optional. If the tag creator is different from the software creator, the tag_creator_name qualifier should be specified. |
| tag_creator_regid | Optional |  |  | The qualifier tag_creator_regid is optional. If the tag creator is different from the software creator, the tag_creator_regid qualifier should be specified. |

## Examples

- `pkg:swid/Acme/example.com/Enterprise+Server@1.0.0?tag_id=75b8c285-fa7b-485b-b199-4745e3004d0d`
- `pkg:swid/Fedora@29?tag_id=org.fedoraproject.Fedora-29`
- `pkg:swid/Adobe%2BSystems%2BIncorporated/Adobe%2BInDesign@CC?tag_id=CreativeCloud-CS6-Win-GM-MUL`

## Note

Use of known qualifiers key/value pairs such as download_url can be used to specify where the package was retrieved from.
