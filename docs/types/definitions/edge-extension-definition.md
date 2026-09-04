<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: edge-extension

- **Type Name:** Microsoft Edge Browser Extensions (Add-ons)
- **Description:** Microsoft Edge Browser Extensions (Add-ons), distributed through the Microsoft Edge Add-ons store. Edge extensions use the same CRX packaging and 32-character extension ID format as Chrome extensions. There is no officially documented store API; two known data sources are a product details endpoint at https://microsoftedge.microsoft.com/addons/getproductdetailsbycrxid/<extension-id> and an 'updatecheck' style endpoint at https://edge.microsoft.com/extensionwebstorebase/v1/crx which follows the same protocol as the Chrome Web Store, see https://github.com/chromium/chromium/blob/main/docs/updater/protocol_3_1.md
- **Schema ID:** `https://packageurl.org/types/edge-extension-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:edge-extension/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://microsoftedge.microsoft.com/addons
- **Note:** Store pages are at https://microsoftedge.microsoft.com/addons/detail/<slug>/<extension-id>. There is no officially documented API, and only the latest version of an extension is publicly available.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `There is no namespace`

## Name definition

- **Requirement:** Required
- **Permitted Characters:** `^[a-p]{32}$`
- **Native Label:** extension_id
- **Note:** `The name is the extension ID: 32 characters in the range a-p (base16-encoded with letters instead of hex digits), the same format as Chrome extension IDs, and is case insensitive. This is not the same as the display name, which is human readable and may vary with locale. The extension ID is the last path segment of the store page URL.`

## Version definition

- **Requirement:** Optional
- **Permitted Characters:** `^\d+(\.\d+){0,3}$`
- **Native Label:** version
- **Note:** `The edge extension version is semver-like but 1-4 segments, following the same manifest version format as Chrome extensions. When the version is omitted, the PURL references the latest version. See https://developer.chrome.com/docs/extensions/reference/manifest/version`

## Examples

- `pkg:edge-extension/odfafepnkmbhccpbejgmiehpchacaeak@1.72.2`
- `pkg:edge-extension/cimighlppcgcoapaliogpjjdehbnofhn@2026.714.1952`
- `pkg:edge-extension/nffknjpglkklphnibdiadeeeeailfnog@25.5.0`
- `pkg:edge-extension/odfafepnkmbhccpbejgmiehpchacaeak`

## Reference URLs

- `https://learn.microsoft.com/en-us/microsoft-edge/extensions/`
- `https://developer.chrome.com/docs/extensions/reference/manifest/version`
- `https://github.com/chromium/chromium/blob/main/docs/updater/protocol_3_1.md`
