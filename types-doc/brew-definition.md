<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: brew

- **Type Name:** Homebrew
- **Description:** Homebrew packages for macOS and Linux
- **Schema ID:** `https://packageurl.org/types/brew-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:brew/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://formulae.brew.sh/
- **Note:** The default repository is the Homebrew Formulae at https://formulae.brew.sh/. Homebrew also supports third-party taps (repositories) which can be specified using the namespace or repository_url qualifier.

## Namespace definition

- **Requirement:** Optional
- **Native Label:** tap
- **Note:** `The namespace is the Homebrew tap name, typically in the format 'owner/repo' (e.g., 'homebrew/core', 'some-org/some-tap'). When not specified, formulas are assumed to come from the default 'homebrew/core' tap.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** formula
- **Note:** `The name is the Homebrew formula or cask name. Formula names containing '@' (used for versioned formulas like 'postgresql@12') must have the '@' character percent-encoded as '%40' in the PURL string.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The version is the Homebrew package version. Versions are optional to support use cases where the latest or any available version is acceptable.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional |  |  | The git URL of the tap repository when using a non-default tap. For example, 'https://github.com/some-org/homebrew-some-tap.git'. |

## Examples

- `pkg:brew/sqlite@3.43.2`
- `pkg:brew/go`
- `pkg:brew/postgresql%4012@12.17`
- `pkg:brew/homebrew/core/sqlite@3.43.2`
- `pkg:brew/some-org/some-tap/some-app@1.2.3?repository_url=https://github.com/some-org/homebrew-some-tap.git`

## Reference URLs

- `https://brew.sh/`
- `https://formulae.brew.sh/`
- `https://docs.brew.sh/Taps`
