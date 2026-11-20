---
id: test-cases
title: PURL test cases
sidebar_label: Test cases
hide_table_of_contents: false
---

# PURL test cases

## Test case structure
Each test case is in JSON format with following basic structure:

| **Property**     | **Format** | **Description**                     |
| ---------------- | ---------- | --------------------------------------------------------------------- |
| description      | string     |     |
| test_group       | string     | 'required' or 'recommended'          |
| test_type        | string     | 'build', 'parse', or 'validate'      |
| expected_failure | boolean    |                                     |
| expected_message | string     |                                     |
| input            | string     | A PURL string or an object of PURL components; not required to be in valid form. |
| expected_output  | string     | A PURL string or an object of decoded components; required to be in valid form.  |

See below for more details about each test case property.

### Testing Principles

Each test case is granular such that an expected failure condition covers only
one error. This means that a test case should only cover an error for a single
PURL component or a single parsing error related to separator characters. This
is necessary to keep test cases simple. It is not intended to constrain error
message handling implemented by a PURL tool.

## Test case properties

### description
The test case `description` should succinctly describe the test case scope
and purpose.

### test_group
There are two PURL `test groups`:
- 'required': A test case to demonstrate conformance with ECMA-427 which means
  conformance with:
   - The Package-URL specification as documented in [ECMA-427 Clause 5](https://ecma-tc54.github.io/ECMA-427/#sec-purl-specification), and
   - The current set of registered PURL `type` definitions.
- 'recommended': A test case that is recommended to identify common problems
  in PURL data and how to remediate or normalize them in order to pass the
  'required' tests. The use of 'recommended' test cases is always optional.

The terminology of 'required' vs 'recommended' matches the use of "shall" vs
"should" from Clause 2 of ECMA-427. A "shall" statement in ECMA-427 means
'required'; a "should" statement means 'recommended'.

### test_type
There are three PURL `test types`:
- 'build': A test case for the function of building a valid PURL output
  string from an input of decoded PURL components. See also [How to build a PURL](https://www.packageurl.org/docs/purl/how-to-build).
- 'parse': A test case for the function of parsing a PURL input string into
  a set of decoded PURL components. See also [How to parse a PURL](https://www.packageurl.org/docs/purl/how-to-parse).
- 'validate': A test case for the function of validating a PURL input
  string. The input is a PURL string (in valid form or not) and the output
  is a PURL string in valid form.

### input
- `input` may be a PURL string or an object containing PURL components.
- `input` does not need to be in valid form, but a test case with
  non-valid input shall fail if the `test_group` is 'required' unless
  there is a "shall" normalization rule in ECMA-427 or in an applicable
  `type` definition.

### expected_output
`expected output` is either a valid PURL string or an object containing
a set of decoded PURL components.
- If `expected_failure` is true, then `expected_output` is null.
- If `expected_failure` is false, then `expected_output` is required.

### expected_failure
`expected_failure` is true if the test `input` is expected to fail
according to the function defined by the `test_type` ('build', 'parse' or
'validate').

### expected_message
`expected-message` documents either the reason that a test case results in a
failure or provides information about the result of the test case. It should
be descriptive without duplicating the test case `description`.
- If `expected_failure` is true, then `expected_message` is
  required.
- If `expected_failure` is false, then `expected_message` is not required,
  but is recommended in some cases. These cases include:
  - When the PURL specification requires normalization of an `input` for
    a 'parse' or 'validate' `test-type`. It is important in these cases to
    report that the `input` was not in valid form even though the test case
    did not fail.
  - When a "should" normalization from ECMA-427 or an applicable `type`
    definition is applied in a test case.
  - When an `input`contains an unregistered PURL `type`. It is important
    to document that a PURL `type` is not registered because this means that
    the PURL `type` is effectively unknown across the tools and databases
    that implement PURL.

##









