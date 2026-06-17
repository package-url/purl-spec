# PURL test overview

The Package-URL (PURL) specification provides a JSON Schema for test
files to support language-neutral testing of PURL implementations. The 
objective for the PURL test schema and JSON test files is to enable tools to 
conform to the PURL specification for core functions such as:
- build a PURL string from a set of PURL components 
- parse a PURL string into a set of PURL components
- validate a PURL string

There are two distinct levels of test files in the test suite:
- Specification: These test files are based on the Core Specification which is 
Clause 5 of [ECMA-427 1st edition](https://ecma-tc54.github.io/ECMA-427/). 
The specification-level tests cover the canonical syntax for a PURL string and
for a set of PURL components. 
- PURL types: These test files are based on the PURL **type** definitions 
for the current set of registered PURL **types**. The structure of PURL 
**types** is defined in Clause 6 and ANNEX A (JSON Schema) of ECMA-427, but
the set of registered PURL **types** is dynamic as new PURL **types** are 
approved or existing PURL **types** are updated.  

## Test suite
The PURL test suite is intended to help a PURL implementation tool demonstrate
conformance with the PURL specification. The ultimate objective is to provide
clarity about whether a PURL string or set of PURL components is in canonical 
form which means the test case input conforms to ECMA-427. The test suite also 
includes "optional" test cases which are intended to help a PURL 
implementation tool identify and possibly remediate non-canonical PURL data.

## Terminology
Some key terminology used in this document is:

| Term        | Definition           |
|-------------|---------------------------------------------------------|
| PURL data   | Summary term for a PURL string, a PURL component or an object composed of PURL components |
| PURL tool   | A software program that includes functionality to build, parse or validate PURL data |
| test case   | a single test example within a *test file*              |
| test file   | a set of test cases                                     |
| test suite  | the entire set of PURL test files                       |

## Test files

Each PURL test file is a collection of test cases whose structure is defined
by the PURL test schema (a JSON Schema). The PURL test schema is not currently
included in the [ECMA-427 1st edition](https://ecma-tc54.github.io/ECMA-427/) 
PURL standard because it is still under active development.
The current PURL test schema is located at: https://packageurl.org/schemas/.

The PURL test files are organized in two primary subfolders:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec) 
This folder contains JSON test files that are for the core specification and 
not for a specific PURL type. 
  - [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json): This file contains a set of test cases that cover 
testing the validity of PURL strings including separators between PURL 
components.
  - There is a current proposal to add component-specific test files with the 
  naming convention: `<component-name>-test.json`
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types):
This folder contains one JSON test file for each registered PURL **type**. 
These tests are focused on test cases that are specific to a PURL type, such 
as those for the **namespace** or **qualifiers** components. PURL **type**
test cases should not duplicate specification- or component-level test cases.

## Test cases
The basic structure of a PURL **test case** is:
- `test_description`: string
- `test_level`: 'core'. 'type', or 'extra'
- `test_type`: 'build', 'parse', or 'validate'
- `test_input`: a PURL string or an object containing PURL components
- `test_result`: 'failure' or 'success'
- `test_output`: a PURL string or an object containing PURL components
- `test_message`: string

This structure is documented in the PURL test schema.

Each test case is granular such that an expected failure condition covers only 
one error. This means that a test case should only cover an error for a single
PURL component or a single parsing error related to separator characters. This
is necessary to keep test cases simple. It is not intended to constrain error 
message handling implemented by a PURL tool.

### Test description
The test description should describe the condition that is the subject of a 
test case. It should be as specific as possible.

### Test level
The **test level** property defines whether and how a test case is intended to 
demonstrate conformance with ECMA-427. 
- 'core': A test case that demonstrates conformance with the core Package-URL
specification (Clause 5 of ECMA-427).
- 'type': A test case that demonstrates conformance with the PURL **type**
definition (Clause 6 of ECMA-427) for a registered PURL **type**.
- 'extra': A test case that is useful for PURL tools, but is not required
for conformance.

### Test type
PURL test cases are organized according to three **test types** that map 
to typical implementation tool functionality - building, parsing, or 
validation. The three PURL **test types** defined in the PURL test schema are:
- 'build': A test case for the use case of building a canonical PURL output string 
from an input of decoded PURL components.
- 'parse': A test case for the use case of parsing a PURL input string and creating
 a set of decoded PURL components.
- `validate': A test case for the use case of validating that a PURL string input
 complies with the core specification (ECMA-427) and the rules for its PURL 
 **type**. This **test type** was previously named 'roundtrip'.

### Test input
**Test input** may be a PURL string or an object containing PURL components.
**Test input** does not need to be in canonical form, but a test case with 
non-canonical input shall fail when **test conformance** is true unless 
there is a normalization exception in ECMA-427.

### Test result
The **test result** shall be 'failure' or 'success'.
- If a **test result** is 'failure', then a **test message** explaining
the failure is required.
- If a **test result** is 'success', then a **test message** is optional.

### Test output
**Test output** is either a canonical PURL string or an object containing
a set of decoded PURL components.
- If a **test result** is 'failure', then the **test output** is null.
- If a **test result** is "success', then the **test output** is required.

### Test message
A **test message** is a string that provides information about the **test 
result**.
- If a **test result** is 'failure', then the **test message** is required
and should explain the reason for the 'failure'.
- If a **test result** is "success', then the **test message** is optional. The 
typical reason for a **test message** in this case is to provide a warning or 
other information about the **test_input**. Some examples are:
   - ECMA-427 mandates normalization of some **test input**. In this case, the
messsage alerts a PURL tool that the **test input** was not in canonical
form even though the **test result** was 'success'.
   - The **namespace** value from the **test input** is syntactically correct 
but is not included in the list of **namespace** values enumerated in the 
corresponding PURL **type** definition.
   - A **key** value in **qualifiers** input is syntactically correct but is 
not included in the list of **qualifiers** values enumerated in the 
corresponding PURL **type** definition.

## Error handling and messages by PURL tools
The PURL specification does not mandate how a PURL tool natively reports 
the success or failure of a test. Implementation languages that throw 
exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL input that fails PURL **type**-specific 
validation should result in different types or enum values.

## Summary of changes from PURL test schema v0.1
- Added prefix of "test_" to all property names for consistency
- Replaced `test group` with `test_level`
- Renamed `test type` value 'roundtrip' to 'validate'
- Renamed `expected_output` to `test_output`
- Renamed `expected_failure` to `test_result` and redefined from a boolean to
a choice of 'success' or 'failure'
- Renamed `expected_failure_reason` to `test_message` and redefined it to 
allow/encourage the use of a **test message** for selected successful test 
cases

## Open items

### Open questions
- How do we handle testing related to unregistered PURL **types**?
   - This condition is logically a specification level test for the PURL 
   **type** component to check whether a PURL **type** is present in 
   `purl-types-index.json` at the time of the test.
   - The test case should return a **test message** that the **test input**
   contains an unregistered PURL **type**

### Action items
- Create new PURL component level test files by extracting them from
`tests/spec/specification-test.json`
- Review and resolve the impact of changes to current PRs - most are listed
at: [Upgrade PURL test suite](https://github.com/orgs/package-url/projects/10)
- Contact maintainers of known PURL implementations (toolgrid) for feedback 
and impact analysis
- Plan for automated migration of existing test cases to the new schema
- Draft "How to create a PURL test case"

### Not in scope
The following proposed changes to the PURL test framework are not covered
by this draft:
- Adding an ABNF grammmar
- Defining a unique name for each test case (manual or generated)
- Moving test cases to one file per test case
- This document does not provide specific guidance or instructions for creating
or using PURL test files. That will be the subject of future "How-to" 
documentation.

