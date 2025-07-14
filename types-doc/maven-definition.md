> NOTE: This file was auto-generated from the canonical JSON definition. Do not manually edit this file. Changes should be made in the corresponding JSON definition.

# PURL Type Definition: maven

**Name:** Maven

**Description:** PURL type for Maven packages.

**Schema ID:** `https://purl-spec.org/types/maven.json`

## PURL Syntax

The structure of a PURL for this package type is:

```
pkg:maven/<namespace>/<name>@<version>?<qualifiers>#<subpath>
```

## Namespace

- **Requirement:** Required
- **Allowed Characters:** `^[a-zA-Z0-9_.-]+$`
- **Case Sensitivity:** case-sensitive
- **Native Label:** groupId

## Name

- **Requirement:** Required
- **Allowed Characters:** `^[a-zA-Z0-9_.-]+$`
- **Case Sensitivity:** case-sensitive
- **Native Label:** artifactId

## Version

- **Requirement:** Required
- **Allowed Characters:** `^[a-zA-Z0-9_.-]+$`
- **Native Label:** version

## Subpath

- **Requirement:** Optional
- **Description:** If specified, the subpath represents the individual files within the archive, such as resources, compiled classes, and source files.

## Qualifiers

| Name | Requirement | Description |
|------|-------------|-------------|
| classifier | Optional | The maven `classifier` as defined in the POM documentation. |
| type | Optional | The maven `type` as defined in the POM documentation. Maven uses a concept / coordinate called packaging which does not map directly 1:1 to a file extension. In this use case, we need to construct a link to one of many possible artifacts. Maven itself uses type in a dependency declaration when needed to disambiguate between them. |

## Repository Information

- **Uses Repository:** Yes
- **Default Repository:** Maven Central
  - **URL:** https://repo.maven.apache.org/maven2/
  - **Description:** The central repository for Maven packages.

## Examples

- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1`
- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=pom`
- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?classifier=sources`
- `pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?type=zip&classifier=dist`
- `pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x86&type=dll`
- `pkg:maven/net.sf.jacob-projec/jacob@1.14.3?classifier=x64&type=dll`
- `pkg:maven/groovy/groovy@1.0?repository_url=https://maven.google.com`

