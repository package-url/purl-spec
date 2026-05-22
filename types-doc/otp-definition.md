<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: otp

- **Type Name:** BEAM/OTP Application
- **Description:** BEAM/OTP applications written in Elixir, Erlang, Gleam and other BEAM languages
- **Schema ID:** `https://packageurl.org/types/otp-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:otp/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** No

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `The component is unused and MUST be empty`

## Name definition

- **Requirement:** Required
- **Native Label:** name
- **Note:** `The OTP application name from the `.app` file; it is case-insensitive and MUST be lower-cased.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The OTP application version (the `vsn` attribute).`

## Subpath definition

- **Requirement:** Optional
- **Native Label:** May be added to reference a specific file or directory inside the OTP application.

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional | Repository URL |  | The canonical origin of the OTP application source. This qualifier is optional, but it should be included whenever the origin is known, and should point to a trusted source repository. |
| platform | Optional | platform |  | The target operating system for native code (e.g. ``linux``, ``darwin``, ``freebsd``, ``sunos``, ``win32``; case-insensitive). |
| arch | Optional | arch |  | The arch is the qualifiers key for a package architecture. |

## Examples

- `pkg:otp/erts@10.6.3?platform=linux&arch=amd64&repository_url=https:%2F%2Fgithub.com%2Ferlang%2Fotp&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Ferlang%2Fotp.git`
- `pkg:otp/stdlib@3.11.2?repository_url=https:%2F%2Fgithub.com%2Ferlang%2Fotp&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Ferlang%2Fotp.git`
- `pkg:otp/crypto@4.6.4?platform=darwin&arch=x86_64&repository_url=https:%2F%2Fgithub.com%2Ferlang%2Fotp&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Ferlang%2Fotp.git`
- `pkg:otp/elixir@1.10.0?repository_url=https:%2F%2Fgithub.com%2Felixir-lang%2Felixir&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Felixir-lang%2Felixir.git`
- `pkg:otp/eex@1.10.0?repository_url=https:%2F%2Fgithub.com%2Felixir-lang%2Felixir&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Felixir-lang%2Felixir.git`
- `pkg:otp/logger@1.10.0?repository_url=https:%2F%2Fgithub.com%2Felixir-lang%2Felixir&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Felixir-lang%2Felixir.git`
- `pkg:otp/rebar@3.13.0?repository_url=https:%2F%2Fgithub.com%2Ferlang%2Frebar3&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Ferlang%2Frebar3.git`
- `pkg:otp/hex@2.1.1?repository_url=https:%2F%2Fgithub.com%2Fhexpm%2Fhex&vcs_url=git%2Bhttps:%2F%2Fgithub.com%2Fhexpm%2Fhex.git`

## Note

- If the component was fetched from a Hex repository, prefer a ``hex`` purl
  because Hex provides a global, collision-free namespace that uniquely ties
  the version to the published source.
- There is no default package repository. When the application can be
  fetched from a known location, add a general qualifier such as
  `repository_url`, `download_url` or `vcs_url`.
