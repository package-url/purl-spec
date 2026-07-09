<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: pub

- **Type Name:** Pub
- **Description:** Dart and Flutter pub packages
- **Schema ID:** `https://packageurl.org/types/pub-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:pub/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://pub.dartlang.org

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Permitted Characters:** `^[a-z0-9_]`
- **Normalization rules:**
  - Replace non-[a-z] letters, non-[0-9] digits with underscore _
- **Native Label:** name
- **Note:** `Pub normalizes all package names to be lowercase and using underscores. The only allowed characters are [a-z0-9_]. More information on pub naming and versioning is available in the pubspec documentation https://dart.dev/tools/pub/pubspec`

## Version definition

- **Requirement:** Optional
- **Native Label:** version

## Examples

- `pkg:pub/characters@1.2.0`
- `pkg:pub/flutter@0.0.0`
