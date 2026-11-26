<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: guix

- **Type Name:** GNU Guix
- **Description:** Packages defined for GNU Guix, including packages provided by the official and third-party Guix channels.
- **Schema ID:** `https://packageurl.org/purl-types/guix-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:guix/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://git.guix.gnu.org/guix.git
- **Note:** The default repository is the official GNU Guix channel. Additional channels can be identified using the namespace and repository_url qualifier.

## Namespace definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** channel name
- **Note:** The namespace identifies the Guix channel providing the package. It is required for consistency across all Guix PURLs. Use 'guix' for the official GNU Guix channel, yielding PURLs such as pkg:guix/guix/<name>. For packages from other channels, use the corresponding channel name (e.g. 'nonguix' or 'guix-science') as the namespace and provide the repository_url qualifier to identify the channel's Git repository. Channel names are not globally unique, so the repository_url qualifier helps distinguish channels with the same name.

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** package name
- **Note:** The name is the Guix package name.

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** The version is the Guix package version.

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| output | Optional |  | out | The selected output of the Guix package. Output names are package-specific; examples include 'out', 'bin', 'lib', 'doc', and 'debug'. When omitted, the default 'out' output is assumed. |
| repository_url | Optional |  |  | The URL of the Git repository containing the Guix channel and package definitions. This qualifier should be provided for non-default channels to identify their repository. It is not the upstream source repository URL or a binary substitute server URL. |

## Examples

- `pkg:guix/guix/drawing@1.0.2`
- `pkg:guix/guix/bvi@1.5.0`
- `pkg:guix/guix/glib?output=doc`
- `pkg:guix/guix/glib?output=bin`
- `pkg:guix/nonguix/linux-firmware@20261019?repository_url=https:%2F%2Fgitlab.com%2Fnonguix%2Fnonguix`
