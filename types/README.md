### PURL Type Definitions

This directory contains the machine-readable definitions of all registered Package-URL (PURL) types,
one JSON file for each type. These JSON files serve as the reference for PURL type specifications.

## Contents

- **index.json**: The index of all registered PURL types as a simple list of types.
- Definitions: **<purl-type>-definition.json**: The definition for a specific PURL type (e.g.,
  maven-definition.json, npm-definition.json).
- Tests: **<purl-type>-test.json**: The test suite for a specific PURL type.

## Definitions

Each JSON file named *-definition.json in this directory follows the standard PURL Type Definition
Schema, ensuring:

- Consistency across all PURL types.
- Machine-readability for validation and automation.
- Standardized structure defining namespace, name, version, qualifiers, subpath, and repository behavior.

## Tests

Each JSON file named *-test.json in this directory follows the standard PURL Test Schema, ensuring:

- Consistency across all PURL types tests
- Machine-readability for automation such that tools can all use the same tests.
- Two levels (aka. groups) of tests: one for the base conformance to the PURL spec and one for
  advanced processing including flexible, recovering parsing of invalid PURL.


## Usage

- These JSON files are the the authoritative source for defining, validating and tesing PURL types.
- They should be referenced by tools, libraries, and documentation generators.

## Contributions

- Modifications must be made to these JSON files directly.
- The type definitions, tests and index and validated for consistency on commit.
- Documentation files are generated from these JSON files.
