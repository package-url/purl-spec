<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: maven

- **Type Name:** Maven
- **Description:** PURL type for Maven packages.
- **Schema ID:** `https://packageurl.org/types/maven-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:maven/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Namespace definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** groupId

## Name definition

- **Case Sensitive:** Yes
- **Native Label:** artifactId

## Version definition

- **Case Sensitive:** Yes
- **Native Label:** version

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| classifier | Optional | classifier |  | The maven `classifier` as defined in the POM documentation. |
| type | Optional | type | jar | The maven `type` as defined in the POM documentation. Maven uses a concept called packaging which does not map directly 1:1 to a file extension. In this use case, we need to construct a link to one of many possible artifacts. Maven itself uses type in a dependency declaration when needed to disambiguate between them. |

## Repository Information

- **Use Repository:** Yes
- **Default Repository Name:** Maven Central
- **Default Repository URL:** https://repo.maven.apache.org/maven2/
- **Description:** The central repository for Apache Maven packages. This repository is also mirrored at https://repo1.maven.org/maven2/. Use the standard `repository_url` qualifier to point to another repository

## Examples

- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1`
- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=pom`
- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?classifier=sources`
- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=zip&classifier=dist`
- `pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x86&type=dll`
- `pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x64&type=dll`
- `pkg:maven/groovy/groovy@1.0?repository_url=https://maven.google.com`
