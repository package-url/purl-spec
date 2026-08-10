---
id: test-schema-changes
title: PURL test schema v0.2 changes
sidebar_label: Test schema changes
hide_table_of_contents: true
---

# PURL test schema v0.2 changes
The PURL test schema was updated to: https://packageurl.org/schemas/purl-test.schema-0.2.json 
on August 4, 2026. This update includes an automated update to all of the PURL 
test suite files at: `purl-spec/tests/`. See a summary of the changes below.

The original PURL test suite files for the [PURL test schema v0.1](https://packageurl.org/schemas/purl-test.schema-0.1.json) remain available under [purl-spec v1.0.1](https://github.com/package-url/purl-spec/releases/tag/v1.0.1).

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
value because the input and output are required to be the same - a PURL tool
can easily test this "roundtrip" behavior without a test case.

The 'validate' **test type** does not require the input PURL string to be in 
canonical form. There is a high degree of similarity between the 'parse'
and 'validate' **test types** in terms of the functions a PURL tool performs.
The key difference is that the **expected output** from a 'parse' test case is
an object composed of decoded PURL components and the **expected output**
from a 'validate' test case is a PURL string.









