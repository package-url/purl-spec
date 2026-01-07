<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: yocto

- **Type Name:** Yocto Project
- **Description:** Yocto Project recipes
- **Schema ID:** `https://packageurl.org/types/yocto-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:yocto/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository. The classifier repository_url is optional.

## Namespace definition

- **Requirement:** Optional
- **Native Label:** layer
- **Note:** `The namespace is the name of the layer which provides the recipe. The layer name as specified in the BBFILE_COLLECTIONS variable in conf/layer.conf of the layer.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** BPN
- **Note:** `The name of the package with common prefixes and suffixes removed, also known as BPN (https://docs.yoctoproject.org/ref-manual/variables.html#term-BPN) in a yocto recipe.`

## Version definition

- **Requirement:** Optional
- **Native Label:** PV
- **Note:** `The version of the package also known as PV (https://docs.yoctoproject.org/ref-manual/variables.html#term-PV>) in a yocto recipe.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| repository_url | Optional |  |  | The GIT URL of the layer. In example: https%3A%2F%2Fgit.openembedded.org%2Fopenembedded-core or https%3A%2F%2Fgithub.com%2Fakuster%2Fmeta-odroid. The URL scheme is mandatory and must be one of https, http, ssh, or git. |
| layer_version | Optional |  |  | layer_version is the version of the yocto layer which is a SHA1 commit, tag or branch of the yocto layer GIT repository. It should support also short commits (https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#_short_sha_1). |

## Examples

- `pkg:yocto/core/glibc@2.35`
- `pkg:yocto/core/glibc@2.35&repository_url=https:%2F%2Fgit.openembedded.org%2Fopenembedded-core&layer_version=kirkstone`
- `pkg:yocto/core/glibc@2.35&repository_url=https:%2F%2Fgit.openembedded.org%2Fopenembedded-core&layer_version=25ba9895b9`
- `pkg:yocto/core/glibc@2.35&repository_url=https:%2F%2Fgit.openembedded.org%2Fopenembedded-core&layer_version=25ba9895b98715adb66a06e50f644aea2e2c9eb6`
- `pkg:yocto/xilinx/u-boot-xlnx-uenv@1.0.0`
- `pkg:yocto/odroid-layer/emmc@1.0.0?layer_version=4e07fab&repository_url=https:%2F%2Fgithub.com%2Fakuster%2Fmeta-odroid`
