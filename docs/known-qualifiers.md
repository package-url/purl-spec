## Known PURL  **qualifiers** key/value pairs

Note: Do not abuse **qualifiers**: it can be tempting to use many qualifier
keys but their usage should be limited to the bare minimum for proper package
identification to ensure that a PURL  stays compact and readable in most
cases.

Additional, separate external attributes stored outside of a PURL are the
preferred mechanism to convey extra long and optional information such as a
download URL, VCS URL or checksums in an API, database or web form.

With this warning, the known **key** and **value** defined here are valid for
use in all package types:

- VERS allows the specification of a version range.
  The **value** must adhere to the [Version Range Specification](https://github.com/package-url/vers-spec/blob/main/VERSION-RANGE-SPEC.md).
  This qualifier is mutually exclusive with the **version** component.
  For example:

      pkg:pypi/django?vers=vers:pypi%2F%3E%3D1.11.0%7C%21%3D1.11.1%7C%3C2.0.0

- 'repository_url' is an extra URL for an alternative, non-default package
repository or registry. When a package does not come from the 
'default_repository_url' for its **type** a PURL may be qualified with this 
extra URL.

- 'download_url' is an extra URL for a direct package web download URL to
  optionally qualify a PURL .

- 'vcs_url' is an extra URL for a package version control system URL to
  optionally qualify a PURL. The syntax for this URL should be as defined
  in Python pip or the SPDX specification. See
  https://github.com/spdx/spdx-spec/blob/cfa1b9d08903/chapters/3-package-information.md#3.7

- 'file_name' is an extra file name of a package archive.

- 'checksum' is a qualifier for one or more checksums stored as a
  comma-separated list. Each item in the **value** is in form of
  'lowercase_algorithm:hex_encoded_lowercase_value' such as
  'sha1:ad9503c3e994a4f611a4892f2e67ac82df727086'.

  For example (with checksums truncated for brevity):

      checksum=sha1:ad9503c3e994a4f,sha256:41bf9088b3a1e6c1ef1d
