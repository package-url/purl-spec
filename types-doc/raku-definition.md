<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: raku

- **Type Name:** Raku
- **Description:** Raku Programming Language packages
- **Schema ID:** `https://packageurl.org/types/raku-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:raku/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** No
- **Note:** The 'zef' installation program may be configured to obtain from any content delivery system.  By default it will either download files from (https://360.zef.pm), or from the Raku Ecosystem Archive (http://github.com/Raku/REA/tree/main/archive).

## Namespace definition

- **Requirement:** Required
- **Note:** `The namespace indicates the 'auth' of a package, which indicates which ecosystem and author(s) are responsible for the development/maintenance of the package. Although currently it *is* possble to specify a dependency without 'auth', it is considered bad practice and will be disallowed in the not too far future.`

## Name definition

- **Case Sensitive:** Yes
- **Native Label:** distribution name
- **Note:** `The name is the distribution name and is case sensitive. Although technically this can currently also be a module name, it is considered bad practice and will be disallowed in the not too far future.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The version is the distribution versioni dependency or requirement.  If used as a requirement, can contain a postfix '+' to indicate any version higher or equal than the given version.  The version can also consist of just a '*' as an indication of 'any' version. Versions can optionally have a ':' followed by an 'api' value, indicating an API level.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| download_url | Optional |  |  | URL of package or distribution |

## Examples

- `pkg:raku/zef:lizmat/SBOM::CycloneDX@0.0.7`
- `pkg:raku/cpan:TIMOTIMO/JSON::Fast@0.19`
- `pkg:raku/zef:vrurg/Cro::RPC::JSON@0.1.6:2`
- `pkg:raku/zef:lizmat/駱駝道@0.0.1`
- `pkg:raku/zef:lizmat/SBOM::CycloneDX@0.07?download_url=https://360.zef.pm/S/BO/SBOM_CYCLONEDX/e9df9ac7d473c289aae4df19ea10c0289bb04851.tar.gz`
- `pkg:raku/cpan:TIMOTIMO/JSON::Fast@0.19?download_url=https://cpan.metacpan.org/authors/id//T/TI/TIMOTIMO/Perl6/JSON-Fast-0.19.tar.gz`
