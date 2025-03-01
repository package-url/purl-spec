> NOTE: This file was auto-generated from the canonical JSON definition. Do not manually edit this file. Changes should be made in the corresponding JSON definition.

# PURL Type Definition: swid

**Name:** Software Identification (SWID) Tag

**Description:** PURL type for ISO-IEC 19770-2 Software Identification (SWID) tags, uniquely identifying software products.

**Schema ID:** `https://purl-spec.org/types/swid.json`

## PURL Syntax

The structure of a PURL for this package type is:

```
pkg:swid/<namespace>/<name>@<version>?<qualifiers>#<subpath>
```

## Namespace

- **Requirement:** Optional
- **Allowed Characters:** `^[a-zA-Z0-9.+_\- ]+(/[a-zA-Z0-9.+_\- ]+)?$`
- **Case Sensitivity:** case-sensitive
- **Native Label:** softwareCreator

## Name

- **Requirement:** Required
- **Allowed Characters:** `^[a-zA-Z0-9.+_\- ]+$`
- **Case Sensitivity:** case-sensitive
- **Native Label:** SoftwareIdentity/name

## Version

- **Requirement:** Optional
- **Allowed Characters:** `^[a-zA-Z0-9.+_\- ]+$`
- **Case Sensitivity:** case-sensitive
- **Native Label:** SoftwareIdentity/version

## Subpath

- **Requirement:** Optional
- **Description:** No description provided.

## Qualifiers

| Name | Requirement | Description |
|------|-------------|-------------|
| tag_id | Required | The tagId as defined in the SWID SoftwareIdentity element. GUIDs must be lowercase. If not a GUID, case-aware but case-insensitive. |
| tag_version | Optional | The tagVersion as defined in the SWID SoftwareIdentity element. Must be an integer. Defaults to 0 if not specified. |
| patch | Optional | Indicates whether the SWID tag corresponds to a patch. Defaults to false if not specified. |
| tag_creator_name | Optional | The entity that created the SWID tag, if different from the software creator. |
| tag_creator_regid | Optional | The registration ID (regid) of the entity that created the SWID tag, if different from the software creator. |

## Repository Information

- **Uses Repository:** No
- **Additional Info:** SWID PURLs do not reference a package repository.

## Examples

- `pkg:swid/Acme/example.com/Enterprise+Server@1.0.0?tag_id=75b8c285-fa7b-485b-b199-4745e3004d0d`
- `pkg:swid/Fedora@29?tag_id=org.fedoraproject.Fedora-29`
- `pkg:swid/Adobe+Systems+Incorporated/Adobe+InDesign@CC?tag_id=CreativeCloud-CS6-Win-GM-MUL`

