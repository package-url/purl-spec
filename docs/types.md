## Package-URL type definitions

Each package manager, platform, type, or ecosystem has its own conventions
and protocols to identify, locate, and provision software packages.

The package **type** is the component of a Package-URL that is used to
capture this information with a short string such as 'maven', 'npm',
'nuget', 'gem', 'pypi', etc.

PURL type definitions are maintained in a set of JSON Schema files with a
separate file for each PURL **type**. Each PURL **type** has a corresponding
file of automatically generated documentation. There is also a simple index
of all currently registered purl types.

## Where to find PURL type information

- In individual JSON files, one for each PURL **type** definition at:
  https://github.com/package-url/purl-spec/tree/main/types

- As Markdown documentation, generated from each PURL **type** JSON
  definition at:
  https://github.com/package-url/purl-spec/tree/main/types-doc

- In the JSON Index listing of all registered PURL types at:
  https://github.com/package-url/purl-spec/tree/main/purl-types-index.json
