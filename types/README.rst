=============================
Canonical PURL Type Definitions
=============================

This directory contains the **canonical machine-readable definitions** of all known Package-URL (PURL) types. These JSON files serve as the **source of truth** for PURL type specifications.

Contents:
---------
- **index.json**: The **canonical index** of all PURL types.
- **<purl-type>.json**: The **canonical definition** for a specific PURL type (e.g., `maven.json`, `npm.json`).

Canonical Definitions:
----------------------
Each JSON file in this directory follows the standard **PURL Type Definition Schema**, ensuring:

- **Consistency** across all PURL types.
- **Machine-readability** for validation and automation.
- **Standardized structure** defining namespace, name, version, qualifiers, subpath, and repository behavior.

Usage:
------
- These files should be **used as the authoritative source** for defining and validating PURLs.
- They should be referenced by tools, libraries, and documentation generators.

Contributions:
--------------
- **Modifications must be made to these JSON files directly**.
- Any changes should be **reviewed and approved** to maintain consistency.
- If you need to propose a new PURL type, **follow the contribution guidelines** in the repository.
