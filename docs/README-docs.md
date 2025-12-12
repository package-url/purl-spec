This README explains the organization of documentation files for the PURL 
specification.

## ECMA-427 documentation
The `purl-spec/docs/standard` folder has markdown files with text that match the content of [ECMA-427](https://ecma-international.org/publications-and-standards/standards/ecma-427/) which is the first edition of the Package-URL 
Specification standard. These files map to ECMA-427 document as follows:

- About this specification: `about.md`
- Introduction: `introduction.md`
- Clause 1 Scope: `scope.md`
- Clause 2 Conformance: `conformance.md`
- Clause 3 Normative references: `refererences.md`
- Clause 4 Overview: `overview.md`
- Clause 5 Package-URL specification: `specification.md`
- Clause 6 Package-URL Type Definition Schema: `type-definition-schema.md`

ECMA-427 is the official documention for the 1st edition of the PURL
Specification standard. The source for this documentation is located at:
https://github.com/Ecma-TC54/ECMA-427/blob/main/spec.html. The text stored in
purl-spec/docs/standard/` matches the official text with following exceptions:
- The text does not include the clause numbering from ECMA-427. This 
numbering is automatically added by the Ecma tools for publishing an Ecma
standard.
- `docs/standard/type-definition-schema.md` only has the introductory text
from ECMA-427 Clause 6 because Clause 6 presents the PURL Type Definition 
Schema in a "human-friendly" format that is difficult to reproduce in
markdown. The equivalent information is in this repository in JSON Schema 
format: at `purl-spec/schemas/purl-type-definition.schema-1.0.json`

The purpose of keeping a copy of the ECMA-427 text here is to make it easier
to track any proposed changes to the PURL specification that will affect
the ECMA-427 standard. Any such changes need to be tracked and approved for
a future 2nd edition of the ECMA-427 standard.

## PURL specification documentation
The other files in `purl-spec/docs` are also specification documentation, but 
they are not part of the ECMA-427 1st edition standard. Most of the documents
provide information to support implementation of the PURL Specification in 
other software or databases.

