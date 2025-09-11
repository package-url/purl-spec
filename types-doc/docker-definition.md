<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: docker

- **Type Name:** Docker image
- **Description:** for Docker images
- **Schema ID:** `https://packageurl.org/types/docker-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:docker/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://hub.docker.com

## Namespace definition

- **Requirement:** Optional
- **Note:** `The namespace is the registry/user/organization if present.`

## Name definition

- **Requirement:** Required
- **Native Label:** name

## Version definition

- **Requirement:** Optional
- **Note:** `The version should be the image id sha256 or a tag. Since tags can be moved, a sha256 image id is preferred.`

## Examples

- `pkg:docker/cassandra@latest`
- `pkg:docker/smartentry/debian@dc437cc87d10`
- `pkg:docker/customer/dockerimage@sha256%3A244fd47e07d10?repository_url=gcr.io`
