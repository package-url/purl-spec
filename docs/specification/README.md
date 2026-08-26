This README explains the organization of documentation files for the PURL
specification.

# PURL specification documentation

There are two levels of PURL specification documentation:
- The `docs/specification/standard` folder has markdown files with text that
  matches the content of [ECMA-427](https://ecma-international.org/publications-and-standards/standards/ecma-427/).
- The other files in the `docs/specification` folder are also
  specification documentation, but they are not part of the ECMA-427 1st Edition
  Standard. These documents provide information to support implementation
  of the PURL Specification in other software or databases.

## ECMA-427 documentation
ECMA-427 is the official documentation for the 1st edition of the Package-URL
(PURL) Specification Standard. The source for this documentation is located
at: https://github.com/Ecma-TC54/ECMA-427/blob/main/spec.html. The text from
this HTML file is processed with several Ecma tools to produce a PDF file that
is available from: https://tc54.org/purl/ and an HTML version at: https://ecma-tc54.github.io/ECMA-427/.
These files map to ECMA-427 1st edition as follows:

- About this specification: `About.md`
- Introduction: `Introduction.md`
- Clause 1 Scope: `Clause-1-Scope.md`
- Clause 2 Conformance: `Clause-2-Conformance.md`
- Clause 3 Normative references: `Clause-3-Normative-References.md`
- Clause 4 Overview: `Clause-4-Overview.md`
- Clause 5 Package-URL specification: `Clause-5-Package-URL-Specification.md`
- Clause 6 Package-URL Type Definition Schema: `Clause-6-Package-URL-Type-Definition-Schema.md`
- Annex A (normative) PURL Type Definition: `Annex-A-PURL-Type-Definition.md`
- New for ECMA-427 2nd Edition
  - Annex B (informative) PURL Standard Qualifiers: `Annex-B-Recommended-Qualifiers.md`
  - Annex C (informative) PURL ABNF Grammar: *tbd*
  
The text in the `docs/specification/standard` files matches the official text
with the following exceptions:
- examples are left-justified, not centered, to avoid using HTML tags for centering
- the use of italics instead of intra-document links
- some other formatting differences between the official Ecmarkup format and markdown

The purpose of keeping a copy of the ECMA-427 1st Edition text here is to track
changes at a more modular level than the EMCA-427 "source" code at: https://github.com/Ecma-TC54/ECMA-427/blob/main/spec.html

