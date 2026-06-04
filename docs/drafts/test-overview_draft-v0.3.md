# PURL test overview

The Package-URL (PURL) specification provides a JSON Schema for test
files to support language-neutral testing of PURL implementations. The 
objective for the PURL test schema and JSON test files is to enable tools to 
conform to the PURL specification for core functions such as:
- build a PURL string from a set of PURL components 
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
  - There is a current proposal to add component-specific test files with the 
  naming convention: `<component-name>-test.json`
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types):
This folder contains one JSON test file for each registered PURL **type**. 
These tests are focused on test cases that are specific to a PURL type, such 
as those for the **namespace** or **qualifiers** components. PURL **type**
test cases should not duplicate specification or component level test cases.

The PURL specification does not mandate how a PURL implementation tool 
natively reports the success or failure of a test. Implementation languages 
that throw exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL input that fails PURL **type**-specific 
validation should result in different types or enum values.

## Test cases
The basic structure of a PURL test case is:
- `test_description`: string
- `test_type`: 'build', 'parse' or 'validation'
- `test_input`: a PURL string or an object containing PURL components
- `test_result`: string with an enum of: 'failure' or 'success'
- `test_output`: a PURL string or an object containing PURL components
- `test_message`: string

Each test case is granular such that an expected failure condition covers only 
one error. This means that a test case should only cover an error for a single
PURL component or a single parsing error related to separator characters. This
is necessary to keep failure reasons and test messages simple for conformance 
tests. It is not intended to constrain the error message handling implemented
by a PURL tool.

### Description
The **description** should describe the condition that is the subject of a
test case.

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

### Test input
**Test input** may be a PURL string or an object containing PURL components.

**Test input** does not need to be canonical, but any test with non-canonical
input shall fail.

### Test result
The **test result** must be 'failure' or 'success'
- If a **test result** is 'failure' then then a **test message** explaining
the failure is required.
- If a **test result** is "success' then a **test message** is optional.

### Test output
**Test output** is either a canonical PURL string or an object containing
a set of decoded PURL components.
- If a **test result** is 'failure' then then the **test output** is null.
- If a **test result** is "success' then the **test output** is required.

### Test message
A **test message** is a string that provides information about the **test 
result**.
- If a **test result** is 'failure' then then the **test message** is required
and should explain the reason for the 'failure'.
- If a **test result** is "success' then the **test message** is optional. The 
typical reason for a **test message** in this case is to provide a "warning" 
about test case content - most often related to PURL **type** definitions.
Some examples are:
   - The **namespace** from the input is syntactically correct, but is not 
included in the list of **namespace** values enumerated in the corresponding 
PURL **type** definition.
   - A **key** value in **qualifiers** input is syntactically correct, but is not
included in the list of **qualifiers** values enumerated in the corresponding 
PURL **type** definition.

## Summary of changes from PURL test schema v0.1
- Renamed test case properties to simpler names:
   - Renamed `expected_output` to `output`
   - Renamed `expected_failure` to `result` and changed it from a boolean to
  a string with 2 enumerated values: 'failure' or 'success'
   - Renamed `expected_failure_reason` to `message`
- Removed **test group** in favor of one set of tests to focus on conformance 
with the PURL specification.
- Renamed **test type** value 'roundtrip' to 'validation'.

## Open questions
- Should we remove **test** from the property names? This prefix seems 
redundant in the context of this document but it may be helpful in other 
documentation that references test cases and other PURL data.

## Action items
- Create new PURL component level test files by extracting them from
`tests/spec/specification-test.json`
- Review and resolve the impact of changes to current PRs - most are listed
at: [Upgrade PURL test suite](https://github.com/orgs/package-url/projects/10)
- Review the impact of changes on current test cases and how to automatically
update existing test cases
- Contact maintainers of known PURL implementations (toolgrid) for feedback and
impact analysis
- Draft "How to create a PURL test case"

## Open items
The following proposed changes to the PURL test framework are not covered
by this draft:
- Defining a unique name or id for each test case (manual or generated)
- Moving test cases to one file per test case
- Adding the ABNF grammmar

## Not in scope
- This document does not provide specific guidance or instructions for creating
or using PURL test files. That will be the subject of future "How-to" 
documentation.


