## Character encoding

- In the "Rules for each ``purl`` component" section, each component
  defines when and how to apply percent-encoding and decoding to its content.
- When percent-encoding is required by a component definition, the component
  string MUST first be encoded as UTF-8.
- In the component string, each "data octet" MUST be replaced by the
  percent-encoded "character triplet" applying the percent-encoding mechanism
  defined in [RFC 3986 section 2.1](https://datatracker.ietf.org/doc/html/rfc3986#section-2.1),
  including the RFC definition of "data octet" and "character triplet",
  and using these definitions for RFC's "allowed set" and "delimiters":
  - "allowed set" is composed of the Alphanumeric Characters and the
    Punctuation Characters
  - "delimiters" is composed of the Separator Characters
- The following characters MUST NOT be percent-encoded:
  - the Alphanumeric Characters,
  - the Punctuation Characters,
  - the Separator Characters when being used as ``purl`` separators,
  - the colon ':', whether used as a Separator Character or otherwise, and
  - the percent sign '%' when used to represent a percent-encoded character.
- Where the space ' ' is permitted, it MUST be percent-encoded as '%20'.
- With the exception of the percent-encoding mechanism, the rules regarding
  percent-encoding are defined by this specification alone.
