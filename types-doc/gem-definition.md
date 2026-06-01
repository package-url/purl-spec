<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: gem

- **Type Name:** RubyGems
- **Description:** RubyGems
- **Schema ID:** `https://packageurl.org/types/gem-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:gem/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://rubygems.org

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `There is no namespace`

## Name definition

- **Requirement:** Required
- **Native Label:** name

## Version definition

- **Requirement:** Optional
- **Native Label:** version

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| platform | Optional | platform | ruby | qualifiers key is used to specify an alternative platform. such as java for JRuby. The implied default is ruby for Ruby MRI. |

## Examples

- `pkg:gem/ruby-advisory-db-check@0.12.4`
- `pkg:gem/jruby-launcher@1.1.2?platform=java`
