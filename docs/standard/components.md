## Rules for each `purl` component

A `purl` string is an ASCII URL string composed of seven components.

Except as expressly stated otherwise in this section, each component:

- MAY be composed of any of the characters defined in the "Permitted characters" section
- MUST be encoded as defined in the "Character encoding" section

The "lowercase" rules are defined in the "Case folding" section.

The rules for each component are:

- **scheme**:

  - The `scheme` is a constant with the value "pkg".
  - The `scheme` MUST be followed by an unencoded colon ':'.
  - `purl` parsers MUST accept URLs where the `scheme` and colon ':' are
    followed by one or more slash '/' characters, such as 'pkg://', and MUST
    ignore and remove all such '/' characters.


- **type**:

  - The package `type` MUST be composed only of ASCII letters and numbers,
    period '.', and dash '-'.
  - The `type` MUST start with an ASCII letter.
  - The `type` MUST NOT be percent-encoded.
  - The `type` is case insensitive. The canonical form is lowercase.


- **namespace**:

  - The `namespace` is optional, unless required by the package's `type` definition.
  - If present, the `namespace` MAY contain one or more segments, separated
    by a single unencoded slash '/' character.
  - All leading and trailing slashes '/' are not significant and SHOULD be
    stripped in the canonical form. They are not part of the `namespace`.
  - Each `namespace` segment MUST be a percent-encoded string.
  - When percent-decoded, a segment:

    - MUST NOT contain any slash '/' characters
    - MUST NOT be empty
    - MAY contain any Unicode character other than '/' unless the package's
      `type` definition provides otherwise.

  - A URL host or Authority MUST NOT be used as a `namespace`. Use instead a
    `repository_url` qualifier. Note however that for some types, the
    `namespace` may look like a host.


- **name**:

  - The `name` is prefixed by a single slash '/' separator when the
    `namespace` is not empty.
  - All leading and trailing slashes '/' are not significant and SHOULD be
    stripped in the canonical form. They are not part of the `name`.
  - A `name` MUST be a percent-encoded string.
  - When percent-decoded, a `name` MAY contain any Unicode character unless
    the package's `type` definition provides otherwise.


- **version**:

  - The `version` is prefixed by a '@' separator when not empty.
  - This '@' is not part of the `version`.
  - A `version` MUST be a percent-encoded string.
  - When percent-decoded, a `version` MAY contain any Unicode character unless
    the package's `type` definition provides otherwise.
  - A `version` is a plain and opaque string.


- **qualifiers**:

  - The `qualifiers` component MUST be prefixed by an unencoded question
    mark '?' separator when not empty. This '?' separator is not part of the
    `qualifiers` component.
  - The `qualifiers` component is composed of one or more `key=value`
    pairs. Multiple `key=value` pairs MUST be separated by an
    unencoded ampersand '&'. This '&' separator is not part of an
    individual `qualifier`.
  - A `key` and `value` MUST be separated by the unencoded equal sign '='
    character. This '=' separator is not part of the `key` or `value`.
  - A `value` MUST NOT be an empty string: a `key=value` pair with an
    empty `value` is the same as if no `key=value` pair exists for this
    `key`.

  - For each `key=value` pair:

    - The `key` MUST be composed only of lowercase ASCII letters and numbers,
      period '.', dash '-' and underscore '_'.
    - A `key` MUST start with an ASCII letter.
    - A `key` MUST NOT be percent-encoded.
    - Each `key` MUST be unique among all the keys of the `qualifiers`
      component.
    - A `value` MAY contain any Unicode character and all characters MUST be
      encoded as described in the "Character encoding" section.


- **subpath**:
  - The `subpath` string is prefixed by a '#' separator when not empty
  - This '#' is not part of the `subpath`
  - The `subpath` contains zero or more segments, separated by slash '/'
  - Leading and trailing slashes '/' are not significant and SHOULD be stripped
    in the canonical form
  - Each `subpath` segment MUST be a percent-encoded string
  - When percent-decoded, a segment:

    - MUST NOT contain any slash '/' characters
    - MUST NOT be empty
    - MUST NOT be any of '..' or '.'
    - MAY contain any Unicode character other than '/' unless the package's
      `type` definition provides otherwise.

  - The `subpath` MUST be interpreted as relative to the root of the package
