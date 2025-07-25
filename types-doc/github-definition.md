<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: github

- **Type Name:** GitHub
- **Description:** GitHub-based packages
- **Schema ID:** `https://packageurl.org/types/github-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:github/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com

## Namespace definition

- **Requirement:** Required
- **Native Label:** user or organization
- **Note:** `The namespace is the user or organization. It is not case sensitive and must be lowercased.`

## Name definition

- **Native Label:** repository name
- **Note:** `The name is the repository name. It is not case sensitive and must be lowercased.`

## Version definition

- **Native Label:** commit or tag
- **Note:** `The version is a commit or tag.`

## Examples

- `pkg:github/package-url/purl-spec@244fd47e07d1004`
- `pkg:github/package-url/purl-spec@244fd47e07d1004#everybody/loves/dogs`
