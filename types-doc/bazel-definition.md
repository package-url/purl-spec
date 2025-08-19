<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: bazel

- **Type Name:** Bazel modules
- **Description:** Bazel modules as specified at https://bazel.build/external/module
- **Schema ID:** `https://packageurl.org/types/bazel-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:bazel/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://bcr.bazel.build
- **Note:** The default repository is the Bazel Central Registry (BCR)

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `Bazel modules do not use namespaces`

## Name definition

- **Requirement:** Required
- **Note:** `The name as defined in the MODULE.bazel file`

## Version definition

- **Requirement:** Required
- **Note:** `The version as defined in the MODULE.bazel file. Uses a relaxed semantic versioning format described at https://bazel.build/external/module#version-format.`

## Subpath definition

- **Requirement:** Optional
- **Native Label:** label
- **Note:** `The optional subpath MAY refer to a label of a particular package or target in the module (https://bazel.build/concepts/labels). The label MUST NOT include a repo name and the leading '//' MUST be omitted. When referring to targets, the label MUST include the name of the target, separated from the package by ':'. If there is no target name, subpath is assumed to refer to the whole package.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional | registry | https://bcr.bazel.build | The URL of the registry that hosts this Bazel module. If not specified, it defaults to the BCR URL. |

## Examples

- `pkg:bazel/rules_java@7.8.0`
- `pkg:bazel/curl@8.8.0.bcr.1`
- `pkg:bazel/curl@8.8.0?repository_url=https://example.org/bazel-registry`
- `pkg:bazel/rules_java@8.5.0#java/runfiles`
- `pkg:bazel/rules_java@8.5.0#java/runfiles:runfiles`
- `pkg:bazel/rules_go@0.48.0#go`

## Reference URLs

- `https://bazel.build/external/module`
