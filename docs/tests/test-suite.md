---
id: test-suite
title: PURL test suite
sidebar_label: Test suite
hide_table_of_contents: false
---

# PURL test suite
The PURL test suite is intended to help a PURL implementation tool demonstrate
conformance with the PURL specification. The primary objective is to provide
clarity about whether a PURL string or a set of PURL components is in 
canonical form. The test suite also includes "optional" test cases which are 
provided to help a PURL tool identify and possibly normalize or remediate 
non-canonical PURL data.

## Test files
Each PURL test file is a collection of test cases whose structure is defined
by the PURL test schema. The PURL test schema is not currently
included in the [ECMA-427 1st edition](https://ecma-tc54.github.io/ECMA-427/) 
PURL Standard because it is still under active development.
The current PURL test schema is located at: https://packageurl.org/schemas/.

The PURL test files are currently organized in two primary subfolders:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec) 
  This folder contains JSON test files that are for the core specification and 
  not for a specific PURL **type**. This folder currently contains one test 
  file: [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json). 
  There may separate test files for each PURL component in the future.
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types):
  This folder contains one JSON test file for each registered PURL **type**. 
  These tests are focused on test cases that are specific to a PURL type, such 
  as those for the **namespace** or **qualifiers** components. PURL **type**
  test cases should not duplicate specification-level test cases.

## Test cases
The basic structure of a PURL **test case** is:
- `description`: string
- `test_group`: 'required' or 'recommended'
- `test_type`: 'build', 'parse', or 'validate'
- `input`: A PURL string or an object of PURL components that is the test case
  input. The "input" is not required to be in canonical form.
- `expected_output`: A PURL string or a set of decoded components (canonical 
  form) that is the test case output.
- `expected_failure`: boolean
- `expected_message`: string

Each test case is granular such that an expected failure condition covers only 
one error. This means that a test case should only cover an error for a single
PURL component or a single parsing error related to separator characters. This
is necessary to keep test cases simple. It is not intended to constrain error 
message handling implemented by a PURL tool.

### description
The test case **description** should succinctly describe the test case scope 
and purpose.

### test_group
There are two PURL **test groups**:
- 'required': A test case to demonstrate conformance with ECMA-427 which means 
  conformance with:
   - The Package-URL specification as documented in [ECMA-427 Clause 5](https://ecma-tc54.github.io/ECMA-427/#sec-purl-specification), and
   - The current set of Registered PURL **type** definitions.
- 'recommended': A test case that is recommended to identify common problems 
  in PURL data and how to remediate or normalize them in order to pass the 
  'required' tests. The use of 'recommended' test cases is always optional.

The terminology of 'required' vs 'recommended' matches the use of "shall" vs 
"should" from the Conformance section above and Clause 2 of ECMA-427. A "shall"
statement in ECMA-427 means 'required'; a "should" statement means 
'recommended'.

### test_type
There are three PURL **test types**:
- 'build': A test case for the function of building a canonical PURL output 
  string from an input of decoded PURL components. See also [`/docs/how-to-build.md`](https://github.com/package-url/purl-spec/blob/main/docs/how-to-build.md).
- 'parse': A test case for the function of parsing a PURL input string into 
  a set of decoded PURL components. See also [`/docs/how-to-parse.md`](https://github.com/package-url/purl-spec/blob/main/docs/how-to-parse.md).
- 'validate': A test case for the function of validating a PURL input
  string. The input is a PURL string (in canonical form or not) and the output
  is a PURL string in canonical form.

### input
- **input** may be a PURL string or an object containing PURL components.
- **input** does not need to be in canonical form, but a test case with 
  non-canonical input shall fail when the **test group** is 'required' unless 
  there is a normalization exception in ECMA-427.

### expected_output
**expected output** is either a canonical PURL string or an object containing
a set of decoded PURL components.
- If **expected_failure** is true, then **expected output** is null.
- If **expected failure** is false, then **expected output** is required.

### expected_failure
**expected failure** is true if the test **input** is expected to fail 
according to the function defined by the **test type** ('build' 'parse' or
'validate').

### expected_message
**expected message** either documents the reason that a test case results in a 
failure or provides information about the result of the test case. It should 
be descriptive without duplicating the test case **description**.
- If **expected failure** is true, then **expected message** is 
  required.
- If **expected failure** is false, then **expected message** is not required, 
  but is recommended in some cases. These cases include:
  - When the PURL specification requires normalization of an **input** for 
    a 'parse' or 'validate' **test type**. It is important in these cases to
    document that the **input** was not in canonical form even though the test 
    passed.
  - When an **input** contains an unregistered PURL **type**. It is important 
    to document that a PURL **type** is not registered because this means that 
    the PURL **type** is effectively unknown across the tools and databases 
    that implement PURL.

The PURL specification does not mandate how a PURL tool natively reports 
the success or failure of a test. Implementation languages that throw 
exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL input that fails PURL **type**-specific 
validation should result in different types or enum values.