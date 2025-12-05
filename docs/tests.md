## Tests

The Package-URL (PURL) specification provides a JSON Schema and test
files to support language-neutral testing of PURL implementations. The 
objectives for the PURL schema and test files are to enable tools to conform
to the PURL specification for tool functions such as:
- build a canonical PURL string from a set of PURL component data
- parse a canonical PURL string into a set of PURL components
- parse a PURL string input and rebuild it as a canonical PURL string

The current  JSON schema is available at: [`purl-spec/schemas/purl-test.schema-0.1.json`](https://github.com/package-url/purl-spec/blob/main/schemas/purl-test.schema-0.1.json).

The test files are available at:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec): 
This folder contains JSON test files that are not for a specific PURL type.
  - [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json) - This file contains an array of test objects
  that primarily cover testing the validity of individual PURL components,
  separators between PURL components, and complete PURL strings.
  - There is a proposal to add separate test files in this folder for each 
  PURL component.
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types): This folder contains one JSON test file for each registered PURL type. These 
tests should be focused on test cases that are specific to a PURL type, such 
as those for namespace or qualifiers.

Two key properties in the PURL test JSON schema are:
- Test groups
- Test types

### Test groups

There are two PURL test groups:
- **base**: Test group for base conformance tests. Base tests are pass/fail.
- **advanced**: Test group for advanced tests. Advanced tests are more 
permissive than base tests. They may correct some errors.

### Test types

There are three PURL test types:
- **build**: A test to build a canonical PURL output string from an input of 
decoded PURL components. See also [`/docs/how-build.md`](https://github.com/package-url/purl-spec/blob/main/docs/how-to-build.md).
- **parse**: A test to parse a PURL input string into a set of decoded components. See also [`/docs/how-parse.md`](https://github.com/package-url/purl-spec/blob/main/docs/how-to-parse.md).
- **roundtrip**: A test to parse an input PURL string and then rebuild it as a
 canonical PURL output string.

### Test case basics

#### Test case fields
The fields for each test case are:
- description: description of the test case purpose
- test_group: base or advanced
- test_type: build, parse, or roundtrip
- input: PURL string or set of PURL components
- expected_output: canonical PURL string, set of PURL components or null for 
an expected test failure
- expected_failure: true or false
- expected_failure_reason: description of the reason for the test case failure

#### Error handling
The standard error-handling behaviour for all test cases is based on two
properties from the PURL test schema:
```
"expected_failure": {
          "title": "Expected failure",
          "description": "true if this test input is expected to fail to be processed.",
          "type": "boolean",
          "default": false
        },
        "expected_failure_reason": {
          "title": "Expected failure reason",
          "description": "The reason why this test is expected to fail if expected_failure is true.",
          "default": null,
          "type": [
            "string",
            "null"
          ]
        }          
```
In the case of a test case failure the `expected_output` is null.





