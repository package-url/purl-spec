---
id: test-overview
title: PURL test overview
sidebar_label: Test overview
hide_table_of_contents: false
---

# Package-URL test overview
The Package-URL (PURL) specification provides test files to support
language-neutral testing of PURL implementations. The objectives for the PURL
test files are to:
- Enable tools to demonstrate conformance with the PURL specification as
  defined in [ECMA-427 2nd Edition](https://ecma-tc54.github.io/ECMA-427/)
  or in registered PURL `type` definitions.
- Help tools identify and fix common problems in PURL data.

The structure of test cases used in PURL test files is defined in a JSON
schema that is available at: https://packageurl.org/purl-schemas/purl-test.schema-0.2.json.
This schema is not currently included in ECMA-427 for PURL.

## ECMA-427
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
The primary content of the PURL Standard is documented in two clauses of
ECMA-427:
- [5 Package-URL specification](https://ecma-tc54.github.io/ECMA-427/#sec-purl-specification)
which covers the structure of a PURL and:
   - Permitted and separator characters,
   - Character encoding and case folding, and
   - Rules for each PURL component.
- [6 Package-URL Type Definition Schema](https://ecma-tc54.github.io/ECMA-427/sec-purl-type-schema)
  which covers the definition of a PURL `type` but not the data for each
  PURL `type` because that data is evolving as new PURL `types` are
  registered (see Terminology below). Conformance with the PURL Standard
  requires conformance with the currently registered PURL `type` definitions.

Other PURL documentation such as "How to build a PURL" or "How to parse a
PURL" is part of the specification, but but not part of the PURL Standard for conformance purposes.

### Terminology
Some common words have a very specific meaning for ECMA-427 conformance:
- "valid form" means a PURL string or a set of PURL components in the
  format that matches the Standard for a string or components respectively
- "normalization" means the process of structuring, standardizing, or
  converting data to conform to a standard format
- "shall" indicates a requirement (Ecma & ISO definition)
- "should" indicates a recommendation (Ecma & ISO definition)

### Valid form
The PURL Standard requires that:
- A PURL string is in valid form or
- Each PURL component in a set (object) in valid form.

In the testing context, there are no exceptions to valid form for the
output of a PURL tool, but there are some exceptions for the input where the
Standard requires a PURL tool to normalize data elements in order to produce a
valid test output. The exceptions are:
- At the core specification level (Clause 5), ECMA-427 says: "PURL parsers
  shall accept URLs where the scheme and colon ':' are followed by one or more
  slash '/' characters, such as 'pkg://', and shall ignore and remove all such
  '/' characters."

   Note that other statements in Clause 5 that: "All leading and
   trailing  slashes '/' are not significant and should be stripped in the
   valid form." are recommendations ("should"), not requirements ("shall").

- At the PURL `type` level (Clause 6), some PURL `type` definitions
  include normalization requirements. If applicable these are documented in
  two properties:
   - `case_sensitive`: "true if this PURL component is case sensitive. If
     false, the valid form shall be lowercase."
   - `normalization_requirements`: "List of rules to normalize this component
      for this PURL type. These are plain text, unstructured rules as some
      require programming and cannot be enforced only with a schema. Tools are
      expected to apply these rules programmatically."

   The definition of the `name` component of the 'pypi' PURL `type` is an
   example of both normalization requirements.

## PURL test schema

The PURL test schema defines the structure of a PURL test file which contains
one or more test cases. It is a JSON schema and the current version is v0.2.
You can use the following links to view the JSON Schema file directly or view
an Interactive HTML version created with [JSON Schema for Humans](https://github.com/coveooss/json-schema-for-humans).

- <a href="https://packageurl.org/purl-schemas/purl-test.schema-0.2.json" target="_blank">JSON Schema</a> `↗`
- <a href="/interactive_schemas/purl-test.schema-0.2.html" target="_blank">Interactive HTML</a> `↗`

*See the Test cases page for additional information about the properties in the
schema.*
