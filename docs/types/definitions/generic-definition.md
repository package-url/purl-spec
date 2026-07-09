<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: generic

- **Type Name:** Generic Package
- **Description:** The generic type is for plain, generic packages that do not fit anywhere else such as for "upstream-from-distro" packages. In particular this is handy for a plain version control repository such as a bare git repo in combination with a vcs_url.
- **Schema ID:** `https://packageurl.org/types/generic-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:generic/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** No
- **Note:** There is no default repository.

## Namespace definition

- **Requirement:** Optional
- **Note:** `there is no generic namespace definition`

## Name definition

- **Requirement:** Required
- **Note:** `as for other type, the name component is mandatory. In the worst case it can be a file or directory name.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| download_url | Optional |  |  | A download_url and checksum may be provided in qualifiers or as separate attributes outside of a purl for proper identification and location. |
| checksum | Optional |  |  | A checksum may be provided in qualifiers or as separate attributes outside of a purl for proper identification and location. |

## Examples

- `pkg:generic/openssl@1.1.10g`
- `pkg:generic/openssl@1.1.10g?download_url=https://openssl.org/source/openssl-1.1.0g.tar.gz&checksum=sha256:de4d501267da`
- `pkg:generic/bitwarderl?vcs_url=git%2Bhttps://git.fsfe.org/dxtr/bitwarderl%40cc55108da32`

## Note

When possible another or a new purl type should be used instead of using the generic type and eventually contributed back to this specification. Example have been truncated for brevity
