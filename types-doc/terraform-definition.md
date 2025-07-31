<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: terraform

- **Type Name:** Terraform providers and modules
- **Description:** Terraform providers and modules
- **Schema ID:** `https://packageurl.org/types/terraform-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:terraform/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://registry.terraform.io
- **Note:** The HashiCorp registry is the default. Use the standard repository_url qualifier to point to another registry.

## Namespace definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Note:** `The namespace is the provider or module namespace, which is usually the organization or vendor name.`

## Name definition

- **Case Sensitive:** Yes
- **Native Label:** Name is the name of the terraform provider or module.

## Version definition

- **Case Sensitive:** Yes
- **Native Label:** Version is the package version and is required.

## Examples

- `pkg:terraform/hashicorp/aws@6.0.0`
- `pkg:terraform/terraform-aws-modules/vpc@6.0.1`
- `pkg:terraform/terraform-aws-modules/vpc@6.0.1?registry_url=https://registry.example.com`
