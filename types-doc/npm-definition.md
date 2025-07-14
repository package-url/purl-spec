<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: npm

- **Type Name:** Node Package Manager (npm)
- **Description:** PURL type for npm packages.
- **Schema ID:** `https://packageurl.org/types/npm-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:npm/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Namespace definition

- **Requirement:** Optional
- **Native Label:** scope

## Name definition

- **Native Label:** name

## Version definition

- **Case Sensitive:** Yes
- **Native Label:** version

## Repository Information

- **Use Repository:** Yes
- **Default Repository Name:** npm Registry
- **Default Repository URL:** https://registry.npmjs.org/
- **Description:** The official npm package repository.

## Examples

- `pkg:npm/foobar@12.3.1`
- `pkg:npm/%40angular/animation@12.3.1`
- `pkg:npm/mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git%404345abcd34343`
