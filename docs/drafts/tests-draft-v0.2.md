# PURL test overview

The Package-URL (PURL) specification provides a JSON Schema for test
files to support language-neutral testing of PURL implementations. The 
objective for the PURL test schema and JSON test files is to enable tools to 
conform to the PURL specification for core functions such as:
- build a canonical PURL string from a set of PURL components 
- parse a PURL string into a set of PURL components
- validate a PURL string and provide messages about the correctness of 
the input PURL

The JSON schema for test files *will be* available at: `purl-spec/schemas/purl-test.schema-0.2.json`

The PURL test files are available at:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec) 
This folder contains JSON test files that are not for a specific PURL type. 
The specification-level tests are tests required to demonstrate conformance 
with [ECMA-427](https://ecma-tc54.github.io/ECMA-427/); also known as the 
'base' **test group**.
  - [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json) This file contains a set of test cases that cover 
testing the validity of PURL strings including separators between PURL 
components.
  - `type-test.json` This file contains tests for the PURL **type** component.
  - `namespace-test.json` This file contains tests for the PURL **namespace** 
component.
  - `version-test.json` This file contains tests for the PURL **name** 
  component.
  - `qualifiers-test.json` This file contains tests for the PURL **qualifiers** 
component.
  - `subpath-test.json` This file contains tests for the PURL **subpath** 
component.
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types)
This folder contains one JSON test file for each registered PURL type. These 
tests are focused on test cases that are specific to a PURL type, such 
as those for the **namespace** or **qualifiers** components. PURL type
test cases should not duplicate specification or component level test cases.

This document does not provide specific guidance or instructions for using 
PURL test files. That will be the subject of future "How-to" 
documentation.

Two key properties in the PURL test JSON schema are:
- `test_group`: to distinguish between test cases that demonstrate
conformance with ECMA-427 and registered PURL **type** definitions versus other
test cases that provide additional information about how to build, parse, or
validate PURL data
- `test_type`: to organize test cases according to implementation tool 
functionality - building, parsing, or validation

## Test groups

There are two PURL **test groups** defined in the PURL test schema:
- 'base': for conformance test cases. These are pass/fail tests. 
A PURL implementation tool shall pass all 'base' tests to demonstrate 
conformance with ECMA-427 and registered PURL **type** definitions.
- 'advanced': test cases that are intended to show a PURL implementation 
tool how to correct a build, parse or validation error or anomaly. 

## Test types

There are three PURL **test types** defined in the PURL test schema:
- 'build': A test to build a canonical PURL output string from an input of 
decoded PURL components.
- 'parse': A test to parse a PURL input string and create a set of decoded
PURL components.
- `validation': A test to validate that a PURL string input complies with 
the specification and the rules for its PURL **type**. 

## Test case output
The PURL specification does not mandate how a PURL implementation tool 
natively reports the success or failure of a test. Implementation languages 
that throw exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL that fails PURL **type**-specific 
validation should result in different types or enum values.

The PURL test specification provides two levels of error handling and test 
result messages.

### Base test group error handling and messages
Test cases in the 'base' **test group** are pass/fail. The error handling for 
test cases in the 'base' **test group** is based on two properties from the 
PURL test schema:
- `expected_failure`
  - description: "true if this test input is expected to fail to be 
processed."
  - type: boolean
  - default: 'false'
- `expected_failure_reason`: "The reason why this test is is expected to fail 
if expected_failure is true."
   - default: 'null'

In the case of a test case failure the test case `expected_output` is 'null'.

### Advanced test group error handling and messages
Test cases in the 'advanced' **test group** may be pass/fail. Most should 
provide a validation message. If a test case provides corrected output it 
shall at a minimum also provide a validation message that explains the 
correction.

### Validation messages
There are 3 levels of **validation message**:
- 'info': An 'info' message means that there is some anomaly in the test 
input that is not an error. A common example is the be the presence of a 
**namespace** or **qualifiers** value that is not a registered for a PURL **type**.
- 'warning': A 'warning' message means some of the test input is incorrect, 
but that it can be corrected with information from the PURL **type** 
definition. An example is correcting case sensitivity.
- 'error': An 'error' message means that the test input does not provide 
enough information to produce a canonical PURL or a set of canonical PURL
components (for a 'parse' **test type**).

A test case can return more than one **validation message**. There is no 
message for success because that is handled by `expected_failure`='false' and
`expected_failure_reason`='null'.

### Test case examples

#### Validation message example

The first test case in the current [`tests/types/pypi.test.json`](https://github.com/package-url/purl-spec/blob/main/tests/types/pypi-test.json) is an example of 
an 'advanced' 'round-trip' test case. The data are:

```
"description": "pypi names have special rules and not case sensitive. 
Roundtrip  an input purl to canonical.",  
"test_group": "advanced",  
"test_type": "roundtrip",  
"input": "pkg:PYPI/Django_package@1.11.1.dev1",    
"expected_output": "pkg:pypi/django-package@1.11.1.dev1",  
"expected_failure": false,  
"expected_failure_reason": null
```  
In this case the **validation message** test output should include three 
'warning' messages:
  - "The pkg component must be lowercased."  
  - "The name component must be lowercased."  
  - "Runs of consecutive dash -, underscore _, or dot . characters must be 
replaced with a single dash -."  

## Summary of changes from PURL test schema v0.1
- Rename `expected_failure_reason` to `expected_message` so that a message can 
be provided for any test case, not only expected failures
- Implement `expected_message` as an object with 2 properties: severity 
(string with enum) and message (string)




