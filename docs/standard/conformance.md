# 2 Conformance

## 2.1 Requirements Terminology

In this standard, the words that are used to define the significance of each requirement are detailed below. These words are used in accordance with their definitions in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt), and their respective meanings are reproduced below:

* Must: This word, or the adjective “required” and the auxiliary verb "shall", means that the item is an absolute requirement of the standard.
* Should: This word, or the adjective “recommended”, means that there might exist valid reasons in particular circumstances to ignore this item, but the full implications should be understood and the case carefully weighed before making an implementation decision.
* May: This word, or the adjective “optional”, means that this item is truly optional.

The words "must not", "shall not", "should not", and "not recommended", are the negative forms of "must", "shall", "should", and "recommended", respectively. There is no negative form of "may".

## 2.2 Implementation Conformance

A conforming implementation of Package-URL (PURL) must fully implement and support all elements defined within this specification, including the syntax, components, and semantic requirements for constructing and interpreting valid PURLs.

A conforming implementation of PURL must adhere to the syntax defined in this specification, ensuring that all PURLs are parsed, constructed, and validated according to the prescribed rules. The implementation must provide full support for ecosystem-agnostic behaviour, enabling PURLs to function consistently and reliably across diverse environments.

All required components of a PURL, such as the scheme, type, and name, must be present and validated according to the rules defined in this specification. Additionally, optional components, including qualifiers and subpaths, must be handled appropriately if provided, in full compliance with their specified behaviours.

Implementations must ensure that equivalent PURLs are consistently resolved to the same canonical representation. This includes strict adherence to normalisation and equivalence rules. Furthermore, implementations must process URI encoding and decoding for PURL components according to the standards outlined in RFC 3986.

Invalid PURLs that fail to conform to the specification must be identified and rejected by any conforming implementation. This guarantees the integrity and reliability of PURLs in all supported contexts.

A conforming implementation of PURL may extend its functionality by providing ecosystem-specific validation, processing, or metadata handling, as long as these extensions do not violate the core specification. Additionally, implementations may offer auxiliary tools or features, such as utilities for constructing or validating PURLs, provided they align with the standard's requirements.

A conforming implementation must not redefine or alter the core syntax, components, or semantics defined by this specification. Any prohibited extensions explicitly identified in the specification must not be implemented. Furthermore, behaviours that compromise the interoperability of PURLs across tools, platforms, or ecosystems are strictly disallowed.

A conforming implementation of Package-URL may choose to implement or not implement Normative Optional subclauses. If any Normative Optional behaviour is implemented, all of the behaviour in the containing Normative Optional clause must be implemented. A Normative Optional clause is denoted in this specification with the words "Normative Optional" in a coloured box, as shown below.

## 2.3 Example Normative Optional Clause Heading

Example clause contents.

