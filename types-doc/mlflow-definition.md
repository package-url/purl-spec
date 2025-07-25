<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: mlflow

- **Type Name:** 
- **Description:** MLflow ML models (Azure ML, Databricks, etc.)
- **Schema ID:** `https://packageurl.org/types/mlflow-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:mlflow/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** The repository is the MLflow tracking URI. There is no default. Some examples include Azure ML https://<region>.api.azureml.ms/mlflow/v1.0/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name> and Azure Databricks https://adb-<numbers>.<number>.azuredatabricks.net/api/2.0/mlflow and AWS Databricks https://dbc-<alphanumeric>-<alphanumeric>.cloud.databricks.com/api/2.0/mlflow and GCP Databricks https://<numbers>.<number>.gcp.databricks.com/api/2.0/mlflow

## Namespace definition

- **Requirement:** Prohibited
- **Note:** `there is no namespace`

## Name definition

- **Note:** `The name is the model name. Case sensitivity depends on the server implementation, such as for Azure ML, it is case sensitive and must be kept as-is in the package URL; and for Databricks, it is case insensitive and must be lowercased in the package URL.`

## Version definition

- **Native Label:** version
- **Note:** `The version is the model version.`

## Qualifiers Definition

| Key  | Requirement | Native name | Default Value | Description |
|------|-------------|-------------|---------------|-------------|
| model_uuid | Optional | model_uuid |  | model_uuid as defined in the MLflow documentation. |
| run_id | Optional | run_id |  | run_id as defined in the MLflow documentation. |

## Examples

- `pkg:mlflow/creditfraud@3?repository_url=https://westus2.api.azureml.ms/mlflow/v1.0/subscriptions/a50f2011-fab8-4164-af23-c62881ef8c95/resourceGroups/TestResourceGroup/providers/Microsoft.MachineLearningServices/workspaces/TestWorkspace`
- `pkg:mlflow/trafficsigns@10?model_uuid=36233173b22f4c89b451f1228d700d49&run_id=410a3121-2709-4f88-98dd-dba0ef056b0a&repository_url=https://adb-5245952564735461.0.azuredatabricks.net/api/2.0/mlflow`
