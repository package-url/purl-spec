## Package-URL Type definitions

Each package manager, platform, type, or ecosystem has its own conventions
and protocols to identify, locate, and provision software packages.

The package **type** is the component of a Package-URL that is used to
capture this information with a short string such as ``maven``, ``npm``,
``nuget``, ``gem``, ``pypi``, etc.

These are registered ``PURL`` package type definitions.

Definitions can also include types reserved for future use.

This document no longer contains a manually maintained list of PURL types.

Instead, all PURL type definitions are now maintained in a simple JSON
document with automatically generated documentation.

## Where to find PURL Type information

- In the JSON Index listing of all defined PURL types at:
  `/purl-types-index.json <https://github.com/package-url/purl-spec/tree/main/purl-types-index.json>`_

- In individual JSON files, one for each PURL type definition at:
  `/types <https://github.com/package-url/purl-spec/tree/main/types>`_

- As Markdown documentation, generated from for each PURL type JSON
  definition at:
  `/types-doc <https://github.com/package-url/purl-spec/tree/main/types-doc>`_
