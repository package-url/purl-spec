## PURL qualifiers guidance

The PURL **qualifiers** component is intended to provide flexibility to define important PURL information at the PURL **type** level. This flexibility is 
provided by **key=value** pairs. It may be tempting to use many **key=value** 
pairs to document package attributes, but their usage should be limited and 
focused on a minimal set of **key=value** pairs 
that are necessary for accurate package identification. This restraint is 
necessary to ensure that PURLs stay compact and readable.

Some commonly-used **qualifiers keys** are:

- 'checksum' is a qualifier for one or more checksums stored as a
comma-separated list. Each item in the **value** is in the form of
'lowercase_algorithm:hex_encoded_lowercase_value' such as
'sha1:ad9503c3e994a4f611a4892f2e67ac82df727086'.

  For example (with checksums truncated for brevity):

      checksum=sha1:ad9503c3e994a4f,sha256:41bf9088b3a1e6c1ef1d

- 'download_url' is a URL for a direct package download URL.

- 'file_name' is normally used to specify the file name of a package archive. 
You should use the **subpath** component for the use case where you need to 
specify a PURL at the file level.

- 'repository_url' should be used to provide a URL when a PURL **type** 
definition does not specify a 'default_repository_url' or when there are 
multiple commonly used repositories for a PURL **type**.

- 'vcs_url' should be used to provide a URL for a version control system (aka 
SCM or VCS) for the use case where you need to specify a PURL for a package at
its SCM/VCS location. The syntax for 'vcs_url' should follow the Python pip 
syntax or the SPDX specification for ["Package Download Location"](https://github.com/spdx/spdx-spec/blob/cfa1b9d08903/chapters/3-package-information.md#3.7).

- 'vers' allows the specification of a version range instead of a single 
version. The primary use cases for this **qualifiers key** are to identify a 
version range for dependency analysis or vulnerability reporting. Use of this 
**key** is mutually exclusive with the **version** component. The **value** 
must adhere to the [Version Range Specification](https://github.com/package-url/vers-spec/blob/main/VERSION-RANGE-SPEC.md).

  For example:

      pkg:pypi/django?vers=vers:pypi%2F%3E%3D1.11.0%7C%21%3D1.11.1%7C%3C2.0.0





