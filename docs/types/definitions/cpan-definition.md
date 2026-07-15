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

- **Requirement:** Optional
- **Native Label:** CPAN author/publisher ID (CPANID)
- **Note:** `When present, it represents the CPAN author/publisher ID (CPANID) and MUST be uppercase. It is appropriate to use 'namespace' for compatibility with existing CPAN purl producers/consumers or when a workflow explicitly requires author-scoped identifiers. For new identifiers, the 'author' qualifier is the preferred way to specify the author/publisher. When 'version' is omitted, author scoping via 'namespace' MAY be ambiguous because a distribution can change maintainers over time.`

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
| author | Optional |  |  | CPAN author/publisher ID (CPANID) |
| distpath | Optional |  |  | Repository-relative path (not a URL) to the distribution archive or directory, typically under 'authors/id/...' |
| repository_url | Optional |  |  | CPAN/MetaCPAN/BackPAN/DarkPAN repository base URL |
| download_url | Optional |  |  | URL of package or distribution |
| vcs_url | Optional |  |  | extra URL for a package version control system |
| ext | Optional |  | tar.gz | distribution file extension |

## Examples

- `pkg:cpan/perl@5.42`
- `pkg:cpan/DBI@1.646`
- `pkg:cpan/SBOM-CycloneDX`
- `pkg:cpan/URI-PackageURL?author=GDT`
- `pkg:cpan/libwww-perl@6.76?author=OALDERS`
- `pkg:cpan/DateTime@1.55?author=DROLSKY&repository_url=backpan.perl.org`
- `pkg:cpan/Term-Gnuplot@0.90380906?distpath=authors%2Fid%2FI%2FIL%2FILYAZ%2Fmodules%2FTerm-Gnuplot-0.90380906.zip`

## Note

The PURL 'name' MUST be the CPAN distribution name (case sensitive) and MUST NOT contain the '::' separator (module name). The CPAN author/publisher ID (CPANID) is OPTIONAL: when needed, it SHOULD be provided using the 'author' qualifier. The PURL 'namespace' is OPTIONAL and, when present, represents the CPANID and MUST be uppercase; it MAY be used for compatibility with existing identifiers or tooling. When PURL 'version' is omitted, author scoping (via 'author' qualifier or 'namespace') MAY be ambiguous because a distribution can change maintainers over time.
