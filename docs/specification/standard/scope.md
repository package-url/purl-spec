# Scope
This Standard defines the Package-URL (PURL) syntax for identifying software 
packages independently from their ecosystem or distribution channel. PURL is 
used to identify software packages across software supply chains supporting 
many use cases, identifying software packages in Software Bills of Materials, 
vulnerability databases, vulnerability advisories, vulnerability disclosures 
and exploitability reports, and managing software package dependencies.

A PURL is a valid URL and URI composed of seven components to identify a 
software package. The PURL type component defines the ecosystem-specific 
structure and meaning for the other PURL components. This Standard specifies 
the syntax for PURLs and the schema for defining PURL types, but it does not 
include any specific PURL type definitions, such as maven, pypi or npm.