# PURL test overview

The Package-URL (PURL) specification provides a JSON Schema for test
files to support language-neutral testing of PURL implementations. The 
objective for the PURL test schema and JSON test files is to enable tools to 
conform to the PURL specification for core functions such as:
- build a canonical PURL string from a set of PURL components 
- parse a PURL string into a set of PURL components
- validate a PURL string

The JSON schema for test files *will be* available at: `purl-spec/schemas/purl-test.schema-0.2.json`

The PURL test files are available at:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec) 
This folder contains JSON test files that are for the core specification and 
not for a specific PURL type. 
The specification-level tests are tests required to demonstrate conformance 
with [ECMA-427](https://ecma-tc54.github.io/ECMA-427/). These test cases are
 part of the 'base' **test group**.
  - [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json) This file contains a set of test cases that cover 
testing the validity of PURL strings including separators between PURL 
components.
  - `type-test.json` This file contains tests for the PURL **type** component.
  - `namespace-test.json` This file contains tests for the PURL **namespace** 
component.
  - `name-test.json` This file contains tests for the PURL **name** 
component.
  - `version-test.json` This file contains tests for the PURL **version** 
  component.
  - `qualifiers-test.json` This file contains tests for the PURL **qualifiers** 
component.
  - `subpath-test.json` This file contains tests for the PURL **subpath** 
component.
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types)
This folder contains one JSON test file for each registered PURL **type**. 
These tests are focused on test cases that are specific to a PURL type, such 
as those for the **namespace** or **qualifiers** components. PURL **type**
test cases should not duplicate specification or component level test cases.

This document does not provide specific guidance or instructions for using 
PURL test files. That will be the subject of future "How-to" 
documentation.

Two key test classification properties in the PURL test JSON schema are:
- `test_group`: to distinguish between test cases that demonstrate
conformance with ECMA-427 and registered PURL **type** definitions versus 
other test cases that provide examples of how to build, parse, or validate 
PURL data.
- `test_type`: to organize test cases according to implementation tool 
functionality - building, parsing, or validation.

## Test groups

There are two PURL **test groups** defined in the PURL test schema:
- 'base': for conformance test cases. These are pass/fail tests. 
A PURL implementation tool shall pass all 'base' tests to demonstrate 
conformance with ECMA-427 and registered PURL **type** definitions.
- 'advanced': Test cases that are intended to show a PURL implementation 
tool how to correct a build, parse or validation error or report and anomaly 
in test input data. These tests are informational and not considered to be 
part of the PURL specification.

## Test types

There are three PURL **test types** defined in the PURL test schema:
- 'build': A test to build a canonical PURL output string from an input of 
decoded PURL components.
- 'parse': A test to parse a PURL input string and create a set of decoded
PURL components.
- `validation': A test to validate that a PURL string input complies with 
the specification and the rules for its PURL **type**. This **test type**
was previously named 'roundtrip'.

## Test case output
The PURL specification does not mandate how a PURL implementation tool 
natively reports the success or failure of a test. Implementation languages 
that throw exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL input that fails PURL **type**-specific 
validation should result in different types or enum values.

The PURL test specification provides two levels of error handling and test 
output messages. Note that the PURL test output messages are related to, but 
separate from the `expected_output`.

### Base test group error handling and messages
Test cases in the 'base' **test group** are pass/fail. Error handling for 
test cases in the 'base' **test group** is based on two properties from the 
PURL test schema:
- `expected_failure`
  - description: "true if this test input is expected to fail to be 
processed."
  - type: boolean
  - default: false
- `expected_failure_reason`
  - description: "The reason why this test is expected to fail if 
  expected_failure is true."
  - type: string
  - default: null

### Advanced test group error handling and messages
Test cases in the 'advanced' **test group** are intended to provide specific 
examples of use cases where a tool could:
  - Correct data errors when there is sufficient information in the test 
  input data to provide canonical output data.
  - Provide advisory information beyond the core specification.

Error handling for Test cases in the 'advanced' **test group** is based on 
a set of "advanced" messages that are separate from the 'base' **test group** 
error handling. 

The structure for "advanced" message handling is:

`advanced_message`
  - title: "PURL advanced test message"
  - description: "Output message type and description for an advanced test 
  case."
  - type: object
  - properties:
    - `advanced_message_type`:
      - title: "Message type for the output of an advanced PURL test."
      - description: "Indicates whether an advanced PURL test case shows how to
      update a non-canonical input to a canonical output or provides 
      information about an anomaly in the test input data.
      - type: string
        enum: 
          - 'update': An 'update' level message means some of the test input 
          data is incorrect, but that it can be corrected to canonical form 
          with information from the core specification or from a PURL **type**
          definition as shown in the `expected_output`. Examples are 
          removing extraneous characters in a PURL component or correcting 
          case sensitivity.
          - 'info': An 'info' level message means that there is some anomaly 
          in the test input that is not an error. A common example is the 
          presence of a **namespace** or **qualifiers** value that is not
          currently enumerated for a specific PURL **type**.
    - `advanced_message`: "Advanced PURL test message."
      - title: "Advanced test message".
      - description: "Message explaining the result of an advanced test case."
      - type: string


### Test case examples

### Base test examples

#### Advanced test examples


## Summary of changes from PURL test schema v0.1
- Implement `advanced_message` as an object with 2 properties: 
  - `advanced_message_type` (enum) and 
  - `advanced_message' (string)




