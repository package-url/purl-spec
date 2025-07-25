<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: luarocks

- **Type Name:** LuaRocks
- **Description:** Lua packages installed with LuaRocks
- **Schema ID:** `https://packageurl.org/types/luarocks-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:luarocks/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes

## Namespace definition

- **Requirement:** Optional
- **Native Label:** user manifest
- **Note:** `The user manifest under which the package is registered. If not given, the root manifest is assumed. It is case insensitive, but lowercase is encouraged since namespaces are normalized to ASCII lowercase.`

## Name definition

- **Native Label:** name
- **Note:** `The LuaRocks package name. It is case insensitive, but lowercase is encouraged since package names are normalized to ASCII lowercase.`

## Version definition

- **Case Sensitive:** Yes
- **Native Label:** full package version, including module version and rockspec revision
- **Note:** `The full LuaRocks package version, including module version and rockspec revision. It is case sensitive, and lowercase must be used to avoid compatibility issues with older LuaRocks versions. The full version number is required to uniquely identify a version.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional |  |  | The LuaRocks rocks server to be used; useful in case a private server is used (optional). If omitted, https://luarocks.org as default server is assumed. |

## Examples

- `pkg:luarocks/luasocket@3.1.0-1`
- `pkg:luarocks/hisham/luafilesystem@1.8.0-1`
- `pkg:luarocks/username/packagename@0.1.0-1?repository_url=https://example.com/private_rocks_server/`
