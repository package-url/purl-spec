# Annex B (informative) Recommended Qualifiers
This Annex documents standard PURL **qualifiers** that may be used across
many PURL **type** definitions.

## B.1 PURL qualifiers

The PURL **qualifiers** component provides flexibility to define important
PURL information at the PURL **type** level. This flexibility is provided by
**key=value** pairs. It may be tempting to use many **key=value** pairs to
document many package attributes, but their usage should be limited to the
minimal set of **key=value** pairs that are necessary for accurate package
identification or location. This restraint is necessary to ensure that PURLs
stay compact and human readable.

## B.2 ECMA-427 references
The standards for the PURL **qualifiers** component and the **key=value**
pairs are defined in two ECMA-427 clauses:
- [Clause 5.6.6 Qualifiers](https://ecma-tc54.github.io/ECMA-427sec-purl-specification-rules-qualifiers)
- [Clause 6.8  Qualifiers definition](https://ecma-tc54.github.io/ECMA-427/#sec--qualifiers-definition)


## B.3 Recommended qualifiers

Many **qualifiers** are applicable to multiple PURL **types**. These qualifier
 **keys** should be used according to the following definitions.

| qualifiers key | Definition                                |
|----------------|---------------------------------------------|
| checksum       | One or more checksums stored as a comma-separated list. Each item in the **value** is in the form of 'lowercase_algorithm:hex_encoded_lowercase_value' such as sha1:ad9503c3e994a4f611a4892f2e67ac82df727086'      |
| download_url   | A URL for a direct package download URL    |
| file_name      | The file name of a package archive. Use the **subpath** component for the use case where you need to specify a PURL at the file level.  |
| repository_url | A URL for when the `default_repository_url` property is empty in a PURL **type** definition or when there are multiple commonly used repositories for a PURL. **type**.                                                          |
| vcs_url        | A URL for a version control system (aka SCM or VCS) for the use case where you need to specify a PURL for a package at its SCM/VCS location. The syntax for 'vcs_url' should follow the Python pip syntax or the SPDX specification for ["Package Download Location"](https://github.com/spdx/spdx-spec/blob/cfa1b9d08903/chapters/3-package-information.md#3.7).                             |
| vers           | Specification of a version range instead of a single version. The primary use cases for this **qualifiers key** are to identify a version range for dependency analysis or vulnerability reporting. Use of this **key** is mutually exclusive with the **version** component. The **value** must adhere to the [Version Range Specification](https://packageurl.org/docs/vers/specification). |

### B.3.1 Checksum algorithm keys
The following standard 'checksum' **keys** should be used where applicable.
This is not an exclusive list.

- BLAKE2b-256 `blake2b-256` (used by pypi)
- BLAKE3 `blake3`
- MD5 `md5` (used by pypi maven)
- RIPEMD-160 `ripemd160`
- SHAKE256 `shake256`
- SHA1 `sha1` (used by maven npm)
- SHA2-224 `sha224`
- SHA2-256 `sha256` (used by cargo gem maven npm)
- SHA2-384 `sha384` (used by npm)
- SHA2-512 `sha512` (used by npm nuget)
- SHA3-224 `sha3-224`
- SHA3-256 `sha3-256`
- SHA3-384 `sha3-384`
- SHA3-512 `sha3-512`



## B.4 Examples


      pkg:pypi/django?vers=vers:pypi%2F%3E%3D1.11.0%7C%21%3D1.11.1%7C%3C2.0.0

