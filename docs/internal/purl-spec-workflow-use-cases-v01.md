# purl-spec workflow use cases

## 1. Add new PURL type

### User

- Setup development environment: run `make conf`

- Add schema definition: `types/<type>-definition.json`

- Add test case(s) data file: `tests/types/<type>-test.json`

- Validate schemas and data files: run `make check`

  - Calls `checkjson`:
    - Validates that every `*.json` file in `schemas/` is itself a valid JSON Schema
    - Validates `purl-types-index.json` against `purl-types-index.schema-1.0.json`.
    - Validates every `*-definition.json` file in `types/` against `purl-type-definition.schema-1.0.json`.
    - Validates all `*-test.json` files inside `tests/spec` and `tests/types` against `purl-test.schema-0.1.json`.

      - Does not validate whether tests comply with the related `*-definition.json` schema file.  Note that the `README-dev.md` says `make check` will "validate that ... data files are correct." -- we need to clarify what we mean by "are correct".

      - Does not check for missing test files, e.g., a new `types/<type>-definition.json` file submitted without companion test file `tests/types/<type>-test.json` should (but does not currently) inform the user that their submission must/shall be accompanied by a test file.

  - Calls `checkcode`: checks that the `.py` files in `etc/scripts` follow project format standards.

- Regenerate Python utility model code (Pydantic model classes) from JSON schemas: run `make gencode`

- Regenerate the PURL `type` .md documentation from the JSON PURL `type` definition files: run `make gendocs`

- Commit, push, open PR

### GitHub CI/workflow

- `.github/workflows/generate-index-and-docs.yml` (currently disabled):

  - x

  - x

---

## 2. Add or update JSON Schema file(s)

### User

- Setup development environment including `make conf`

### GitHub CI/workflow

- x

---

## 3. Add or update JSON data file(s) - including the type definition or test files

### User

- Setup development environment including `make conf`

### GitHub CI/workflow

- x

---

## 4. Add or update .md documentation file(s)

### User

- Setup development environment including `make conf`

### GitHub CI/workflow

- x
