# ECMA-427 2nd Edition Release notes

## Summary
The 2nd Edition of ECMA-427 for Package-URL (PURL) is a minor update for
the specification that affects six elements of the specification as follows:
- Clause 3 Normative References
- Clause 5 Package-URL Specification
- Clause 6 Package-URL Type Definition Schema
- Annex A (normative) PURL Type Definition
- Annex B (informative) Recommended Qualifiers
- Annex C (informative) ABNF Grammar

## Clause 3 Normative References
The change adds 2 new references related to the new ABNF Grammar in Annex
C. The new references are:
- RFC 3629, UTF-8, a transformation format of ISO 10646
  https://datatracker.ietf.org/doc/html/rfc3629
- RFC 5234, Augmented BNF for Syntax Specifications: ABNF
  https://datatracker.ietf.org/doc/html/rfc5234

## Clause 5 Package-URL Specification
The changes are:
- Updated **Clause 5.1 A PURL is a URL** because not every PURL **type** has a
  default repository location.

  Changed from:

      - A PURL is a valid URL because it is a locator even though it has no
        Authority URL component: each type has a default repository location
        when defined.
  To:

      - A PURL is a valid URL because it is a locator even though it has no
        Authority URL component: a default repository location may be defined
        for a PURL type.

- Updated **Clause 5.1 A PURL is a URL** by adding the following text at the
  end of the clause to clarify how and where a PURL is a locator.

    - A PURL should be a locator based on three paths to specify or derive a
      URL:
      - A default repository location should be defined for a PURL **type**.
      - A repository URL or a download URL may be defined as a **qualifier**
        for a PURL **type**.
      - A package ecosystem may provide a mechanism to derive the locator
        based on a set of PURL components.

- Updated **Clause 5.6.1 Scheme** for the last list item to change "shall"
  (i.e. required behaviour) to "should" (recommended behaviour).

  Changed from:

      - PURL parsers shall accept URLs where the **scheme** and colon ':' are
        followed by one or more slash '/' characters, such as 'pkg://', and
        shall ignore and remove all such '/' characters.
  To:

      - PURL parsers should accept URLs where the **scheme** and colon ':' are
        followed by one or more slash '/' characters, such as 'pkg://', and
        should ignore and remove all such '/' characters.


- Added **Clause 5.7 PURL type definitions** to document the meaning of
  "registered" PURL **type** definitions. The new text is:

    This Standard includes the Package-URL Type Definition Schema but it does
    not include the set of current "registered" PURL **type** (JSON format) definition files because there are ongoing additions and changes to these files. The set of current "registered" PURL **type** definition files are located at: https://www.packageurl.org/purl-types/.
    Registration refers to the Package-URL community process for adding a new PURL **type**.

    There are two rules related to the set of registered PURL **type**
    definitions for conforming PURL implementations to validate the PURL
    **type** component of a PURL:
    - If the PURL **type** is registered, then the PURL is invalid if it does
      not conform to all of the rules from the corresponding PURL **type** definition.
    - If the PURL **type** is not registered, then the **type** component is
      valid if it conforms to the rules stated in the _Type_ component rules
      in this Clause of the Standard. In this case an implementation should report a warning that the PURL **type** is not registered.

- Made some editorial improvements.

## Clause 6 Package-URL Type Definition Schema
ECMA-427 2nd Edition implements `purl-type-definition.schema-1.1.json` as an
update to `purl-type-definition.schema-1.0.json` from the 1st Edition.

The changes are:
- Added a heading for the root object at the top of the schema and text to
  document the JSON Schema version and location of PURL **type** definition
  schema files:

    6.1 JSON Schema
    The PURL Type Definition Schema is formally specified by a Draft 07 JSON Schema. Each published version of this specification is accompanied by a versioned meta-schema at a stable URI:

    https://packageurl.org/purl-schemas/purl-type-definition.schema-..json

- Applied the schema changes from `purl-type-definition.schema-1.1.json`:

  - Updated "$schema": "http://json-schema.org/draft-07/schema#" to
    "$schema": "https://json-schema.org/draft-07/schema#."

  - Added "registered_values" as a property for the **namespace** component to
    implement an option to register a set of specific **namespace** values for
    a PURL **type**. If **namespace** values are registered for a PURL
    **type**, a tool should report a warning if the **namespace** value is not one of the registered values. The "registered_values" property is an
    array with three items (strings):
     - "value": "Registered namespace value for this PURL type."
     - "description": "Explanation of what this namespace value means for this
       PURL type."
     - "reference_url": "Optional Reference URL for where this namespace value
       is defined for this PURL type."

  - Added a schema-level "definition" for "recommended_requirement". The other
    requirement definitions are: "optional_requirement",
    "required_requirement", and "prohibited_requirement".
  - Added "recommended_requirement" as an option for the "requirement"
    (**qualifier key** requirement) property of the **qualifiers** component.
    A PURL **qualifier key** is now optional, recommended or required. A tool should report a warning if a PURL **qualifier key** is recommended for a
    PURL **type** but not present in a subject PURL.

## Annex A (normative) PURL Type Definition
The changes are to update the JSON file text to match `purl-type-definition.schema-1.1.json`.

## Annex B (informative) Recommended Qualifiers
Annex B is a new informative Annex that documents the recommended definitions
for common **qualifiers** that are used across many PURL **types**.

## Annex C (informative) ABNF Grammar
Annex C is a new informative Annex that documents the Augmented Backus Naur
Form (ABNF) grammar for PURL strings.
