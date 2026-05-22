### PURL Type Definitions

This directory contains the machine-readable definitions of all registered Package-URL (PURL) types,
one JSON file for each type. These JSON files serve as the reference for PURL type specifications.

## Definitions

Each JSON file named `<purl-type>-definition.json` in this directory follows the standard PURL Type Definition
Schema. The goals are:

- Consistency across all PURL types.
- Machine-readability for validation and automation.
- Standardized structure defining namespace, name, version, qualifiers, subpath, and repository behavior.

## Usage

- These JSON files are the the authoritative source for defining, validating and testing PURL types.
- They should be referenced by tools, libraries, and documentation generators.

## Related files

There are two other places in this repository with important PURL type data:
- [**purl-types-index.json**](https://github.com/package-url/purl-spec/blob/main/purl-types-index.json) - a simple index of
registered PURL types.
- PURL type-specific tests. These test files are in the [`tests/types`](https://github.com/package-url/purl-spec/tree/main/tests/types)
directory.

## PURL Type Tests
Each JSON file in the `tests/types` directory is named `<purl-type>-test.json` and is required to follow the PURL Test schema located at:
[`schemas/purl-test.schema-0.1.json`](https://github.com/package-url/purl-spec/blob/main/schemas/purl-test.schema-0.1.json).
The goals for the PURL Test Schema are:
- Consistency across PURL type tests.
- Machine-readability for automation such that tools can all use the same set of tests.
- Two levels (aka. test-groups) of tests: one for base conformance to the PURL spec and one for
  advanced processing including flexible parsing of invalid input PURLs.

NB: The PURL Test schema is not currently included in the [ECMA-427](https://ecma-tc54.github.io/ECMA-427/) standard for Package-URL (PURL).
It is version 0.1 and is currently pending some significant improvements. See the [**Upgrade PURL test suite** project](https://github.com/orgs/package-url/projects/10)
for a list of issues and PRs.

## Contributions

- Modifications must be made to these JSON files directly.
- The type definitions, tests and index are validated for consistency on commit.
- Documentation files are generated from these JSON files.
