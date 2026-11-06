<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: nipkg

- **Type Name:** NI Package
- **Description:** NI Packages installed with NI Package Manager (NIPM)
- **Schema ID:** `https://packageurl.org/types/nipkg-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:nipkg/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** NI publishes its package feeds at https://download.ni.com/, readable without authentication. Other publishers and users host their own feeds.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** There is no namespace.

## Name definition

- **Requirement:** Required
- **Native Label:** name
- **Note:** The name is not case sensitive and shall be lowercased.

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** The version is the package Version (e.g. 23.8.0.49349-0+f197), not the DisplayVersion.

## Examples

- `pkg:nipkg/ni-daqmx@23.8.0.49349-0%2Bf197`
- `pkg:nipkg/ni-daqmx-25.0.1-dotnet-fx45-runtime@25.0.1.49157-0%2Bf5`
