## What is a ``purl``?

``purl`` stands for **package URL**.

A purl is a URL composed of seven components.

Table 1: Components of a PURL

| Component  | Requirement | Description|
| ---------- | ----------- |:------------------------------------------------------ |
| scheme     | Required    | The URL scheme with the constant value of "pkg". One of the primary reasons for this single scheme is to facilitate the future official registration of the "pkg" scheme for package URLs. |
| type       | Required    | The package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc. |
| namespace  | Optional    | A name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization. Namespace is type-specific. |
| name       | Required    | The name of the package. |
| version    | Optional    | The version of the package.  |
| qualifiers | Optional    | Qualifier data for a package such as OS, architecture, repository, etc. Qualifiers are type-specific. |
| subpath    | Optional    | Subpath within a package, relative to the package root. |

Components are separated by a specific character for unambiguous parsing. Components are designed such that they form a hierarchy from the most significant on the left to the least significant on the right.

A ``purl`` must NOT contain a URL Authority. i.e. there is no support for ``username``, ``password``, ``host`` and ``port`` components. A ``namespace`` segment may sometimes look like a ``host`` but its interpretation is specific to a ``type``.
