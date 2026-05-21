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
- **Note:** There is no default package repository, this is implied in the namespace using the go get command conventions. In practice the Go module proxy acts as a public default repository.

## Namespace definition

- **Requirement:** Required
- **Note:** `The namespace must be lowercased.`

## Name definition

- **Requirement:** Required
- **Note:** `The name must be lowercased.`

## Version definition

- **Requirement:** Optional
- **Note:** `The version may start with a lowercased "v" followed by: a semantic version, or a Go "pseudo-version", which consists of a semantic version followed by a timestamp and revision identifier (see https://go.dev/ref/mod#pseudo-versions).`

## Subpath definition

- **Requirement:** Optional
- **Note:** `The subpath is used to point to a package inside a module.`

## Examples

- `pkg:golang/github.com/gorilla/context@v1.1.1`
- `pkg:golang/google.golang.org/genproto#googleapis/api/annotations`
- `pkg:golang/golang.org/x/text@v0.0.0-20170915032832-14c0d48ead0c#collate`

## Note

The current definition predates Go modules and has several practical problems, and in particular it is impossible to determine what is a module and what is a package short of having full access to the source code or making an API call to the Go module proxy.
