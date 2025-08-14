## How to parse a `purl` string into its components

Parsing a `purl` ASCII string into its components works from right to left,
from `subpath` to `type`.

Note: some extra type-specific normalizations are required.
See the "Registered types section" for details.

To parse a `purl` string in its components:

- Split the `purl` string once from right on '#'

  - The left side is the `remainder`
  - Strip the right side from leading and trailing '/'
  - Split this on '/'
  - Discard any empty string segment from that split
  - Percent-decode each segment
  - Discard any '.' or '..' segment from that split
  - UTF-8-decode each segment if needed in your programming language
  - Join segments back with a '/'
  - This is the `subpath`

- Split the `remainder` once from right on '?'

  - The left side is the `remainder`
  - The right side is the `qualifiers` string
  - Split the `qualifiers` on '&'. Each part is a `key=value` pair
  - For each pair, split the `key=value` once from left on '=':

    - The `key` is the lowercase left side
    - The `value` is the percent-decoded right side
    - UTF-8-decode the `value` if needed in your programming language
    - Discard any key/value pairs where the value is empty
    - If the `key` is `checksum`, split the `value` on ',' to create
      a list of checksums

  - This list of key/value is the `qualifiers` object

- Split the `remainder` once from left on ':'

  - The left side lowercased is the `scheme`
  - The right side is the `remainder`

- Strip all leading and trailing '/' characters (e.g., '/', '//', '///' and
  so on) from the `remainder`

  - Split this once from left on '/'
  - The left side lowercased is the `type`
  - The right side is the `remainder`

- Split the `remainder` once from right on '@'

  - The left side is the `remainder`
  - Percent-decode the right side. This is the `version`.
  - UTF-8-decode the `version` if needed in your programming language
  - This is the `version`

- Split the `remainder` once from right on '/'

  - The left side is the `remainder`
  - Strip all leading characters (e.g., '/', '//' and so on)
    from the right side
  - Percent-decode the right side. This is the `name`
  - UTF-8-decode this `name` if needed in your programming language
  - Apply type-specific normalization to the `name` if needed
  - This is the `name`

- Split the `remainder` on '/'

  - Strip all leading '/' characters (e.g., '/', '//' and so on)
    from that split
  - Discard any empty segment from that split
  - Percent-decode each segment
  - UTF-8-decode each segment if needed in your programming language
  - Apply type-specific normalization to each segment if needed
  - Join segments back with a '/'
  - This is the `namespace`
