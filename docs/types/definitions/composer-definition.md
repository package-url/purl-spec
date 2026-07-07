<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: composer

- **Type Name:** Composer
- **Description:** Composer PHP packages
- **Schema ID:** `https://packageurl.org/types/composer-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:composer/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://packagist.org

## Namespace definition

- **Requirement:** Required
- **Native Label:** vendor
- **Note:** `The namespace is the vendor. The namespace is not case sensitive and must be lowercased.`

## Name definition

- **Requirement:** Required
- **Native Label:** name
- **Note:** `The name is not case sensitive and must be lowercased. Private, local packages may have no name. In this case you cannot create a purl for these.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version

## Examples

- `pkg:composer/laravel/laravel@5.5.0`
