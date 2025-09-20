<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: cpan

- **Type Name:** CPAN
- **Description:** Perl package distributions published on CPAN
- **Schema ID:** `https://packageurl.org/types/cpan-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:cpan/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://www.cpan.org/

## Namespace definition

- **Requirement:** Required
- **Native Label:** CPAN ID of the author/publisher
- **Note:** `It MUST be written uppercase and is required`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** distribution name
- **Note:** `The name is the distribution name and is case sensitive. A distribution name MUST NOT contain the string '::'`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The version is the distribution version`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional |  |  | CPAN/MetaCPAN/BackPAN/DarkPAN repository base URL |
| download_url | Optional |  |  | URL of package or distribution |
| vcs_url | Optional |  |  | extra URL for a package version control system |
| ext | Optional |  | tar.gz | file extension |

## Examples

- `pkg:cpan/GDT/URI-PackageURL`
- `pkg:cpan/OALDERS/libwww-perl@6.76`
- `pkg:cpan/DROLSKY/DateTime@1.55?repository_url=backpan.perl.org`

## Note

The previous CPAN PURL type specification allowed module names (e.g. URI::PackageURL) to be used as PURL 'name' while also omitting the PURL 'namespace'. The parser MUST emit an error when a module is specified as a PURL 'name' or detect '::' characters.
