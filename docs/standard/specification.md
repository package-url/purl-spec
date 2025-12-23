# Package-URL Specification

PURL stands for **Package-URL**.

A PURL is a URL composed of seven components:

    scheme:type/namespace/name@version?qualifiers#subpath

Components are separated by a specific character for unambiguous parsing.

Table 1 —  Components of a PURL

| Component  | Requirement | Description|
| ---------- | ----------- |:------------------------------------------------------ |
| scheme     | Required    | The URL scheme with the constant value of "pkg". One of the primary reasons for this single scheme is to facilitate the future official registration of the "pkg" scheme for Package-URLs. |
| type       | Required    | The package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc. |
| namespace  | Optional    | A name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization. Namespace is type-specific. |
| name       | Required    | The name of the package. |
| version    | Optional    | The version of the package.  |
| qualifiers | Optional    | Qualifier data for a package such as OS, architecture, repository, etc. Qualifiers are type-specific. |
| subpath    | Optional    | Subpath within a package, relative to the package root. |

Components are designed such that they form a hierarchy from the most
significant on the left to the least significant components on the right.

A PURL shall not contain a URL Authority, i.e. there is no support for
**username**, **password**, **host** and **port** components. A **namespace*
segment may sometimes look like a **host**, but its interpretation is specific
 to a **type**.

**Example 1 (Informative): Debian**

    pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie

**Example 2 (Informative): Maven**

    pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources

**Example 3 (Informative): Node Package Manager (NPM)**

    pkg:npm/foobar@12.3.1


## A PURL is a URL

- A PURL is a valid URL and URI that conforms to the URL definitions or
  specifications at:

  - https://tools.ietf.org/html/rfc3986
  - https://en.wikipedia.org/wiki/URL#Syntax
  - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
  - https://url.spec.whatwg.org/

- A PURL is a valid URL because it is a locator even though it has no 
Authority URL component: each type has a default repository location when 
defined.

- The PURL components are mapped to these URL components:

  - PURL **scheme**: this is a URL **scheme** with a constant value: **pkg**
  - PURL **type**, **namespace**, **name** and **version** components: these 
  are collectively mapped to a URL **path**
  - PURL **qualifiers**: this maps to a URL **query**
  - PURL **subpath**: this is a URL **fragment**
  - In a PURL, there is no support for a URL Authority (e.g. no
    **username**, **password**, **host** and **port** components).

- Special URL schemes as defined in https://url.spec.whatwg.org/ such as
  **file://**, **https://**, **http://** and **ftp://** are not valid PURL 
  types.
  They are valid URL or URI schemes but they are not a valid PURL scheme.
  They may be used to reference URLs in separate attributes outside of a PURL
  or in a PURL qualifier.

- Version control system (VCS) URLs such **git://**, **svn://**, **hg://** or 
as defined in Python pip or SPDX download locations are not valid PURL types.
  They are valid URL or URI schemes but they are not a valid PURL scheme.
  They are a closely related, compact and uniform way to reference VCS URLs.
  They may be used as references in separate attributes outside of a PURL or
  in a PURL qualifier.

  ## Permitted characters

A canonical PURL is composed of these permitted ASCII characters:

- the Alphanumeric Characters: **A to Z**, **a to z**, **0 to 9**,
- the Punctuation Characters: **.-_~** (period '.'
  dash '-', underscore '_' and tilde '~')
- the Percent Character: **%** (percent sign '%')
- the Separator Characters **:/@?=&#** (colon ':', slash '/', at sign '@',
  question mark '?', equal sign '=', ampersand '&' and hash sign '#')


## Separator characters

This is how each of the Separator Characters is used:

- ':' (colon) is the separator between **scheme** and **type**
- '/' (slash) is the separator between **type**, **namespace** and **name**
- '/' (slash) is the separator between **subpath** segments
- '@' (at sign) is the separator between **name** and **version**
- '?' (question mark) is the separator before **qualifiers**
- '=' (equals) is the separator between a **key** and a **value** of a
  **qualifier**
- '&' (ampersand) is the separator between **qualifiers** (each being a
  **key=value** pair)
- '#' (hash sign) is the separator before **subpath**

## Character encoding

- In the "Rules for each PURL component" clause, each component
  defines when and how to apply percent-encoding and decoding to its content.
- When percent-encoding is required by a component definition, the component
  string shall first be encoded as UTF-8.
- In the component string, each "data octet" shall be replaced by the
  percent-encoded "character triplet" applying the percent-encoding mechanism
  defined in [RFC 3986 section 2.1](https://datatracker.ietf.org/doc/html/rfc3986#section-2.1),
  including the RFC definition of "data octet" and "character triplet",
  and using these definitions for RFC's "allowed set" and "delimiters":

  - "allowed set" is composed of the Alphanumeric Characters and the
    Punctuation Characters
  - "delimiters" is composed of the Separator Characters

- The following characters shall not be percent-encoded:

  - the Alphanumeric Characters
  - the Punctuation Characters
  - the Separator Characters when being used as PURL separators
  - the colon ':', whether used as a Separator Character or otherwise
  - the percent sign '%' when used to represent a percent-encoded character

- Where the space ' ' is permitted, it shall be percent-encoded as '%20'.
- With the exception of the percent-encoding mechanism, the rules regarding
  percent-encoding are defined by this Standard alone.

## Case folding

References to "lowercase" in this Standard refer to the 
**culture-invariant** full case mapping defined in
[Section 3.13.2 of the Unicode Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G34078).

When applied to the ASCII character set, this operation converts uppercase
Latin letters (**A to Z**) to their corresponding lowercase forms 
(**a to z**).
All other ASCII characters remain unchanged.

## Rules for each PURL component

A PURL string is an ASCII URL string composed of seven components.

Except as expressly stated otherwise in this Clause, each component:

- may be composed of any of the characters defined in the _Permitted
  characters_ clause
- shall be encoded as defined in the _Character encoding_ clause

The "lowercase" rules are defined in the Case folding clause.

The rules for each component are:

### Scheme
- The **scheme** is a constant with the value "pkg".
- The **scheme** shall be followed by an unencoded colon ':'.
- PURL parsers shall accept URLs where the **scheme** and colon ':' are 
followed by one or more slash '/' characters, such as 'pkg://', and shall
ignore and remove all such '/' characters.

### Type
- The package **type** shall be composed only of ASCII letters and numbers,
period '.', and dash '-'.
- The **type** shall start with an ASCII letter.
- The **type** shall not be percent-encoded.
- The **type** is case insensitive. The canonical form is lowercase.

### Namespace
- The **namespace** is optional, unless required by the package's **type** 
definition.
- If present, the **namespace** may contain one or more segments, separated by
 a single unencoded slash '/' character.
- All leading and trailing slashes '/' are not significant and should be 
stripped in the canonical form. They are not part of the **namespace**.
- Each **namespace** segment shall be a percent-encoded string.
- When percent-decoded, a segment:
    - shall not contain any slash '/' characters
    - shall not be empty
    - may contain any Unicode character other than '/' unless the package's
**type** definition provides otherwise
- A URL host or Authority shall not be used as a **namespace**. Use instead a
**repository_url** qualifier. Note however, that for some types, the
**namespace** may look like a host.

### Name
- The **name** is prefixed by a single slash '/' separator when the 
**namespace** is not empty.
- All leading and trailing slashes '/' are not significant and should be 
stripped in the canonical form. They are not part of the **name**.
- A **name** shall be a percent-encoded string.
- When percent-decoded, a **name** may contain any Unicode character unless 
the package's **type** definition provides otherwise.

### Version
- The **version** is prefixed by a '@' separator when not empty.
- This '@' is not part of the **version**.
- A **version** shall be a percent-encoded string.
- When percent-decoded, a **version** may contain any Unicode character
unless the package's **type** definition provides otherwise.
- A **version** is a plain and opaque string.

### Qualifiers
- The **qualifiers** component shall be prefixed by an unencoded question mark 
'?' separator when not empty. This '?' separator is not part of the 
**qualifiers** component.
- The **qualifiers** component is composed of one or more **key=value** pairs. Multiple **key=value** pairs shall be separated by an unencoded ampersand '&'. 
This '&' separator is not part of an individual **qualifier**.
- A **key** and **value** shall be separated by the unencoded equal sign '=' character. This '=' separator is not part of the **key** or **value**.
- A **value** dhall not be an empty string: a **key=value** pair with an empty **value** is the same as if no **key=value** pair exists for this **key**.
- For each **key=value** pair:
    - The **key** shall be composed only of lowercase ASCII letters and 
    numbers, period '.', dash '-' and underscore '_'.
    - A **key** shall start with an ASCII letter.
    - A **key** shall not be percent-encoded.
    - Each **key** shall be unique among all the keys of the **qualifiers**    component.
    - A **value** may contain any Unicode character and all characters shall 
    be encoded as described in the _Character encoding_ clause.

### Subpath
- The **subpath** string is prefixed by a '#' separator when not empty.
- The '#' is not part of the **subpath**.
- The **subpath** contains zero or more segments, separated by slash '/'
- Leading and trailing slashes '/' are not significant and should be stripped 
in the canonical form.
- Each **subpath** segment shall be a percent-encoded string
- When percent-decoded, a segment:
    - shall not contain any slash '/' characters
    - shall not be empty
    - shall not be any of '..' or '.'
    - may contain any Unicode character other than '/' unless the package's       **type** definition provides otherwise.
- The **subpath** shall be interpreted as relative to the root of the package.



