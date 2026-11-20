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
valid form. The test suite also includes "optional" test cases which are
provided to help a PURL tool identify and possibly normalize or remediate
invalid PURL data.

## Terminology
Some key terminology for PURL tests is:

| Term            | Definition                                              |
|-----------------|---------------------------------------------------------|
| PURL component  | One of the 7 components of a PURL string  |
| PURL data       | Summary term for a PURL string or an object composed of PURL components |
| PURL Standard   | Refers to the content of ECMA-427                     |
| PURL tool       | A software program that includes functionality for building, parsing or validating PURL data |
| test case       | Is a single test example within a test file         |
| test file       | Is a set of test cases                              |
| test suite      | Is the entire set of current PURL test files        |

## Test files
Each PURL test file is a collection of test cases whose structure is defined
by the PURL test schema. The PURL test schema is not included in the  [ECMA-427 2nd edition](https://ecma-tc54.github.io/ECMA-427/) PURL Standard because it is
still under active development.

The current PURL test schema is located at: https://packageurl.org/purl-schemas/purl-test.schema-0.2.json.

The PURL test files are currently organized in two primary folders:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec):
  This folder contains JSON test files that are for the core specification and
  are not for a specific PURL `type`. This folder currently contains one test
  file: [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json).

  There may be separate test files for each PURL component in the future.
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types):
  This folder contains one JSON test file for each registered PURL `type` with
  the test file named `<purl-type>-test.json`. These tests should be focused on test cases that are specific to a PURL `type`, such as tests for the `namespace`
  or `qualifiers` components. PURL `type` test cases should not duplicate specification-level test cases.

The PURL specification does not mandate how a PURL tool natively reports
the success or failure of a test. Implementation languages that throw
exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL input that fails PURL `type`-specific
validation should result in different types or enum values.

*See the Test cases page for additional information about structure and format
of test cases.*