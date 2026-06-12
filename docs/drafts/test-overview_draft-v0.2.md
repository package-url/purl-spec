# PURL test overview

The Package-URL (PURL) specification provides a JSON Schema for test
files to support language-neutral testing of PURL implementations. The 
objective for the PURL test schema and JSON test files is to enable tools to 
conform to the PURL specification for core functions such as:
- build a canonical PURL string from a set of PURL components 
- parse a PURL string into a set of PURL components
- validate a PURL string

## Test files

Each PURL test file is a collection of test cases whose structure is defined
by the PURL test schema (a JSON Schema). The PURL test schema is not currently
included in the [ECMA-427 1st edition](https://ecma-tc54.github.io/ECMA-427/) 
PURL standard because it is still under active development.

See [PURL Tests](https://packageurl.org/docs/purl/schemas#purl-tests) for 
details about the current PURL test schema.

The PURL test files are available at:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec) 
This folder contains JSON test files that are for the core specification and 
not for a specific PURL type. 
The specification-level tests are tests required to demonstrate conformance 
with [ECMA-427](https://ecma-tc54.github.io/ECMA-427/). 
  - [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json): This file contains a set of test cases that cover 
testing the validity of PURL strings including separators between PURL components.
  - There is a current proposal to add component-specific test files with the naming convention: <component-name>-test.json`
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types):
This folder contains one JSON test file for each registered PURL **type**. 
These tests are focused on test cases that are specific to a PURL type, such 
as those for the **namespace** or **qualifiers** components. PURL **type**
test cases should not duplicate specification or component level test cases.

This document does not provide specific guidance or instructions for using 
PURL test files. That will be the subject of future "How-to" documentation.

The PURL specification does not mandate how a PURL implementation tool 
natively reports the success or failure of a test. Implementation languages 
that throw exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL input that fails PURL **type**-specific 
validation should result in different types or enum values.

## Test cases
The basic structure of a PURL test case is:
- `description`: string
- `test_type`: 'build', 'parse' or 'validation'
- `input`: a PURL string or a set (object) of PURL components
- `expected_output`: a PURL string or a set (object) of PURL components
- `expected_failure`: boolean
- `expected_failure_reason`: string
- `test_message`: object
   - `message_type`: 'info' or 'update`
   - `message_text`: string

Each test case is granular such that an expected failure condition covers only 
one error. This means that a test case should only cover an error for a single
PURL component or a single parsing error related to separator characters. This
is necessary to keep failure reasons and test messages simple for conformance 
tests. It is not intended to constrain the error message handling implemented
by a PURL tool.

### Test types
PURL test cases are organized according to three **test types** that map 
to typical implementation tool functionality - building, parsing, or 
validation. The three PURL **test types** defined in the PURL test schema are:
- 'build': A test for the use case of building a canonical PURL output string 
from an input of decoded PURL components.
- 'parse': A test for the use case of parsing a PURL input string and creating
 a set of decoded PURL components.
- `validation': A test for the use case of validating that a PURL string input
 complies with the core specification (ECMA-427) and the rules for its PURL 
 **type**. This **test type** was previously named 'roundtrip'.

### Error handling and messages
The PURL test specification covers two levels of error handling and 
messages. 
- **expected failure**: Each test case must specify `expected_failure` as a 
boolean and it must provide the `expected_failure_reason` if `expected_failure`
is true. The `expected_failure_reason` is the primary error message for a test case
and it should describe a specific reason for the failure - e.g. "PURL type input
contains invalid character(s)."
- **test message**: A `test_message` applies only for a test case where 
`expected_failure` is false.

#### Expected failures
PURL test cases are pass/fail based on two properties from the PURL test 
schema:
- `expected_failure`
  - description: "true if this test input is expected to fail to be 
processed."
  - type: boolean
  - default: 'false'
- `expected_failure_reason`
  - description: "The reason why this test is expected to fail if 
  expected_failure is true."
  - type: string
  - default: null

#### Test messages
In addition to the basic error handling a PURL test case may provide a message
to provide additional information for a non-failure test for two use cases:
  - Provide advisory information beyond the core specification. This is most
  often information for a specific PURL **type**.
  - Document where the test case includes an update to the input data that is
  required by the core specification. This is a rare use case. 

The structure for PURL test message handling is:

`test_message`
  - title: "PURL test message"
  - description: "Output message type and description for a PURL test case."
  - type: object
  - properties:
    - `message_type`:
      - title: "Message type for the output of a PURL test."
      - description: "Indicates whether a PURL test case includes an
      update of a non-canonical input to a canonical output or provides 
      information about an anomaly in the test input data.
      - type: string (enum of;)
          - 'info': An 'info' level message means that there is some anomaly 
          in the test input that is not an error. A common example is the 
          presence of a **namespace** or **qualifiers** value that is not
          currently enumerated for a specific PURL **type**.
          - 'update': An 'update' level message means the PURL spec requires 
          some normalization of the test input to produce a canonical output.
          An example from ECMA-427 Clause 5.6.1 is: "PURL parsers shall accept 
          URLs where the scheme and colon ':' are followed by one or more 
          slash '/' characters, such as 'pkg://', and shall ignore and remove 
          all such '/' characters." 

    - `message_text`:
      - title: "PURL test message".
      - description: "Message providing details about the result of a test 
      case in addition to basic error handling."
      - type: string

### Expected test output
PURL **failure reasons** and **test messages** are separate from 
`expected_output`. 
- The `expected_output` for a successful test is a canonical PURL string or a 
set of decoded PURL components. If a test case includes normalization of test
input required by the PURL specification, then the test case must include a
`test_message` (`message_type: "update") that documents the normalization.
- The `expected_output` for a failing test is null.

## Summary of changes from PURL test schema v0.1
- Removed **test group** in favor of one set of tests to focus on conformance 
with the PURL specification.
- Renamed **test type** 'roundtrip' to 'validation'
- Added `test_message` as an object with 2 properties: 
  - `message_type` (enum) and 
  - `message_text` (string)

## Open questions
- Do we really need two types of **test message**s?
   - The only "normalization" required by the ECMA-427 1st edition appears to be:
 Clause 5.6.1: "PURL parsers shall accept URLs where the scheme and colon ':'
are followed by one or more slash '/' characters,  such as 'pkg://', and shall
ignore and remove all such '/' characters." 
   - If that is the case then we should be able to simplify the **test message**
from an object to a string for the message (& possibly rename it) and
devise some other way to deak with the normalization anomaly in Clause 5.6.1.

## Action items
- Create new PURL component level test files by extracting them from
`tests/spec/specification-test.json`
- Review and resolve the impact of changes to current PRs - most are listed
at: [Upgrade PURL test suite](https://github.com/orgs/package-url/projects/10)
- Contact maintainers of known PURL implementations (toolgrid) for feedback and
impact analysis
- Draft "How to create a PURL test case"

## Open items
The following proposed changes to the PURL test framework are not covered
by this draft:
- Defining a unique name for each test case (manual or generated)
- Moving test cases to one file per test case
- Adding an ABNF grammmar


