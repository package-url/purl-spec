<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: chrome

- **Type Name:** chrome
- **Description:** Chrome Browser Extensions (extensions from the official Chrome Webstore)
- **Schema ID:** `https://packageurl.org/types/chrome-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:chrome/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://https://chromewebstore.google.com/
- **Note:** There is no documented API, only a sitemap and 'updatecheck' endpoints.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `There is no namespace`

## Name definition

- **Native Label:** version
- **Note:** `The name is a 32 characters a-z and is case insensitive`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The chrome extension version is semver-like but 1-4 segments`

## Examples

- `pkg:chrome/hlepfoohegkhhmjieoechaddaejaokhf@25.7.1`
- `pkg:chrome/dncgedbnidfkppmdgfgidcepclnokpkb@6.0.2.3611`
- `pkg:chrome/kanfjhdeebkfgkbmnfknhejpadhlmiab@0.6`
- `pkg:chrome/dlpngalgnefjeiefhmpklpfiohadpglk@1`
- `pkg:chrome/dlpngalgnefjeiefhmpklpfiohadpglk`

## Note

There is currently no documented API for querying different versions of a package - there only seems to be responses on the latest version. To this end the version component of a chrome purl can be optional.
