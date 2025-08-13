## What is a `purl`?

`purl` stands for **package URL**.

A `purl` is a URL composed of seven components:

    scheme:type/namespace/name@version?qualifiers#subpath

Components are separated by a specific character for unambiguous parsing.

The definition for each components is:

- **scheme**: this is the URL scheme with the constant value of "pkg". One of
  the primary reason for this single scheme is to facilitate the future official
  registration of the "pkg" scheme for package URLs. Required.
- **type**: the package "type" or package "protocol" such as maven, npm, nuget,
  gem, pypi, etc. Required.
- **namespace**: some name prefix such as a Maven groupid, a Docker image owner,
  a GitHub user or organization. Optional and type-specific.
- **name**: the name of the package. Required.
- **version**: the version of the package. Optional.
- **qualifiers**: extra qualifying data for a package such as an OS,
  architecture, a distro, etc. Optional and type-specific.
- **subpath**: extra subpath within a package, relative to the package root.
  Optional.


Table 1: Components of a PURL

| Component  | Requirement | Description|
| ---------- | ----------- |:------------------------------------------------------ |
| scheme     | Required    | The URL scheme with the constant value of "pkg". One of the primary reasons for this single scheme is to facilitate the future official registration of the "pkg" scheme for package URLs. |
| type       | Required    | The package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc. |
| namespace  | Optional    | A name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization. Namespace is type-specific. |
| name       | Required    | The name of the package. |
| version    | Optional    | The version of the package.  |
| qualifiers | Optional    | Qualifier data for a package such as OS, architecture, repository, etc. Qualifiers are type-specific. |
| subpath    | Optional    | Subpath within a package, relative to the package root. |


Components are designed such that they form a hierarchy from the most significant
on the left to the least significant components on the right.


A `purl` must NOT contain a URL Authority i.e. there is no support for
`username`, `password`, `host` and `port` components. A `namespace` segment may
sometimes look like a `host` but its interpretation is specific to a `type`.


## Some `purl` examples

    pkg:bitbucket/birkenfeld/pygments-main@244fd47e07d1014f0aed9c
    pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
    pkg:gem/ruby-advisory-db-check@0.12.4
    pkg:github/package-url/purl-spec@244fd47e07d1004f0aed9c
    pkg:golang/google.golang.org/genproto#googleapis/api/annotations
    pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources
    pkg:npm/foobar@12.3.1
    pkg:nuget/EnterpriseLibrary.Common@6.0.1304
    pkg:pypi/django@1.11.1
    pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25


## A `purl` is a URL

- A `purl` is a valid URL and URI that conforms to the URL definitions or
  specifications at:

  - https://tools.ietf.org/html/rfc3986
  - https://en.wikipedia.org/wiki/URL#Syntax
  - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
  - https://url.spec.whatwg.org/

- This is a valid URL because it is a locator even though it has no Authority
  URL component: each `type` has a default repository location when defined.

- The `purl` components are mapped to these URL components:

  - `purl` `scheme`: this is a URL `scheme` with a constant value: `pkg`
  - `purl` `type`, `namespace`, `name` and `version` components: these are
    collectively mapped to a URL `path`
  - `purl` `qualifiers`: this maps to a URL `query`
  - `purl` `subpath`: this is a URL `fragment`
  - In a `purl` there is no support for a URL Authority (e.g. NO
    `username`, `password`, `host` and `port` components).

- Special URL schemes as defined in https://url.spec.whatwg.org/ such as
  `file://`, `https://`, `http://` and `ftp://` are NOT valid `purl` types.
  They are valid URL or URI schemes but they are not `purl`.
  They may be used to reference URLs in separate attributes outside of a `purl`
  or in a `purl` qualifier.

- Version control system (VCS) URLs such `git://`, `svn://`, `hg://` or as
  defined in Python pip or SPDX download locations are NOT valid `purl` types.
  They are valid URL or URI schemes but they are not `purl`.
  They are a closely related, compact and uniform way to reference VCS URLs.
  They may be used as references in separate attributes outside of a `purl` or
  in a `purl` qualifier.
