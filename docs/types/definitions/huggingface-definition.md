<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: huggingface

- **Type Name:** HuggingFace models
- **Description:** Hugging Face ML models
- **Schema ID:** `https://packageurl.org/types/huggingfaces-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:huggingface/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** The default repository is https://huggingface.co.

## Namespace definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** model repository username or organization
- **Note:** `The namespace is the model repository username or organization, if present. It is case sensitive.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** model repository name
- **Note:** `The name is the model repository name. It is case sensitive.`

## Version definition

- **Requirement:** Optional
- **Native Label:** model revision Git commit hash
- **Note:** `The version is the model revision Git commit hash. It is case insensitive and must be lowercased in the package URL.`

## Examples

- `pkg:huggingface/distilbert-base-uncased@043235d6088ecd3dd5fb5ca3592b6913fd516027`
- `pkg:huggingface/microsoft/deberta-v3-base@559062ad13d311b87b2c455e67dcd5f1c8f65111?repository_url=https://hub-ci.huggingface.co`
