## Tests

The Package-URL (PURL) specification provides a JSON schema and many test 
files to support language-neutral testing of PURL implementations. The current
 JSON schema is available at: purl-spec/schemas/purl-test.schema-0.1.json. The
  test files are available at:

- `purl-spec/tests/spec/specification-test.json` - This file contains an array 
of test objects that primarily cover testing the validity of individual PURL 
components or separators between a pair of PURL components.
- `purl-spec/tests/types/` - This folder contains one JSON test file for each 
registered PURL type. These tests primarily cover the validity of a complete 
PURL for the corresponding PURL type. 

Two key properties in the PURL test JSON schema are:

**test_group**: There are two PURL test groups:
- **base**: Test group for base conformance tests for PURL building and 
parsing.
- **advanced**: Test group for advanced tests to support flexible PURL 
building and parsing.

**test_type**: There are three PURL test types:
- **build**: A PURL building test from decoded components to a canonical PURL 
string See also `/docs/how-build.md`.
- **parse**: A PURL building test from decoded components to a canonical PURL 
string. See also `/docs/how-parse.md`.
- **roundtrip**: A PURL roundtrip test, parsing a PURL and then building back a PURL from a canonical string input.

To test PURL parsing and building, a tool can use the specification and type tests to run tests for:

- Parsing an input test canonical PURL then re-building a PURL from the
  parsed components should return the test canonical PURL
- Parsing an input test PURL should return the components parsed from the test
  canonical PURL
- Parsing an input test PURL then re-building a PURL from the parsed
  components should return the test canonical PURL
- Building a PURL from input test components should return the test canonical
  PURL

