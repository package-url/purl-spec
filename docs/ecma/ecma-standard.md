# About this Specification

The document at <https://tc54.org/ecmaXXX/> is the most accurate and
up-to-date Package-URL specification.

This document is available as [a single
page](https://ecma-tc54.github.io/ECMA-xxx-PURL/) and as [multiple
pages](https://ecma-tc54.github.io/ECMA-xxx-PURL/multipage/).

# Contributing to this Specification

This specification is developed on GitHub with the help of the
Package-URL community. There are a number of ways to contribute to the
development of this specification:

- GitHub Repository: <https://github.com/Ecma-TC54/ECMA-xxx-PURL>
- Issues: [All
  Issues](https://github.com/Ecma-TC54/ECMA-xxx-PURL/issues), [File a
  New Issue](https://github.com/Ecma-TC54/ECMA-xxx-PURL/issues/new)
- Pull Requests: [All Pull
  Requests](https://github.com/Ecma-TC54/ECMA-xxx-PURL/pulls), [Create a
  New Pull
  Request](https://github.com/Ecma-TC54/ECMA-xxx-PURL/pulls/new)
- Editors:
  - [John Horan](mailto:jmhoran@aboutcode.org)
  - [Michael Herzog](mailto:mjherzog@aboutcode.org)
  - [Philippe Ombredanne](mailto:pombredanne@aboutcode.org)
  - [Steve Springett](mailto:steve.springett@owasp.org)
- Community:
  - Chat: [Slack
    Channel](https://cyclonedx.slack.com/archives/C06KTE3BWEB)

Refer to the
[colophon](https://ecma-tc54.github.io/ECMA-xxx-PURL/#sec-colophon) for
more information on how this document is created.

# Introduction

Software ecosystems have evolved into highly interconnected networks of
components, packages, and dependencies. Managing this complexity demands
a robust, uniform mechanism to identify and track software packages
across diverse ecosystems and tools. Package-URL (PURL) was developed to
address this challenge by providing a simple, consistent, and flexible
approach to identifying software packages with precision and clarity.

PURL introduces a standardized URL-based syntax that uniquely identifies
software packages, independent of their ecosystem or distribution
channel. Unlike traditional identification methods, PURL embeds critical
metadata directly into its structure, enabling efficient, accurate
package identification at scale. This standardization ensures
interoperability between tools and ecosystems, fostering greater
collaboration and reducing ambiguity in software supply chain
management.

Challenges addressed by PURL:

- **Ambiguity in Package Identification:** With diverse naming
  conventions across ecosystems, identifying software packages reliably
  has historically been a challenge. PURL eliminates this ambiguity by
  creating a universal identifier with a predictable structure.
- **Cross-Ecosystem Interoperability:** Developers, organizations, and
  tools often work across multiple ecosystems, each with its own package
  management systems. PURL harmonizes these differences, enabling
  seamless interoperability.
- **Enhanced Traceability and Risk Management:** In an era where supply
  chain security is critical, PURL provides the foundation for
  identifying and tracing packages to their origins, dependencies, and
  potential vulnerabilities.
- **Tooling and Automation:** By standardizing package identification,
  PURL simplifies tooling development, automation, and integration for
  tasks such as software composition analysis, vulnerability management,
  and license compliance.

As software supply chain security becomes a global priority, formalizing
PURL as an international standard ensures its adoption and consistent
implementation. Standardization under Ecma International Technical
Committee 54 (TC54) positions PURL as a foundational building block for
secure, transparent, and efficient software ecosystems worldwide.

By enabling a universally recognized and implementable specification,
PURL aligns with global efforts to improve the security, reliability,
and accountability of software supply chains. Its adoption ensures that
organizations and developers can rely on a common language to manage
software packages across the diverse and rapidly evolving software
landscape.

# 2 Conformance

## 2.1 Requirements Terminology

In this standard, the words that are used to define the significance of
each requirement are detailed below. These words are used in accordance
with their definitions in [RFC
2119](https://www.ietf.org/rfc/rfc2119.txt), and their respective
meanings are reproduced below:

- Must: This word, or the adjective “required” and the auxiliary verb
  “shall”, means that the item is an absolute requirement of the
  standard.
- Should: This word, or the adjective “recommended”, means that there
  might exist valid reasons in particular circumstances to ignore this
  item, but the full implications should be understood and the case
  carefully weighed before making an implementation decision.
- May: This word, or the adjective “optional”, means that this item is
  truly optional.

The words “must not”, “shall not”, “should not”, and “not recommended”,
are the negative forms of “must”, “shall”, “should”, and “recommended”,
respectively. There is no negative form of “may”.

## 2.2 Implementation Conformance

A conforming implementation of Package-URL (PURL) must fully implement
and support all elements defined within this specification, including
the syntax, components, and semantic requirements for constructing and
interpreting valid PURLs.

A conforming implementation of PURL must adhere to the syntax defined in
this specification, ensuring that all PURLs are parsed, constructed, and
validated according to the prescribed rules. The implementation must
provide full support for ecosystem-agnostic behaviour, enabling PURLs to
function consistently and reliably across diverse environments.

All required components of a PURL, such as the scheme, type, and name,
must be present and validated according to the rules defined in this
specification. Additionally, optional components, including qualifiers
and subpaths, must be handled appropriately if provided, in full
compliance with their specified behaviours.

Implementations must ensure that equivalent PURLs are consistently
resolved to the same canonical representation. This includes strict
adherence to normalisation and equivalence rules. Furthermore,
implementations must process URI encoding and decoding for PURL
components according to the standards outlined in RFC 3986.

Invalid PURLs that fail to conform to the specification must be
identified and rejected by any conforming implementation. This
guarantees the integrity and reliability of PURLs in all supported
contexts.

A conforming implementation of PURL may extend its functionality by
providing ecosystem-specific validation, processing, or metadata
handling, as long as these extensions do not violate the core
specification. Additionally, implementations may offer auxiliary tools
or features, such as utilities for constructing or validating PURLs,
provided they align with the standard’s requirements.

A conforming implementation must not redefine or alter the core syntax,
components, or semantics defined by this specification. Any prohibited
extensions explicitly identified in the specification must not be
implemented. Furthermore, behaviours that compromise the
interoperability of PURLs across tools, platforms, or ecosystems are
strictly disallowed.

A conforming implementation of Package-URL may choose to implement or
not implement Normative Optional subclauses. If any Normative Optional
behaviour is implemented, all of the behaviour in the containing
Normative Optional clause must be implemented. A Normative Optional
clause is denoted in this specification with the words “Normative
Optional” in a coloured box, as shown below.

## 2.3 Example Normative Optional Clause Heading

Example clause contents.

# 3 Normative References

The following referenced documents are indispensable for the application
of this document. For dated references, only the edition cited applies.
For undated references, the latest edition of the referenced document
(including any amendments) applies.

ASCII, *American National Standards Institute, “Coded Character Set –
7-bit American Standard Code for Information Interchange”, ANSI X3.4,
1986* https://en.wikipedia.org/wiki/ASCII

RFC 3986, ​*Uniform Resource Identifier (URI): Generic Syntax*​.
<https://datatracker.ietf.org/doc/html/rfc3986>

# 4 Overview

This section contains a non-normative overview of the Package-URL
specification.

The Package-URL (PURL) specification defines a lightweight, universal
syntax for identifying software packages. By leveraging a URL-based
format, PURL provides a consistent and interoperable mechanism for
referencing software packages across a wide range of ecosystems and
tools. Its design addresses the challenges of ambiguity, inconsistency,
and fragmentation in software package identification, enabling better
interoperability and traceability in modern software supply chains.

This specification focuses on the core aspects of PURL, including its
syntax, required components, optional attributes, and conformance
requirements. It does not cover ecosystem-specific types or extensions
such as PURL Version Ranges (VERS). However, the flexibility of PURL
allows it to be extended to meet the needs of diverse package ecosystems
without compromising its universal applicability.

The primary audience for this specification includes developers, tool
implementers, and organisations involved in software composition
analysis, dependency management, and supply chain security. PURL is
foundational to a variety of use cases, from software bill of materials
(SBOM) generation and license compliance to vulnerability tracking and
software artifact exchange.

While this document serves as the authoritative reference for
implementing PURL, it is complemented by various ecosystem-specific
guidance documents, examples, and related standards. These resources
provide additional context and practical insights for leveraging PURL
effectively.

This overview is non-normative and serves to provide context for the
specification’s intent, purpose, and audience. For detailed requirements
and conformance criteria, refer to the normative sections of this
specification.

# 5 Package-URL Specification

`purl` stands for **package URL**.

A purl is a URL composed of seven components.

Table 1: Components of a PURL

| Component | Requirement | Description |
|----|----|:---|
| scheme | Required | The URL scheme with the constant value of “pkg”. One of the primary reasons for this single scheme is to facilitate the future official registration of the “pkg” scheme for package URLs. |
| type | Required | The package “type” or package “protocol” such as maven, npm, nuget, gem, pypi, etc. |
| namespace | Optional | A name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization. Namespace is type-specific. |
| name | Required | The name of the package. |
| version | Optional | The version of the package. |
| qualifiers | Optional | Qualifier data for a package such as OS, architecture, repository, etc. Qualifiers are type-specific. |
| subpath | Optional | Subpath within a package, relative to the package root. |

Components are separated by a specific character for unambiguous
parsing. Components are designed such that they form a hierarchy from
the most significant on the left to the least significant on the right.

A `purl` must NOT contain a URL Authority. i.e. there is no support for
`username`, `password`, `host` and `port` components. A `namespace`
segment may sometimes look like a `host` but its interpretation is
specific to a `type`.

## 5.1 A PURL is a URL

- A `purl` is a valid URL and URI that conforms to the URL definitions
  or specifications at:
  - https://tools.ietf.org/html/rfc3986
  - https://en.wikipedia.org/wiki/URL#Syntax
  - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
  - https://url.spec.whatwg.org/
- This is a valid URL because it is a locator even though it has no
  Authority URL component: each `type` has a default repository location
  when defined.
- The `purl` components are mapped to these URL components:
  - `purl` `scheme`: this is a URL `scheme` with a constant value: `pkg`
  - `purl` `type`, `namespace`, `name` and `version` components: these
    are collectively mapped to a URL `path`
  - `purl` `qualifiers`: this maps to a URL `query`
  - `purl` `subpath`: this is a URL `fragment`
  - In a `purl` there is no support for a URL Authority (e.g. NO
    `username`, `password`, `host` and `port` components).
- Special URL schemes as defined in https://url.spec.whatwg.org/ such as
  `file://`, `https://`, `http://` and `ftp://` are NOT valid `purl`
  types. They are valid URL or URI schemes but they are not `purl`. They
  may be used to reference URLs in separate attributes outside of a
  `purl` or in a `purl` qualifier.
- Version control system (VCS) URLs such `git://`, `svn://`, `hg://` or
  as defined in Python pip or SPDX download locations are NOT valid
  `purl` types. They are valid URL or URI schemes but they are not
  `purl`. They are a closely related, compact and uniform way to
  reference VCS URLs. They may be used as references in separate
  attributes outside of a `purl` or in a `purl` qualifier.

## 5.2 Permitted Characters

A canonical `purl` is composed of these permitted ASCII characters:

- the Alphanumeric Characters: `A to Z`, `a to z`, `0 to 9`,
- the Punctuation Characters: `.-_~` (period ‘.’, dash ‘-’, underscore
  ’\_’ and tilde ‘~’),
- the Percent Character: `%` (percent sign ‘%’), and
- the Separator Characters `:/@?=&#` (colon ‘:’, slash ‘/’, at sign ‘@’,
  question mark ‘?’, equal sign ‘=’, ampersand ‘&’ and pound sign ‘\#’).

## 5.3 Separator Characters

This is how each of the Separator Characters is used:

- ‘:’ (colon) is the separator between `scheme` and `type`
- ‘/’ (slash) is the separator between `type`, `namespace` and `name`
- ‘/’ (slash) is the separator between `subpath` segments
- ‘@’ (at sign) is the separator between `name` and `version`
- ‘?’ (question mark) is the separator before `qualifiers`
- ‘=’ (equals) is the separator between a `key` and a `value` of a
  `qualifier`
- ‘&’ (ampersand) is the separator between `qualifiers` (each being a
  `key=value` pair)
- ‘\#’ (number sign) is the separator before `subpath`

## 5.4 Character Encoding

- In the “Rules for each `purl` component” section, each component
  defines when and how to apply percent-encoding and decoding to its
  content.
- When percent-encoding is required by a component definition, the
  component string MUST first be encoded as UTF-8.
- In the component string, each “data octet” MUST be replaced by the
  percent-encoded “character triplet” applying the percent-encoding
  mechanism defined in [RFC 3986 section
  2.1](https://datatracker.ietf.org/doc/html/rfc3986#section-2.1),
  including the RFC definition of “data octet” and “character triplet”,
  and using these definitions for RFC’s “allowed set” and “delimiters”:
  - “allowed set” is composed of the Alphanumeric Characters and the
    Punctuation Characters
  - “delimiters” is composed of the Separator Characters
- The following characters MUST NOT be percent-encoded:
  - the Alphanumeric Characters,
  - the Punctuation Characters,
  - the Separator Characters when being used as `purl` separators,
  - the colon ‘:’, whether used as a Separator Character or otherwise,
    and
  - the percent sign ‘%’ when used to represent a percent-encoded
    character.
- Where the space ’ ’ is permitted, it MUST be percent-encoded as ‘%20’.
- With the exception of the percent-encoding mechanism, the rules
  regarding percent-encoding are defined by this specification alone.

## 5.5 Case Folding

References to “lowercase” in this specification refer to the
**culture-invariant** full case mapping defined in [Section 3.13.2 of
the Unicode
Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G34078).

When applied to the ASCII character set, this operation converts
uppercase Latin letters (`A to Z`) to their corresponding lowercase
forms (`a to z`). All other ASCII characters remain unchanged.

## 5.6 Component-level Rules

A `purl` string is an ASCII URL string composed of seven components.

Except as expressly stated otherwise in this section, each component:

- MAY be composed of any of the characters defined in the “Permitted
  characters” section
- MUST be encoded as defined in the “Character encoding” section

The “lowercase” rules are defined in the “Case folding” section.

The rules for each component are:

- **scheme**:
  - The `scheme` is a constant with the value “pkg”.
  - The `scheme` MUST be followed by an unencoded colon ‘:’.
  - `purl` parsers MUST accept URLs where the `scheme` and colon ‘:’ are
    followed by one or more slash ‘/’ characters, such as ‘pkg://’, and
    MUST ignore and remove all such ‘/’ characters.
- **type**:
  - The package `type` MUST be composed only of ASCII letters and
    numbers, period ‘.’, and dash ‘-’.
  - The `type` MUST start with an ASCII letter.
  - The `type` MUST NOT be percent-encoded.
  - The `type` is case insensitive. The canonical form is lowercase.
- **namespace**:
  - The `namespace` is optional, unless required by the package’s `type`
    definition.
  - If present, the `namespace` MAY contain one or more segments,
    separated by a single unencoded slash ‘/’ character.
  - All leading and trailing slashes ‘/’ are not significant and SHOULD
    be stripped in the canonical form. They are not part of the
    `namespace`.
  - Each `namespace` segment MUST be a percent-encoded string.
  - When percent-decoded, a segment:
    - MUST NOT contain any slash ‘/’ characters
    - MUST NOT be empty
    - MAY contain any Unicode character other than ‘/’ unless the
      package’s `type` definition provides otherwise.
  - A URL host or Authority MUST NOT be used as a `namespace`. Use
    instead a `repository_url` qualifier. Note however that for some
    types, the `namespace` may look like a host.
- **name**:
  - The `name` is prefixed by a single slash ‘/’ separator when the
    `namespace` is not empty.
  - All leading and trailing slashes ‘/’ are not significant and SHOULD
    be stripped in the canonical form. They are not part of the `name`.
  - A `name` MUST be a percent-encoded string.
  - When percent-decoded, a `name` MAY contain any Unicode character
    unless the package’s `type` definition provides otherwise.
- **version**:
  - The `version` is prefixed by a ‘@’ separator when not empty.
  - This ‘@’ is not part of the `version`.
  - A `version` MUST be a percent-encoded string.
  - When percent-decoded, a `version` MAY contain any Unicode character
    unless the package’s `type` definition provides otherwise.
  - A `version` is a plain and opaque string.
- **qualifiers**:
  - The `qualifiers` component MUST be prefixed by an unencoded question
    mark ‘?’ separator when not empty. This ‘?’ separator is not part of
    the `qualifiers` component.
  - The `qualifiers` component is composed of one or more `key=value`
    pairs. Multiple `key=value` pairs MUST be separated by an unencoded
    ampersand ‘&’. This ‘&’ separator is not part of an individual
    `qualifier`.
  - A `key` and `value` MUST be separated by the unencoded equal sign
    ‘=’ character. This ‘=’ separator is not part of the `key` or
    `value`.
  - A `value` MUST NOT be an empty string: a `key=value` pair with an
    empty `value` is the same as if no `key=value` pair exists for this
    `key`.
  - For each `key=value` pair:
    - The `key` MUST be composed only of lowercase ASCII letters and
      numbers, period ‘.’, dash ‘-’ and underscore ’\_’.
    - A `key` MUST start with an ASCII letter.
    - A `key` MUST NOT be percent-encoded.
    - Each `key` MUST be unique among all the keys of the `qualifiers`
      component.
    - A `value` MAY contain any Unicode character and all characters
      MUST be encoded as described in the “Character encoding” section.
- **subpath**:
  - The `subpath` string is prefixed by a ‘\#’ separator when not empty
  - This ‘\#’ is not part of the `subpath`
  - The `subpath` contains zero or more segments, separated by slash ‘/’
  - Leading and trailing slashes ‘/’ are not significant and SHOULD be
    stripped in the canonical form
  - Each `subpath` segment MUST be a percent-encoded string
  - When percent-decoded, a segment:
    - MUST NOT contain any slash ‘/’ characters
    - MUST NOT be empty
    - MUST NOT be any of ‘..’ or ‘.’
    - MAY contain any Unicode character other than ‘/’ unless the
      package’s `type` definition provides otherwise.
  - The `subpath` MUST be interpreted as relative to the root of the
    package
