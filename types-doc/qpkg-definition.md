<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: qpkg

- **Type Name:** QNX package
- **Description:** QNX packages
- **Schema ID:** `https://packageurl.org/types/qpkg-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:qpkg/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository, this should be implied either from the namespace or using a repository base URL as repository_url qualifiers key.

## Namespace definition

- **Requirement:** Required
- **Native Label:** vendor
- **Note:** `The namespace is the vendor of the package. It is not case sensitive and must be lowercased.`

## Name definition

- **Requirement:** Required
- **Native Label:** name

## Examples

- `pkg:qpkg/blackberry/com.qnx.sdp@7.0.0.SGA201702151847`
- `pkg:qpkg/blackberry/com.qnx.qnx710.foo.bar.qux@0.0.4.01449T202205040833L`
