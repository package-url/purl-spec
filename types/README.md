### PURL Type Definitions

This directory contains the machine-readable definitions of all registered
Package-URL (PURL) types, one JSON file for each type. These JSON files serve
as the reference for PURL type specifications.

## Definitions

Each JSON file named `<purl-type>-definition.json` in this directory follows
the current standard PURL Type Definition Schema. The goals are:

- Consistency across all PURL types
- Machine-readability for validation and automation
- Standardized structure defining namespace, name, version, qualifiers,
  subpath, and repository behavior

## Usage

- These JSON files are the authoritative source for defining, validating
  and testing PURL types.
- They should be referenced by tools, libraries, and documentation generators.

## Related files

There are two other places in this repository with important PURL type data:
- [**purl-types-index.json**](https://github.com/package-url/purl-spec/blob/main/purl-types-index.json): a simple index of registered PURL types.
- PURL type-specific tests. These test files are in the [`tests/types`](https://github.com/package-url/purl-spec/tree/main/tests/types)
directory.

## PURL Type Tests
Each JSON file in the `tests/types` directory is named `<purl-type>-test.json` and is required to follow the PURL Test schema located at:
[`schemas/purl-test.schema-0.2.json`](https://github.com/package-url/purl-spec/blob/main/schemas/purl-test.schema-0.2.json).
The goals for the PURL Test Schema are:
- Consistency across PURL type tests.
- Machine-readability for automation such that tools can all use the same set
  of tests.
- Two levels of tests (`test_groups`): one for test cases that are required
  for conformance to the PURL specification and one for test cases that are recommended for tools to normalize or otherwise improve invalid input PURL
  data so that it can pass the required tests.

NB: The PURL Test schema is not currently included in the [ECMA-427](https://ecma-tc54.github.io/ECMA-427/) standard for Package-URL (PURL).
It is version 0.2 and is currently pending some significant improvements. See the [**Upgrade PURL test suite** project](https://github.com/orgs/package-url/projects/10)
for a list of issues and PRs.

## Contributions
Community contributions for PURL `type` definitions and tests are welcome.

- Registering a new PURL `type` requires an issue to document background
  information for the new `type`. Please use the [Register new PURL type issue template.](https://github.com/package-url/purl-spec/blob/main/.github/ISSUE_TEMPLATE/Register%20new%20PURL%20type.md)
- Changing an existing PURL `type` requires an issue to explain the change
  unless the change is a minor editorial correction. Please use the [Change
  register PURL type template.](https://github.com/package-url/purl-spec/blob/main/.github/ISSUE_TEMPLATE/Change%20registered%20PURL%20type.md)
- Registering a new PURL `type` or changing an existing PURL `type` also
  requires a pull request.
