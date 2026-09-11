<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: huggingface

- **Type Name:** HuggingFace models
- **Description:** Hugging Face packages, including models, datasets, and spaces
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
- **Native Label:** repository username or organization
- **Note:** `The namespace is the repository username or organization, if present. It is case sensitive.`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** repository name
- **Note:** `The name is the repository name. It is case sensitive.`

## Version definition

- **Requirement:** Optional
- **Case Sensitive:** Yes
- **Native Label:** revision Git commit hash or tag
- **Note:** `The version is a revision Git commit hash or tag. Tags are case sensitive and must be preserved as-is. Commit hashes are hexadecimal and shall be lowercased in the package URL.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| type | Optional |  | model | The type is the kind of Hugging Face repository: model (default), dataset, or space. |

## Examples

- `pkg:huggingface/distilbert/distilbert-base-uncased@043235d6088ecd3dd5fb5ca3592b6913fd516027`
- `pkg:huggingface/microsoft/deberta-v3-base@559062ad13d311b87b2c455e67dcd5f1c8f65111?repository_url=https:%2F%2Fhub-ci.huggingface.co`
- `pkg:huggingface/LumiOpen/Poro-34B@14d8824c28d782fcd1cd9579ac06644f60e62450`
- `pkg:huggingface/LumiOpen/Poro-34B@100B?type=model`
- `pkg:huggingface/bigcode/the-stack@v1.1?type=dataset`
- `pkg:huggingface/black-forest-labs/FLUX.1-Kontext-Dev?type=space`
