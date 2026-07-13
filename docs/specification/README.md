This README explains the organization of documentation files for the PURL 
specification.

# PURL specification documentation

There are two levels of PURL specification documentation:
- The `docs/specification/standard` folder has markdown files with text that 
match the content of [ECMA-427](https://ecma-international.org/publications-and-standards/standards/ecma-427/).
- The other files in the `docs/specification` folder are also 
specification documentation, but they are not part of the ECMA-427 1st edition 
Standard. These documents provide information to support implementation 
of the PURL Specification in other software or databases.

## ECMA-427 documentation
ECMA-427 is the official documentation for the 1st edition of the Package-URL 
(PURL) Specification Standard. The source for this documentation is located 
at: https://github.com/Ecma-TC54/ECMA-427/blob/main/spec.html. The text from 
this HTML file is processed with several Ecma tools to produce a PDF file that
is available from: https://tc54.org/purl/. We have validated the text in the 
files in the `docs/specification/standard` folder against the PDF.
These files map to ECMA-427 1st edition as follows:

- Introduction: `introduction.md`
- About this specification: `about.md`
- Clause 1 Scope: `scope.md`
- Clause 2 Conformance: `conformance.md`
- Clause 3 Normative references: `references.md`
- Clause 4 Overview: `overview.md`
- Clause 5 Package-URL specification: `specification.md`
- Clause 6 Package-URL Type Definition Schema: `type-definition-schema.md`

The text in the `docs/standard/` files matches the official text with 
the following exceptions:
- The text does not include the clause numbering from ECMA-427. This 
numbering is automatically added by the Ecma tools for publishing an Ecma
standard.
- `type-definition-schema.md` only has the introductory text from ECMA-427 
Clause 6 because Clause 6 presents the PURL Type Definition Schema in a 
"human-friendly" format that is difficult to reproduce in markdown format.
The equivalent information is in this repository in JSON Schema 
format: at `schemas/purl-type-definition.schema-1.0.json`
- There are some minor formatting differences such as the examples in Clause 5 
and the use of italics instead of intra-document links.

The purpose of keeping a copy of the ECMA-427 text here is to make it easier
to track any proposed changes to the PURL specification that will affect
the ECMA-427 Standard. Any such changes need to be tracked and approved for
a future 2nd edition of the ECMA-427 Standard. 

**NB:** Some files in the `docs` folder contain "front matter" that
is used for publishing the content on the www.packageurl.org website. 
The "front matter" layout is:
| id | title | sidebar_label | hide_table_of_contents |
| -- | ----- | ------------- | ---------------------- |
|    |       |               |                        |
			


