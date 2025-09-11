## Permitted characters

A canonical PURL is composed of these permitted ASCII characters:

- the Alphanumeric Characters: `A to Z`, `a to z`, `0 to 9`,
- the Punctuation Characters: `.-_~` (period '.',
  dash '-', underscore '_' and tilde '~'),
- the Percent Character: `%` (percent sign '%'), and
- the Separator Characters `:/@?=&#` (colon ':', slash '/', at sign '@',
  question mark '?', equal sign '=', ampersand '&' and hash sign '#').


## Separators

This is how each of the Separator Characters is used:

- ':' (colon) is the separator between `scheme` and `type`
- '/' (slash) is the separator between `type`, `namespace` and `name`
- '/' (slash) is the separator between `subpath` segments
- '@' (at sign) is the separator between `name` and `version`
- '?' (question mark) is the separator before `qualifiers`
- '=' (equals) is the separator between a `key` and a `value` of a
  `qualifier`
- '&' (ampersand) is the separator between `qualifiers` (each being a
  `key=value` pair)
- '#' (hash sign) is the separator before `subpath`

## Character encoding

- In the "Rules for each PURL component" section, each component
  defines when and how to apply percent-encoding and decoding to its content.
- When percent-encoding is required by a component definition, the component
  string must first be encoded as UTF-8.
- In the component string, each "data octet" must be replaced by the
  percent-encoded "character triplet" applying the percent-encoding mechanism
  defined in [RFC 3986 section 2.1](https://datatracker.ietf.org/doc/html/rfc3986#section-2.1),
  including the RFC definition of "data octet" and "character triplet",
  and using these definitions for RFC's "allowed set" and "delimiters":

  - "allowed set" is composed of the Alphanumeric Characters and the
    Punctuation Characters
  - "delimiters" is composed of the Separator Characters

- The following characters must not be percent-encoded:

  - the Alphanumeric Characters,
  - the Punctuation Characters,
  - the Separator Characters when being used as PURL separators,
  - the colon ':', whether used as a Separator Character or otherwise, and
  - the percent sign '%' when used to represent a percent-encoded character.

- Where the space ' ' is permitted, it must be percent-encoded as '%20'.
- With the exception of the percent-encoding mechanism, the rules regarding
  percent-encoding are defined by this specification alone.

## Case folding

References to "lowercase" in this specification refer to the **culture-invariant**
full case mapping defined in
[Section 3.13.2 of the Unicode Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G34078).

When applied to the ASCII character set, this operation converts uppercase
Latin letters (`A to Z`) to their corresponding lowercase forms (`a to z`).
All other ASCII characters remain unchanged.
