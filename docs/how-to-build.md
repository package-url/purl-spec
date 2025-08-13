## How to build a `purl` string from its components

Building a `purl` ASCII string works from left to right, from `type` to
`subpath`.

Note: some extra type-specific normalizations are required.
See the "Registered types section" for details.

To build a `purl` string from its components:


- Start a `purl` string with the "pkg:" `scheme` as a lowercase ASCII string

- Append the `type` string to the `purl` as an unencoded lowercase ASCII string

  - Append '/' to the `purl`

- If the `namespace` is not empty:

  - Strip the `namespace` from leading and trailing '/'
  - Split on '/' as segments
  - Apply type-specific normalization to each segment if needed
  - UTF-8-encode each segment if needed in your programming language
  - Percent-encode each segment
  - Join the segments with '/'
  - Append this to the `purl`
  - Append '/' to the `purl`
  - Strip the `name` from leading and trailing '/'
  - Apply type-specific normalization to the `name` if needed
  - UTF-8-encode the `name` if needed in your programming language
  - Append the percent-encoded `name` to the `purl`

- If the `namespace` is empty:

  - Apply type-specific normalization to the `name` if needed
  - UTF-8-encode the `name` if needed in your programming language
  - Append the percent-encoded `name` to the `purl`

- If the `version` is not empty:

  - Append '@' to the `purl`
  - UTF-8-encode the `version` if needed in your programming language
  - Append the percent-encoded version to the `purl`

- If the `qualifiers` are not empty and not composed only of key/value pairs
  where the `value` is empty:

  - Append '?' to the `purl`
  - Build a list from all key/value pair:

    - Discard any pair where the `value` is empty.
    - UTF-8-encode each `value` if needed in your programming language
    - If the `key` is `checksum` and this is a list of checksums join this
      list with a ',' to create this qualifier `value`
    - Create a string by joining the lowercased `key`, the equal '=' sign and
      the percent-encoded `value` to create a qualifier

  - Sort this list of qualifier strings lexicographically
  - Join this list of qualifier strings with a '&' ampersand
  - Append this string to the `purl`

- If the `subpath` is not empty and not composed only of empty, '.' and '..'
  segments:

  - Append '#' to the `purl`
  - Strip the `subpath` from leading and trailing '/'
  - Split this on '/' as segments
  - Discard empty, '.' and '..' segments
  - Percent-encode each segment
  - UTF-8-encode each segment if needed in your programming language
  - Join the segments with '/'
  - Append this to the `purl`
