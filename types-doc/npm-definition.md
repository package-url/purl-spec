> NOTE: This file was auto-generated from the canonical JSON definition. Do not manually edit this file. Changes should be made in the corresponding JSON definition.

# PURL Type Definition: npm

**Name:** Node Package Manager (NPM)

**Description:** PURL type for Node.js packages managed by NPM.

**Schema ID:** `https://purl-spec.org/types/npm.json`

## PURL Syntax

The structure of a PURL for this package type is:

```
pkg:npm/<namespace>/<name>@<version>#<subpath>
```

## Namespace

- **Requirement:** Optional
- **Allowed Characters:** `^[a-z0-9-]+$`
- **Case Sensitivity:** case-sensitive
- **Normalization:** lowercase
- **Native Label:** scope

## Name

- **Requirement:** Required
- **Allowed Characters:** `^[a-z0-9-]+$`
- **Case Sensitivity:** case-sensitive
- **Normalization:** lowercase
- **Native Label:** name

## Version

- **Requirement:** Optional
- **Allowed Characters:** `^[0-9a-zA-Z.-]+$`
- **Native Label:** version

## Subpath

- **Requirement:** Optional
- **Description:** A file or directory path within the package.

## Repository Information

- **Uses Repository:** Yes
- **Default Repository:** NPM Registry
  - **URL:** https://registry.npmjs.org/
  - **Description:** The official NPM package repository.

## Examples

- `pkg:npm/foobar@12.3.1`
- `pkg:npm/%40angular/animation@12.3.1`
- `pkg:npm/mypackage@12.4.5?vcs_url=git://host.com/path/to/repo.git%404345abcd34343`

