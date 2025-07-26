<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: npm

- **Type Name:** Node NPM packages
- **Description:** PURL type for npm packages.
- **Schema ID:** `https://packageurl.org/types/npm-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:npm/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://registry.npmjs.org/
- **Note:** The default repository is the npm Registry at https://registry.npmjs.org

## Namespace definition

- **Requirement:** Optional
- **Native Label:** scope
- **Note:** `The namespace is used for the scope of a scoped NPM package. The npm scope @ sign prefix is always percent encoded, as it was in the early days of npm scope.`

## Name definition

- **Native Label:** name
- **Note:** `Per the package.json spec, new package 'must not have uppercase letters in the name', therefore the name must be lowercased. The npm name used to be case sensitive in the early days for some old packages.`

## Version definition

- **Case Sensitive:** Yes
- **Native Label:** version

## Examples

- `pkg:npm/foobar@12.3.1`
- `pkg:npm/%40angular/animation@12.3.1`
- `pkg:npm/mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git%404345abcd34343`
