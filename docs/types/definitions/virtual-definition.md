<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: virtual

- **Type Name:** Virtual package
- **Description:** Virtual packages represent abstract requirements that can be satisfied by one or more concrete packages
- **Schema ID:** `https://packageurl.org/types/virtual-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:virtual/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** No
- **Note:** Virtual packages have no source repository by definition

## Namespace definition

- **Requirement:** Required

## Name definition

- **Requirement:** Required
- **Normalization rules:**
  - All compiler languages and interfaces shall be lowercased
  - Spaces shall be converted into dashes
  - Any other symbols that would need to be percent encoded shall be spelt out and prefixed with a dash
- **Native Label:** name
- **Note:** `If namespace is 'compiler', the name shall be a normalized programming language identifier. Any of the top-level keys in the [Linguist index](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml), or their aliases, whose `type` field is `programming`, are considered valid once normalized. For standardized language extensions or compiler plugins, consider using the syntax `<language-identifier>-ext-<extension-name>`. For 'interface', the name must refer to the normalized standard identifier, not any of its implementations (e.g. `blas` instead of OpenBLAS).`

## Version definition

- **Requirement:** Optional
- **Normalization rules:**
  - If the versioning scheme uses years, the full four-digit number should be used (e.g. a compiler for C99 shall be expressed as `pkg:virtual/compiler/c@1999) to allow meaningful comparisons without language-specific knowledge.
- **Native Label:** version

## Examples

- `pkg:virtual/compiler/c`
- `pkg:virtual/compiler/c@1999`
- `pkg:virtual/compiler/c-sharp`
- `pkg:virtual/compiler/c-plus-plus`
- `pkg:virtual/compiler/c-plus-plus@2014`
- `pkg:virtual/compiler/fortran`
- `pkg:virtual/compiler/rust`
- `pkg:virtual/compiler/zig`
- `pkg:virtual/interface/blas`
- `pkg:virtual/interface/lapack`
- `pkg:virtual/interface/mpi`
- `pkg:virtual/interface/openmp`
- `pkg:virtual/interface/openmp@4.5`
