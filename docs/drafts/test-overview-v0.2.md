# Package-URL test overview
The Package-URL (PURL) specification provides test files to support 
language-neutral testing of PURL implementations. The objectives for the PURL 
test files are to:
- Enable tools to demonstrate conformance with the PURL specification as
defined in [ECMA-427 1st Edition](https://ecma-tc54.github.io/ECMA-427/) or 
in registered PURL **type** definitions
- Help tools identify and fix common problems in PURL data

The structure of test cases used in PURL test files is defined in a JSON 
schema that is available at: https://packageurl.org/schemas/purl-test.schema-0.1.json. 
This schema is not included in ECMA-427 1st Edition.

## Conformance
Since the primary goal for the PURL test suite is to help PURL tools achieve
and demonstrate conformance with the PURL specification, it is important to 
state what we mean by conformance. Conformance is defined in [ECMA-427 Clause 
2](https://ecma-tc54.github.io/ECMA-427/#sec-conformance). The summary is: "A 
conforming implementation of Package-URL (PURL) shall fully implement and 
support all elements defined within this Standard, including the syntax, 
components, and semantic requirements for constructing and interpreting valid 
PURLs." 

The reference above to "this Standard" means the content of ECMA-427 which is
the core PURL specification, but only part of the overall PURL specification.
The content of the PURL Standard is documented in two clauses of ECMA-427:
- [5 Package-URL specification](https://ecma-tc54.github.io/ECMA-427/#sec-purl-specification) 
which covers the structure of a PURL and:
   - Permitted and separator characters,
   - Character encoding and case folding, and
   - Rules for each PURL component.
- [6 Package-URL Type Definition Schema](https://ecma-tc54.github.io/ECMA-427/#sec-purl-type-schema) which covers the definition of a PURL **type** but not
the data for each PURL **type** because that data is evolving as new PURL 
**types** are registered (see Terminology below). Conformance with the PURL 
Standard requires conformance with the currently registered PURL **type** 
definitions.

Other PURL documentation such as "How to build a PURL string from its 
components" or "How to parse a PURL string into its components" is important 
but not part of the PURL Standard for conformance purposes.

Some common words have a very specific meaning for ECMA-427 conformance:
- "canonical form" means a PURL string or a set of PURL components in the 
format that matches the Standard for a string or components respectively
- "normalization" means the process of structuring, standardizing, or 
converting data to conform to a standard format - i.e. canonical form.
- "shall" indicates a requirement (Ecma & ISO definition)
- "should" indicates a recommendation (Ecma & ISO definition)

The PURL Standard requires that:
- A PURL string is in canonical form or
- Each PURL component in a set (object) conforms to the PURL standard.

In the testing context, there are no exceptions to canonical form for the 
output of a PURL tool, but there are some exceptions for the input where the 
Standard requires a PURL tool to normalize data elements in order to produce a 
canonical test output. The exceptions are:
- At the core specification level (Clause 5), ECMA-427 says: "PURL parsers 
shall accept URLs where the scheme and colon ':' are followed by one or more 
slash '/' characters, such as 'pkg://', and shall ignore and remove all such '/' 
characters." 

   Note that other statements in Clause 5 that: "All leading and 
trailing  slashes '/' are not significant and should be stripped in the 
canonical form." are recommendations ("should"), not requirements ("shall").

- At the PURL **type** level (Clause 6), some PURL **type** definitions 
include normalization requirements. If applicable these are documented in
two properties:
   - `case_sensitive`: "true if this PURL component is case sensitive. If 
false, the canonical form shall be lowercased."
   - `normalization_requirements`: "List of rules to normalize this component 
for this PURL type. These are plain text, unstructured rules as some require 
programming and cannot be enforced only with a schema. Tools are expected to
apply these rules programmatically." 

   The definition of the **name** component of the 'pypi' PURL **type** is an
example of both normalization requirements.

## Terminology
Some key terminology used in this document is:

| Term            | Definition                                              |
|-----------------|---------------------------------------------------------|
| PURL component  | One of the 7 components of the Package-URL standard   |
| PURL data       | Summary term for a PURL string or an object composed of PURL components |
| PURL Standard   | Refers to the content of ECMA-427                     |
| PURL tool       | A software program that includes functionality for building, parsing or validating  *PURL data* |
| PURL type registration | Means that there is a PURL type definition file (JSON) in the [`purl-spec/types`](https://github.com/package-url/purl-spec/tree/main/types) folder  |
| test case       | Is a single test example within a *test file*         |
| test file       | Is a set of *test cases*                              | 
| test suite      | Is the entire set of current PURL *test files*        |

## Test suite
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
PURL standard because it is still under active development.
The current PURL test schema is located at: https://packageurl.org/schemas/.

The PURL test files are currently organized in two primary subfolders:
- [`purl-spec/tests/spec/`](https://github.com/package-url/purl-spec/tree/main/tests/spec) 
This folder contains JSON test files that are for the core specification and 
not for a specific PURL **type**. This folder currently contains one test 
file: [`specification-test.json`](https://github.com/package-url/purl-spec/blob/main/tests/spec/specification-test.json). There may separate test files for each PURL 
component in the future.
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
  - When an **input** contains an unregistered PURL **type**. It is important to
 document that a PURL **type** is not registered because this means that the 
 PURL **type** is effectively unknown across the tools and databases that 
 implement PURL.

The PURL specification does not mandate how a PURL tool natively reports 
the success or failure of a test. Implementation languages that throw 
exceptions or return typed results should return typed errors, i.e.
a syntactically invalid PURL and a PURL input that fails PURL **type**-specific 
validation should result in different types or enum values.

## Changes in PURL test schema v0.2 

### Test groups
**Change**: Renamed
- 'base' to 'required'
- 'advanced' to 'recommended'

This change removes the ambiguity of the **test group** names from the v0.1
PURL test schema by using names that map to the terminology from the 
Conformance Clause (2) of ECMA-427.

### Test messages
**Change**: Renamed **expected_failure_reason** to **expected message** 

The terminology of the v0.1 PURL test schema did not provide a
way to provide a test case message in two important use cases:
- When the PURL specification requires normalization of an **input**. This 
applies to the 'parse' and 'validate' **test types**. It seems important
 to document that the input was not in canonical form even though the test 
 passed.
- When an **input** contains an unregistered PURL **type**. This applies to
all three **test types**. It seems important to document that a PURL **type** 
is not registered because this means that the PURL **type** is effectively
unknown across the tools and databases that implement PURL.

### Test types
**Change**: Renamed **test type** 'roundtrip' to 'validate'.

The general meaning of a "roundtrip" test was to confirm that a PURL 
tool can parse a canonical PURL into its components and then build a canonical
PURL from those components - these functions are also known as deserialization
and serialization. The former 'roundtrip' **test type** did not provide much 
value because the output and are required to be the same - a PURL tool can 
easily test this "roundtrip" behavior without a test case.

The 'validate' **test type** does not require the input PURL string to be in 
canonical form. There is a high degree of similarity between the 'parse'
and 'validate' **test types** in terms of the functions a PURL tool performs.
The key difference is that the **expected output** from a 'parse' test case is
an object composed of decoded PURL components and the **expected output**
from a 'validate' test case is a PURL string.









