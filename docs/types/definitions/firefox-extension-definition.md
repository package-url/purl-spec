<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: firefox-extension

- **Type Name:** Firefox Browser Extensions (Add-ons)
- **Description:** Firefox Browser Extensions (add-ons), typically distributed through addons.mozilla.org (AMO). AMO exposes a documented public API where add-ons can be looked up by extension ID, and where previous versions of an add-on are listed and remain downloadable. See https://mozilla.github.io/addons-server/topics/api/addons.html
- **Schema ID:** `https://packageurl.org/types/firefox-extension-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:firefox-extension/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://addons.mozilla.org
- **Note:** An add-on can be queried at https://addons.mozilla.org/api/v5/addons/addon/<extension-id>/ and its versions at https://addons.mozilla.org/api/v5/addons/addon/<extension-id>/versions/. Extensions may also be signed by Mozilla and self-distributed outside of AMO, in which case there is no repository.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `There is no namespace`

## Name definition

- **Requirement:** Required
- **Permitted Characters:** `^([a-zA-Z0-9-._]*@[a-zA-Z0-9-._]+|\{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\})$`
- **Case Sensitive:** Yes
- **Native Label:** extension_id
- **Note:** `The name is the extension ID set in the 'browser_specific_settings.gecko.id' key of manifest.json: either an email-like string of 80 characters or less (e.g. 'uBlock0@raymondhill.net') or a GUID enclosed in curly braces (e.g. '{d10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d}'). This is the stable unique identifier of an add-on; it is not the same as the human-readable display name, nor the mutable AMO listing slug used in store page URLs. Because '@', '{' and '}' are not allowed as-is in a PURL name, they must be percent-encoded as %40, %7B and %7D in the PURL string. See https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_specific_settings`

## Version definition

- **Requirement:** Optional
- **Permitted Characters:** `^\d+(\.\d+){0,3}$`
- **Native Label:** version
- **Note:** `The version is semver-like with 1 to 4 dot-separated numbers, as set in the 'version' key of manifest.json. addons.mozilla.org enforces this format for new submissions; a few older add-on versions predating this rule may not conform. When the version is omitted, the PURL references the latest version. See https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version`

## Examples

- `pkg:firefox-extension/uBlock0%40raymondhill.net@1.72.2`
- `pkg:firefox-extension/%40testpilot-containers@8.3.8`
- `pkg:firefox-extension/%7Bd10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d%7D@4.41.1`
- `pkg:firefox-extension/uBlock0%40raymondhill.net`

## Reference URLs

- `https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_specific_settings`
- `https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version`
- `https://mozilla.github.io/addons-server/topics/api/addons.html`
