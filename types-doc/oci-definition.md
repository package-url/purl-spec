<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: oci

- **Type Name:** OCI image
- **Description:** For artifacts stored in registries that conform to the OCI Distribution Specification https://github.com/opencontainers/distribution-spec including container images built by Docker and others
- **Schema ID:** `https://packageurl.org/types/oci-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:oci/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no canonical package repository for OCI artifacts. Therefore oci purls must be registry agnostic by default. To specify the repository, provide a repository_url value.

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `OCI purls do not contain a namespace, although, repository_url may contain a namespace as part of the physical location of the package.`

## Name definition

- **Note:** `The name is not case sensitive and must be lowercased. The name is the last fragment of the repository name. For example if the repository name is library/debian then the name is debian.`

## Version definition

- **Note:** `The version is the sha256:hex_encoded_lowercase_digest of the artifact and is required to uniquely identify the artifact.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| arch | Optional |  |  | key for a package architecture, when relevant. |
| repository_url | Optional |  |  | A repository URL where the artifact may be found, but not intended as the only location. This value is encouraged to identify a location the content may be fetched. |
| tag | Optional |  |  | artifact tag that may have been associated with the digest at the time. |

## Examples

- `pkg:oci/debian@sha256%3A244fd47e07d10?repository_url=docker.io/library/debian&arch=amd64&tag=latest`
- `pkg:oci/debian@sha256%3A244fd47e07d10?repository_url=ghcr.io/debian&tag=bullseye`
- `pkg:oci/static@sha256%3A244fd47e07d10?repository_url=gcr.io/distroless/static&tag=latest`
- `pkg:oci/hello-wasm@sha256%3A244fd47e07d10?tag=v1`

## Reference URLs

- `https://github.com/opencontainers/distribution-spec`
