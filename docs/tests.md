## Tests

The Package-URL (PURL) specification provides a JSON Schema and test
files to support language-neutral testing of PURL implementations. The 
objectives for the PURL schema and test files are to enable tools to conform
to the PURL specification for tool functions such as:
- build a canonical PURL string from a set of PURL component-level data
- parse a canonical PURL string into a set of PURL components
- validate an input PURL string and optionally provide warning or info 
messages or correct errors in the input PURL string

The current  JSON schema is available at: `purl-spec/schemas/purl-test.schema-0.1.json`.

The test files are available at:
- `purl-spec/tests/spec/`: This folder contains JSON test files that are not
for a specific PURL type.
  - `specification-test.json` - This file contains an array of test objects
  that primarily cover testing the validity of individual PURL components or
  separators between a pair of PURL components.
  - component-`test.json`: These are test files for a specific PURL component.
- `purl-spec/tests/types/`: This folder contains one JSON test file for each 
registered PURL type. These tests primarily cover the validity of a complete 
PURL for the corresponding PURL type.

Two key properties in the PURL test JSON schema are:

**test_group**

There are two PURL test groups:
- **base**: Test group for base conformance tests. Base tests are pass/fail.
- **advanced**: Test group for advanced tests. Advanced tests are more 
permissive than base tests. They may provide severity messages or correct
errors.

*[Discussion point: Is there a better name than advanced for the second test
group? perhaps Permissive? Or name the groups Strict and Permissive?]*

**test_type**

There are four PURL test types:
- **build**: A test to build a canonical PURL output string from an input of 
decoded PURL components. See also `/docs/how-build.md`.
- **parse**: A test to parse decoded components from a canonical PURL 
input string. See also `/docs/how-parse.md`.
- **roundtrip**: A test to parse an input PURL string and then rebuild it as a canonical PURL output string.
- **validation**: A test to validate a PURL input string and report severity 
messages - info, warning or error. A validation test may optionally correct 
errors in an output PURL string.

*[Discussion point: Do we need both roundtrip and validation test types?]*

**Test case basics**

The standard error-handling behaviour for all test cases is based on two
properties from the PURL test schema:
- `expected_failure` 
  - description: "true if this test input is expected to fail to be 
processed."
  - type: boolean
  - default: false

- `expected_failure_reason`: The reason why this test is is expected to fail 
if expected_failure is true."
   - default: null

In the case of a test case failure the `expected_output` is null.

*[Discussion point: The current test schema does not include any specific
properties for error or other test result messages. Most of the test cases
with an expected failure  ]*






