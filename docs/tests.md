## Tests

To support the language-neutral testing of `purl` implementations, a test suite
is provided as JSON document named `test-suite-data.json`. This JSON document
contains an array of objects. Each object represents a test with these key/value
pairs some of which may not be normalized:

- **purl**: a `purl` string.
- **canonical**: the same `purl` string in canonical, normalized form
- **type**: the `type` corresponding to this `purl`.
- **namespace**: the `namespace` corresponding to this `purl`.
- **name**: the `name` corresponding to this `purl`.
- **version**: the `version` corresponding to this `purl`.
- **qualifiers**: the `qualifiers` corresponding to this `purl` as an object of
  {key: value} qualifier pairs.
- **subpath**: the `subpath` corresponding to this `purl`.
- **is_invalid**: a boolean flag set to true if the test should report an
  error

To test `purl` parsing and building, a tool can use this test suite and for
every listed test object, run these tests:

- parsing the test canonical `purl` then re-building a `purl` from these parsed
  components should return the test canonical `purl`

- parsing the test `purl` should return the components parsed from the test
  canonical `purl`

- parsing the test `purl` then re-building a `purl` from these parsed components
  should return the test canonical `purl`

- building a `purl` from the test components should return the test canonical `purl`
