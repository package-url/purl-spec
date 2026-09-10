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

Tools that build PURLs should sort multiple **qualifiers** lexicographically
by **key**, but this is not expected behaviour for a tool to parse or validate
a PURL.

## B.2 ECMA-427 references
The standards for the PURL **qualifiers** component and the **key=value**
pairs are defined in two ECMA-427 clauses:
- [Clause 5.6.6 Qualifiers](https://ecma-tc54.github.io/ECMA-427/#sec-purl-specification-rules-qualifiers)
- [Clause 6.8  Qualifiers definition](https://ecma-tc54.github.io/ECMA-427/#sec--qualifiers-definition)

## B.3 Recommended qualifiers

Many **qualifiers** are applicable to multiple PURL **types**. These qualifier
 **keys** should be used according to the following definitions.

| key            | Definition                                  |
|----------------|---------------------------------------------|
| checksum       | One or more checksums stored as a comma-separated list  |
| download_url   | A URL for a direct package download URL    |
| file_name      | The file name of a package archive         |
| repository_url | A URL for a package or software repository |
| vcs_url        | A URL for a version control system (VCS) location |
| vers           | A VERS notation that specifies a version range instead of a single version  |

### B.3.1 checksum qualifier
Each item in the **value** for a 'checksum' **qualifer** is in the form of
'lowercase_algorithm:hex_encoded_lowercase_value' such as 'sha1:ad9503c3e994a4f611a4892f2e67ac82df727086'

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

### B.3.2 download_url qualifier
Most package managers provide a mechanism to derive a 'download-url' from the
PURL data. Use this **qualifier** for the use case where the download URL for
a package cannot be derived from the PURL or otherwise provided by the package
manager. A 'download_url' **value** shall be percent-encoded.

### B.3.3 file_name qualifier
This **qualifier** is intended for the use case where you want to specify the
name of a package archive or other file. Use the **subpath** component for the
use case where you need to specify a PURL at the file level.

### B.3.4 repository_url qualifier
This **qualifier** is intended for the use cases where:
- the 'default_repository_url' property is empty in a PURL **type** definition
- there are multiple commonly used repositories for a PURL **type**

A 'repository_url' **value** shall be percent-encoded.

### B.3.5 vcs_url qualifier
This **qualifier** is intended for the use case where you where you need to
specify a PURL at its Version Control System location. The syntax for 'vcs_url'
is based on Python pip syntax at: https://pip.pypa.io/en/stable/topics/vcs-support/
The syntax is:

      <vcs_tool>+<transport>://<host_name>[/<path_to_repository>][@<revision_tag_or_branch>]#<sub_path>]

This compact VCS location notation supports referencing locations in version
control systems such as Git, Mercurial, Subversion and Bazaar, and specifies
the type of VCS tool using url prefixes: 'git+', 'hg+', 'bzr+', svn+ and
specific transport schemes such as SSH or HTTPS.

Specifying sub-paths, branch names, a commit hash, a revision or a tag name is
recommended, and supported using the '@' delimiter for commit **versions** and
the '#' delimiter for **sub-paths**.

Using user names and password in the **host_name** is not supported and should
be reported by tools as an error. User access control to URLs or VCS
repositories shall be handled outside of an SPDX document.

In VCS location compact notations, the trailing slashes in **host_name**, and **path_to_repository** are not significant. Leading and trailing slashes in
**sub_path** are not significant.

- The supported schemes for Git are: 'git', 'git+git', 'git+https', 'git+http',
  and 'git+ssh'. 'git' and 'git+git' are equivalent.
- The supported schemes for Mercurial are: 'hg+http', 'hg+https',
  'hg+static-http', and 'hg+ssh'.
- The supported schemes for Subversion are: 'svn', 'svn+svn', 'svn+http',
  'svn+https', and 'svn+ssh'. 'svn and 'svn+svn' are equivalent.
- The supported schemes for Bazaar are: 'bzr+http', 'bzr+https', 'bzr+ssh',
  'bzr+sftp', 'bzr+ftp', and 'bzr+lp'.

A 'vcs_url' **value** shall be percent-encoded.

### B.3.6 vers qualifier
The primary use cases for this **qualifier** are to identify a version range
for dependency analysis or vulnerability reporting. Use of this **qualifier**
is mutually exclusive with use of the **version** component. The **value** for
a 'vers' **key** must adhere to the [Version Range Specification](https://packageurl.org/docs/vers/specification).

Example:

      pkg:pypi/django?vers=vers:pypi%2F%3E%3D1.11.0%7C%21%3D1.11.1%7C%3C2.0.0

