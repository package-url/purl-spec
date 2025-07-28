<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: golang

- **Type Name:** Go package
- **Description:** Go packages
- **Schema ID:** `https://packageurl.org/types/golang-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:golang/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository, this is implied in the namespace using the go get command conventions. In practice the go module proxy acts as a public defulat repository.

## Namespace definition

- **Requirement:** Required
- **Note:** `The namespace must be lowercased.`

## Name definition

- **Note:** `The name must be lowercased.`

## Version definition

- **Note:** `The version is often empty when a commit is not specified and should be the commit in most cases when available.`

## Subpath definition

- **Note:** `The subpath is used to point to a subpath inside a package.`

## Examples

- `pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c`
- `pkg:golang/google.golang.org/genproto#googleapis/api/annotations`
- `pkg:golang/github.com/gorilla/context@234fd47e07d1004f0aed9c#api`

## Note

the current definition predates Go modules and has several practical problems, and in particular it is impossible to determine what is a module and what is a package short of having full access to the source code or making an API call to the Go module proxy.
