<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: vipm

- **Type Name:** VI Package
- **Description:** VIPM packages for LabVIEW
- **Schema ID:** `https://packageurl.org/types/vipm-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:vipm/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** VIPM is configured by default with two public repositories, VIPM Community and the NI LabVIEW Tools Network, which can be read without authentication. Users can add other repositories.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** There is no namespace.

## Name definition

- **Requirement:** Required
- **Native Label:** name
- **Note:** The name is the VIPM package name (e.g. oglib_file). It is not case sensitive and shall be lowercased.

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** The version is the package version, including the release suffix when there is one (e.g. 6.0.2.28, 5.0.9-1).

## Examples

- `pkg:vipm/oglib_file@6.0.2.28`
- `pkg:vipm/oglib_lvzip@5.0.9-1`
- `pkg:vipm/mgi_lib_matrix_%26_vector@1.1.0.1`
- `pkg:vipm/ni_gds_2016@1.1.83.83`
