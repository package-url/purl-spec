<!--
  ~ SPDX-License-Identifier: MIT
  -->
## Normalization and validation of `purl` components

Components produced by a conforming PURL parser are already valid and normalized.  
However, when components come from other sources, they may require additional normalization and validation.

The following rules apply (all components are assumed to be in percent-decoded form):

- **type**
    - Convert to lowercase.
    - Validate against the allowed character set: `[a-z0-9.-]`.

- **namespace** as string:
    - Split on `/`.
    - Normalize and validate each segment.

- **namespace** segments:
    - Remove any empty segments.
    - Apply type-specific normalization and validation.

- **name**
    - Apply type-specific normalization and validation.

- **version**
    - Apply type-specific normalization and validation.

- **qualifiers**
    - Discard key–value pairs with an empty `value`.
    - For each pair:
        - Convert `key` to lowercase.
        - Validate `key` against the allowed character set: `[a-z0-9._-]`.

- **subpath** as string:
    - Split on `/`.
    - Normalize and validate each segment.

- **subpath** segments:
  - Remove any segment that is empty, `.` or `..`.
  - Apply type-specific normalization and validation.
