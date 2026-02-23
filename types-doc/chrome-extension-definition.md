<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: chrome-extension

- **Type Name:** Chrome Browser Extensions
- **Description:** Chrome Browser Extensions. Note: there are currently no officially documented APIs, further there appears to be no way to query different versions of a package - there only seems to be responses on the latest version. To this end the version component of a chrome purl can be optional. Two known data sources are a sitemap which can be crawled to discover (some) extensions at https://chromewebstore.google.com/sitemap, and an 'updatecheck' API which you can read about here https://github.com/Rob--W/crxviewer , and perhaps here https://github.com/chromium/chromium/blob/main/docs/updater/protocol_3_1.md
- **Schema ID:** `https://packageurl.org/types/chrome-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:chrome-extension/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://https://chromewebstore.google.com/
- **Note:** There is no documented API, only a sitemap and 'updatecheck' endpoints.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `There is no namespace`

## Name definition

- **Requirement:** Required
- **Native Label:** extension_id
- **Note:** `The name is a 32 characters a-z and is case insensitive. This is not the same as the display name which is human readable and may vary with locale.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version
- **Note:** `The chrome extension version is semver-like but 1-4 segments`

## Examples

- `pkg:chrome-extension/hlepfoohegkhhmjieoechaddaejaokhf@25.7.1`
- `pkg:chrome-extension/dncgedbnidfkppmdgfgidcepclnokpkb@6.0.2.3611`
- `pkg:chrome-extension/kanfjhdeebkfgkbmnfknhejpadhlmiab@0.6`
- `pkg:chrome-extension/dlpngalgnefjeiefhmpklpfiohadpglk@1`
- `pkg:chrome-extension/dlpngalgnefjeiefhmpklpfiohadpglk`
