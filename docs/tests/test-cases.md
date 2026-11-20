---
id: test-cases
title: PURL test cases
sidebar_label: Test cases
hide_table_of_contents: false
---

# PURL test cases

## PURL test schema

The PURL test schema is specified with [JSON Schema Draft-07](https://json-schema.org/draft-07/draft-handrews-json-schema-01.html).

The current PURL test schema version is v0.2. You can use the following links
to view the JSON Schema file directly or view an Interactive HTML version created with [JSON Schema for Humans](https://github.com/coveooss/json-schema-for-humans).

- <a href="https://packageurl.org/purl-schemas/purl-test.schema-0.2.json" target="_blank">JSON Schema</a> `↗`
- <a href="/interactive_schemas/purl-test.schema-0.2.html" target="_blank">Interactive HTML</a> `↗`

## Test case structure
Each test case is in JSON format with following basic structure:

| **Property**     | **Format** | **Description**                     |
| ---------------- | ---------- | --------------------------------------------------------------------- |
| description      | string     |     |
| test_group       | string     | 'required' or 'recommended'         |
| test_type        | string     | 'build', 'parse', or 'validate'     |
| expected_failure | boolean    |                                     |
| expected_message | string     |                                     |
| input            | string     | A PURL string or an object of PURL components; not required to be in valid form. |
| expected_output  | string     | A PURL string or an object of decoded components; required to be in valid form.  |

See below for more details about each test case property.

## PURL test principles

### Test case granularity
Each test case is granular such that an expected failure condition covers only
one error. This means that a test case should only cover an error for a single
PURL component or a single parsing error related to separator characters. This
is necessary to keep test cases simple. It is not intended to constrain error
message handling implemented by a PURL tool.

### Test failure or success
Test cases should be balanced between examples of successes and failures. A
general rule is that one quarter to one third of the PURL test cases should
result in an `expected_failure` condition. This is important to provide a
realistic set of test cases.

### PURL 'type' test cases
Test cases for a PURL `type` should be focused on:
- Testing PURL component definitions that are specific to the PURL `type`,
  especially those that are related to the `namespace`, `name`, and
  `qualifiers` components.
- Illustrating common data patterns for the PURL `type` such as typical
  `name` or `version` patterns.

## Test case properties
This section provides a human-friendly explanation of each test case property
of the PURL test schema and guidance for how to define useful test cases at
the property level.

### description
The test case `description` should succinctly describe the test case scope
and purpose.

### test_group
There are two PURL `test_groups`:
- 'required': A test case to demonstrate conformance with ECMA-427 which means
  conformance with:
   - The Package-URL specification as documented in [ECMA-427 Clause 5](https://ecma-tc54.github.io/ECMA-427/#sec-purl-specification), and
   - The current set of registered PURL `type` definitions.
- 'recommended': A test case that is recommended to identify common errors
  in PURL data and how to report or normalize these errors in order to
  update the data to pass the 'required' tests. The use of 'recommended' test
  cases is optional for a PURL tool.

The terminology of 'required' vs 'recommended' matches the use of "shall" vs
"should" from Clause 2 of ECMA-427. A "shall" statement in ECMA-427 means
'required'; a "should" statement means 'recommended'.

### test_type
There are three PURL `test_types`:
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

## PURL test requirements









