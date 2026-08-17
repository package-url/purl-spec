# Conformance

A conforming implementation of Package-URL (PURL) shall fully implement and
support all elements defined within this Standard, including the syntax,
components, and semantic requirements for constructing and interpreting valid
PURLs.

A conforming implementation of PURL shall adhere to the syntax defined in this
Standard, ensuring that all PURLs are parsed, constructed, and validated
according to the prescribed rules. The implementation shall provide full
support for ecosystem-agnostic behaviour, enabling PURLs to function
consistently and reliably across diverse environments.

All required components of a PURL, such as the scheme, type, and name, shall
be present and validated according to the rules defined in this
Standard. Additionally, optional components, including qualifiers and
subpaths, shall be handled appropriately if provided, in full compliance with
their specified behaviours.

Implementations shall ensure that equivalent PURLs are consistently resolved
to the same canonical representation. This includes strict adherence to
normalisation and equivalence rules. Furthermore, implementations shall
process URI encoding and decoding for PURL components according to the
standards outlined in RFC 3986.

Invalid PURLs that fail to conform to the specification shall be identified
and rejected by any conforming implementation. This guarantees the integrity
and reliability of PURLs in all supported contexts.

A conforming implementation of PURL may extend its functionality by providing
ecosystem-specific validation, processing, or metadata handling, as long as
these extensions do not violate the core specification. Additionally,
implementations may offer auxiliary tools or features, such as utilities for
constructing or validating PURLs, provided they align with the standard's
requirements.

A conforming implementation shall not redefine or alter the core syntax,
components, or semantics defined by this Standard. Any prohibited
extensions explicitly identified in the specification shall not be
implemented. Furthermore, behaviours that compromise the interoperability of
PURLs across tools, platforms, or ecosystems are strictly disallowed.