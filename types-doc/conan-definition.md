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
- **Note:** `The vendor of the package.`

## Name definition

- **Native Label:** package-name
- **Note:** `The Conan <package-name>.`

## Version definition

- **Native Label:** package-version
- **Note:** `The Conan <package-version>.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| user | Optional | user |  | The Conan <user>. Only required if the Conan package was published with <user>. |
| channel | Optional | channel |  | The Conan <channel>. Only required if the Conan package was published with Conan <channel>. |
| rrev | Optional | recipe revision |  | The Conan recipe revision (optional). If omitted, the purl refers to the latest recipe revision available for the given version. |
| prev | Optional | package revision |  | The Conan package revision (optional). If omitted, the purl refers to the latest package revision available for the given version and recipe revision. |

## Examples

- `pkg:conan/openssl@3.0.3`
- `pkg:conan/openssl.org/openssl@3.0.3?user=bincrafters&channel=stable`
- `pkg:conan/openssl.org/openssl@3.0.3?arch=x86_64&build_type=Debug&compiler=Visual%20Studio&compiler.runtime=MDd&compiler.version=16&os=Windows&shared=True&rrev=93a82349c31917d2d674d22065c7a9ef9f380c8e&prev=b429db8a0e324114c25ec387bfd8281f330d7c5c`

## Note

Additional qualifiers can be used to distinguish Conan packages with different settings or options, e.g. os=Linux, build_type=Debug or shared=True. If no additional qualifiers are used to distinguish Conan packages build with different settings or options, then the purl is ambiguous and it is up to the user to work out which package is being referred to (e.g. with context information).
