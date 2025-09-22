<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: cran

- **Type Name:** CRAN
- **Description:** CRAN R packages
- **Schema ID:** `https://packageurl.org/types/cran-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:cran/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://cran.r-project.org

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** name
- **Note:** `The name is the package name and is case sensitive, but there cannot be two packages on CRAN with the same name ignoring case.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The version is the package version.`

## Examples

- `pkg:cran/A3@1.0.0`
- `pkg:cran/rJava@1.0-4`
- `pkg:cran/caret@6.0-88`
