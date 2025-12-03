## Tests

>This is a draft document to replace the current tests.md file. The scope of 
tests.md is to provide an overall description of PURL tests in the context of 
the PURL test schema. Its scope does not cover how to create a test file or 
how to use the test files for a PURL tool.

>The primary text is a provisional draft based on the existing v0.1 schema and 
recent proposed changes. There are Discussion sections to track key notes and
questions separately from the current draft text.

>Note that this document uses Ecma standard style conventions for consistency 
with the PURL specification language in the PURL 1st edition standard, e.g., 
bolding key words instead of using code snippet notation (back-ticks).

The Package-URL (PURL) specification provides a JSON Schema for test
files to support language-neutral testing of PURL implementations. The 
objective for the PURL test schema and JSON test files is to enable tools to 
conform to the PURL specification for core functions such as:
- build a canonical PURL string from a set of PURL components 
- parse a PURL string into a set of PURL components
- validate a PURL string and provide messages about the correctness of 
the input PURL
- analyze a PURL string and recover from small errors to produce a canonical
PURL when possible

The current JSON schema for test files is available at: [`purl-spec/schemas/purl-test.schema-0.1.json`](https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema-1.0.json).

The test files are available at:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec): 
This folder contains JSON test files that are not for a specific PURL type.
  - [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json)
   - This file contains an array of test 
  cases that primarily cover testing the validity of individual PURL 
  components or separators between a pair of PURL components.
  - *component-test.json*: These are test files for a specific PURL component.
 See [PR 738](https://github.com/package-url/purl-spec/pull/738) which adds 
 `tests/spec/qualifiers.json`. 
- [`purl-spec/tests/types/`](https://github.com/package-url/purl-spec/tree/main/tests/types):
 This folder contains one JSON test file for each 
registered PURL type. These tests should be focused on test cases that are
specific to a PURL type, such as those for namespace or qualifiers.

Any PURL implementation tool is expected to canonicalize a PURL string during 
a parsing or building operation.

>*Discussion for PURL test files*
- After PR 738 is approved/merged we will probably want to create test files
for each PURL component by moving component-specific test cases from
`specification-test.json` to the new test files.
- [Issue 743](https://github.com/package-url/purl-spec/issues/743) proposes 
that the current test files should be re-organized so that:
  - Everything based on core spec definition is done in the spec tests. all the
   canonicalization, parsing, building, validation, ...
  - Type tests only test things that are based on the type definition. Type 
tests don't test core spec again.

> *End of test file discussion*

Two key properties in the PURL test JSON schema are:
- **Test group**
- **Test type**

The focus of this document is to clearly define these properties/concepts.

### Test groups

There are two PURL test groups defined in the current v0.1 test schema:
- **base**: "Test group for base conformance tests for PURL building and 
parsing."
- **advanced**: "Test group for advanced tests to support flexible PURL 
building and parsing."

There are examples of **base** and **advanced** test cases across the various
test files but there is no clear pattern likely because the current schema 
definitions are not clear. A proposed new definition is:
- **base**: "Tests that are required for conformance with the PURL 
specification. Base tests are pass/fail."
- **advanced**: Tests that are more permissive (lenient?) than base tests. 
Advanced tests may provide severity messages (new validation test type) or 
correct errors from test input (or both?)

>*Discussion for test groups*
- What is the intersection of test groups with test types?
  - Are **build** or **parse** test types that return only pass/fail always in 
  the **base** test group?
   - Are **build** or **parse** test types that remediate an error always in 
   the **advanced** test group?
  - Are **roundtrip** tests that return only pass/fail always in the **base** 
  test group? _pombredanne - not always_
  - Are **roundtrip** tests that remediate an error always in the **advanced**
   test group? _pombredanne - yes_
   - Are **validation** tests always in the **advanced** test group?
   _pombrdeanne - yes_

- Is there a better name for the the test groups? Strict and permissive? 
Or strict and lenient?
- _pombredanne prefers strict/permissive_
- Would it be better to have separate test files for base and advanced test 
groups? This would add one level of depth to the directory structure, but it 
could have the benefit of making it much simpler for a tool to work with base 
tests required for conformance instead of parsing every test file to find
the base tests.
- _pombredanne supports separating test files by test group_


> *End of test group discussion*

### Test types

There are three PURL test types defined in the current v0.1 test schema:

- **build**: "A PURL building test from decoded components to a canonical PURL
 string.".
- **parse**: "A PURL parsing test from a canonical PURL string to decoded 
components.".
- **roundtrip**: "A PURL roundtrip test, parsing then building back a PURL 
from a canonical string input."

>*Discussion and proposed changes for test types*

The current definition for the **roundtrip** test type does not make sense 
because it requires a canonical string input and output. The proposed new 
schema definitions for test types are:

- **build**: A test to build a canonical PURL output string from an input of 
decoded PURL components."
- **parse**: A test to parse decoded components from a PURL input string."
- **roundtrip**: A test to produce a canonical PURL output string from an 
input PURL string.

For the **build** and **parse** test types there is no normative change here -
 just an attempt to improve the text.

#### New validation test type

There is a proposed new **validation** test type from [Issue 692](https://github.com/package-url/purl-spec/issues/692) 
and [PR 614](https://github.com/package-url/purl-spec/pull/614). 
The proposed definition is: "A PURL validation test, checking if a PURL 
follows all the rules for a particular ecosystem."
- A better definition (editorially) would be: "A test to validate that an 
input PURL string complies with the rules for its PURL type." 
- _pombredanne approves better definition_
- The new PURL type test cases in PR 614 are a mixture of **base** and
**advanced** test groups, but there is no obvious pattern for the difference.
- _pombredanne - roundtrip tests are advanced when input is not canonical_

#### Validation test messages:

PR 614 adds a **purl_validation_message** to the test schema with possible 
validation severity values of "info", "warning" or "error". There is no 
specific definition of the difference between info and warning messages, but 
the examples in PURL type test case updates from PR 614 follow the patterns:
- Warning messages for cases where a PURL component does not follow rules 
related to case sensitivity.
- Info messages for cases of an unregistered namespace or qualifier - see also
Issues [690](https://github.com/package-url/purl-spec/issues/690) and 
[710](https://github.com/package-url/purl-spec/issues/710).

Validation message notes:
- The proposed change for validation messages allows multiple messages from a 
single test case.
- There is no message returned for a successful validation. _pombredanne - we
can add one_
- We will need to clearly define the difference between an info message and a 
warning message or reduce the set to warning and error messages.
- The messages as shown in the test case examples from PR 614 are clear and 
helpful as presented, but it is not clear if/how some PURL tools will be able 
to handle such specific messages. See also the following Error 
message discussion section.

>*End of test type discussion*

>*Error message discussion*

The current PURL specification documentation does not contain guidance
or instructions for using PURL test files. This document is not intended to 
provide that guidance. We will need to create new How-to documentation for 
that, but we need a basic definition of error messages and their intended use 
in PURL tools to complete the updates to the test schema.

### Error handling

The current error handling behaviour for all test cases is based on two
properties from the PURL test schema:
- `expected_failure`
  - description: "true if this test input is expected to fail to be 
processed."
  - type: boolean
  - default: 'false'
- `expected_failure_reason`: "The reason why this test is is expected to fail 
if expected_failure is true."
   - default: null

In the case of a test case failure the `expected_output` is `null`.

#### Validation messages

As discussed above the **validation** test type introduces a set of 
validation messages for that test type, but these messages might also be 
useful  for other test types. For example:

The first test case in [`tests/types/pypi.test.json`](https://github.com/package-url/purl-spec/blob/main/tests/types/pypi-test.json)
 is an example of an **advanced** **roundtrip** test. The test case data is:

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
 
 In this case it would be helpful for the test case to provide a ("warning" or 
 "info"?) message explaining the correction, such as:  
    - The pkg component must be lowercased.  
    - The name component must be lowercased.  
    - Runs of consecutive dash -, underscore _, or dot . characters must be 
    replaced with a single dash -.  

Without a message the user will never know that there was a correction needed 
for the input PURL string.
- _pombredanne agrees that a message is warranted here_

#### Error message handling by PURL tools

The current v0.1 test schema does not include any specific properties for 
error messages. Most of the test case examples with an expected 
failure are in the file [`test/spec/specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json). Based on 
these examples a tool could usually derive an error message from the 
description, but the message would be indirect. For example from the first 
test case in `test/spec/specification-test.json` we 
have:

`"description": "a scheme is always required"`.  
`"expected_output": null,`  
`"expected_failure": true,`  
`"expected_failure_reason": "Should fail to parse a PURL from invalid purl 
input"`

If a tool wants to provide a specific error message it would apparently need 
to
 construct a message by combining information from the `description` and the 
 `expected_failure_reason` like: "Invalid PURL input - the PURL scheme is 
 missing." The solution may be to update `expected_failure_reason` to be a 
 more
specific error message.

There is also an important perspective from [PR 747](https://github.com/package-url/purl-spec/pull/747)
regarding the expected use of PURL test messages by PURL tools.

*"I don't think it is necessary or beneficial for PURL to specify error 
message strings to be produced by implementations. It seems 
potentially reasonable to have an explanation of why the test fails, but 
specifying the errors produced in this way prohibits or discourages 
implementations from handling errors in better or more customary ways. 
Implementation languages that throw exceptions or return typed 
results/outcomes should return typed errors, ie a syntactically invalid PURL 
and a PURL that fails package-type-specific validation should result in 
different types or enum values such that the consuming software doesn't need 
to analyze a string to determine what's going on. It's possible to specify 
that there is a conversion from however the implementation specifies errors 
into a string, but this seems more useful for the purposes of this test case 
than in actual usage.*

- _pombredanne: We are not expecting tools to report the exact same message, 
just to report a problem of the same type IMHO_

>*End of error message discussion*
