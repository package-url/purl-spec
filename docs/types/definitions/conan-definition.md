<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: conan

- **Type Name:** Conan C/C++ packages
- **Description:** Conan C/C++ packages. The purl is designed to closely resemble the Conan-native <package-name>/<package-version>@<user>/<channel> syntax for package references as specified in https://docs.conan.io/en/1.46/cheatsheet.html#package-terminology
- **Schema ID:** `https://packageurl.org/types/conan-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:conan/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://center.conan.io

## Namespace definition

- **Requirement:** Optional
- **Native Label:** vendor
- **Note:** The vendor of the package.

## Name definition

- **Requirement:** Required
- **Native Label:** package-name
- **Note:** The Conan <package-name>.

## Version definition

- **Requirement:** Optional
- **Native Label:** package-version
- **Note:** The Conan <package-version>.

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| user | Optional | user |  | The Conan <user>. Only required if the Conan package was published with <user>. |
| channel | Optional | channel |  | The Conan <channel>. Only required if the Conan package was published with Conan <channel>. |
| rrev | Optional | recipe revision |  | The Conan recipe revision (optional). If omitted, the purl refers to the latest recipe revision available for the given version. |
| package_id | Optional | package_id |  | The Conan package ID (optional). Conan computes the package ID from the settings, options and requirements of a binary package and uses it to identify the binary packages of a recipe revision. If omitted, the purl does not refer to a specific binary package. |
| prev | Optional | package revision |  | The Conan package revision (optional). If omitted, the purl refers to the latest package revision available for the given version, recipe revision and package ID. |

## Examples

- `pkg:conan/openssl@3.0.3`
- `pkg:conan/openssl@3.1.2?package_id=0348efdcd0e319fb58ea747bb94dbd88850d6dd1&rrev=8879e931d726a8aad7f372e28470faa1`
- `pkg:conan/openssl.org/openssl@3.0.3?channel=stable&user=bincrafters`
- `pkg:conan/openssl.org/openssl@3.0.3?arch=x86_64&build_type=Debug&compiler=Visual%20Studio&compiler.runtime=MDd&compiler.version=16&os=Windows&prev=b429db8a0e324114c25ec387bfd8281f330d7c5c&rrev=93a82349c31917d2d674d22065c7a9ef9f380c8e&shared=True`

## Note

Use the package_id qualifier to refer to a specific Conan binary package. Additional qualifiers can be used to distinguish Conan packages with different settings or options, e.g. os=Linux, build_type=Debug or shared=True. These additional qualifiers may not be sufficient to identify a binary package, because the package ID also depends on the requirements of the package. If neither the package_id qualifier nor additional qualifiers are used to distinguish Conan packages build with different settings or options, then the purl is ambiguous and it is up to the user to work out which package is being referred to (e.g. with context information).
