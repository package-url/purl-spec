<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: cpan

- **Type Name:** CPAN
- **Description:** CPAN Perl packages
- **Schema ID:** `https://packageurl.org/types/cpan-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:cpan/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://www.cpan.org/

## Namespace definition

- **Requirement:** Optional
- **Note:** `- To refer to a CPAN distribution name, the namespace MUST be present. In this case, the namespace is the CPAN id of the author/publisher. It MUST be written uppercase, followed by the distribution name in the name component. A distribution name MUST NOT contain the string ::.
- To refer to a CPAN module, the namespace MUST be absent. The module name MAY contain zero or more :: strings, and the module name MUST NOT contain a -
`

## Name definition

- **Case Sensitive:** Yes
- **Native Label:** module or distribution name
- **Note:** `The name is the module or distribution name and is case sensitive.`

## Version definition

- **Native Label:** version
- **Note:** `The version is the module or distribution version.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional |  |  | CPAN/MetaCPAN/BackPAN/DarkPAN repository base URL |
| download_url | Optional |  |  | URL of package or distribution |
| vcs_url | Optional |  |  | extra URL for a package version control system |
| ext | Optional |  | tar.gz | file extension |

## Examples

- `pkg:cpan/Perl::Version@1.013`
- `pkg:cpan/DROLSKY/DateTime@1.55`
- `pkg:cpan/DateTime@1.55`
- `pkg:cpan/GDT/URI-PackageURL`
- `pkg:cpan/LWP::UserAgent`
- `pkg:cpan/OALDERS/libwww-perl@6.76`
- `pkg:cpan/URI`
