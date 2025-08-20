## Rules for each `purl` component

A `purl` string is an ASCII URL string composed of seven components.

Except as expressly stated otherwise in this section, each component:

- May be composed of any of the characters defined in the "Permitted characters" section
- Must be encoded as defined in the "Character encoding" section

The "lowercase" rules are defined in the "Case folding" section.

The rules for each component are:

- **scheme**:

  - The `scheme` is a constant with the value "pkg".
  - The `scheme` must be followed by an unencoded colon ':'.
  - `purl` parsers must accept URLs where the `scheme` and colon ':' are
    followed by one or more slash '/' characters, such as 'pkg://', and must
    ignore and remove all such '/' characters.


- **type**:

  - The package `type` must be composed only of ASCII letters and numbers,
    period '.', and dash '-'.
  - The `type` must start with an ASCII letter.
  - The `type` must not be percent-encoded.
  - The `type` is case insensitive. The canonical form is lowercase.


- **namespace**:

  - The `namespace` is optional, unless required by the package's `type` definition.
  - If present, the `namespace` may contain one or more segments, separated
    by a single unencoded slash '/' character.
  - All leading and trailing slashes '/' are not significant and should be
    stripped in the canonical form. They are not part of the `namespace`.
  - Each `namespace` segment must be a percent-encoded string.
  - When percent-decoded, a segment:

    - Must not contain any slash '/' characters
    - Must not be empty
    - Must contain any Unicode character other than '/' unless the package's
      `type` definition provides otherwise.

  - A URL host or Authority must not be used as a `namespace`. Use instead a
    `repository_url` qualifier. Note however, that for some types, the
    `namespace` may look like a host.


- **name**:

  - The `name` is prefixed by a single slash '/' separator when the
    `namespace` is not empty.
  - All leading and trailing slashes '/' are not significant and should be
    stripped in the canonical form. They are not part of the `name`.
  - A `name` must be a percent-encoded string.
  - When percent-decoded, a `name` may contain any Unicode character unless
    the package's `type` definition provides otherwise.


- **version**:

  - The `version` is prefixed by a '@' separator when not empty.
  - This '@' is not part of the `version`.
  - A `version` must be a percent-encoded string.
  - When percent-decoded, a `version` may contain any Unicode character unless
    the package's `type` definition provides otherwise.
  - A `version` is a plain and opaque string.


- **qualifiers**:

  - The `qualifiers` component must be prefixed by an unencoded question
    mark '?' separator when not empty. This '?' separator is not part of the
    `qualifiers` component.
  - The `qualifiers` component is composed of one or more `key=value`
    pairs. Multiple `key=value` pairs must be separated by an
    unencoded ampersand '&'. This '&' separator is not part of an
    individual `qualifier`.
  - A `key` and `value` must be separated by the unencoded equal sign '='
    character. This '=' separator is not part of the `key` or `value`.
  - A `value` must not be an empty string: a `key=value` pair with an
    empty `value` is the same as if no `key=value` pair exists for this
    `key`.

  - For each `key=value` pair:

    - The `key` must be composed only of lowercase ASCII letters and numbers,
      period '.', dash '-' and underscore '_'.
    - A `key` must start with an ASCII letter.
    - A `key` must not be percent-encoded.
    - Each `key` must be unique among all the keys of the `qualifiers`
      component.
    - A `value` may contain any Unicode character and all characters must be
      encoded as described in the "Character encoding" section.


- **subpath**:
  - The `subpath` string is prefixed by a '#' separator when not empty
  - This '#' is not part of the `subpath`
  - The `subpath` contains zero or more segments, separated by slash '/'
  - Leading and trailing slashes '/' are not significant and should be stripped
    in the canonical form
  - Each `subpath` segment must be a percent-encoded string
  - When percent-decoded, a segment:

    - Must not contain any slash '/' characters
    - Must not be empty
    - Must not be any of '..' or '.'
    - May contain any Unicode character other than '/' unless the package's
      `type` definition provides otherwise.

  - The `subpath` must be interpreted as relative to the root of the package
