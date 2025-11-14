<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: pypi

- **Type Name:** PyPI
- **Description:** Python packages
- **Schema ID:** `https://packageurl.org/types/pypi-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:pypi/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://pypi.org
- **Note:** Previously https://pypi.python.org

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Requirement:** Required
- **Normalization rules:**
  - Replace underscore _ with dash -
  - Replace dot . with underscore _ when used in distribution (sdist, wheel) names
- **Native Label:** name
- **Note:** `PyPI treats - and _ as the same character and is not case sensitive. Therefore a PyPI package name must be lowercased and underscore _ replaced with a dash -. Note that PyPI itself is preserving the case of package names. When used in distribution and wheel names, the dot . is replaced with an underscore _`

## Version definition

- **Requirement:** Optional
- **Native Label:** version

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| file_name | Optional |  |  | The file_name qualifier selects a particular distribution file (case-sensitive). For naming convention, see the Python Packaging User Guide on source distributions https://packaging.python.org/en/latest/specifications/source-distribution-format/#source-distribution-file-name and on binary distributions https://packaging.python.org/en/latest/specifications/binary-distribution-format/#file-name-convention and the rules for platform compatibility tags https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/ |

## Examples

- `pkg:pypi/django@1.11.1`
- `pkg:pypi/django@1.11.1?file_name=Django-1.11.1.tar.gz`
- `pkg:pypi/django@1.11.1?file_name=Django-1.11.1-py2.py3-none-any.whl`
- `pkg:pypi/django-allauth@12.23`
