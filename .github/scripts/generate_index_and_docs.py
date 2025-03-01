import os
import json
from datetime import datetime, UTC

TYPES_DIR = "types"
DOCS_DIR = os.path.join(TYPES_DIR, "docs")
INDEX_FILE = os.path.join(TYPES_DIR, "index.json")

# Ensure the docs directory exists
os.makedirs(DOCS_DIR, exist_ok=True)


def get_current_timestamp():
    """Returns the current UTC timestamp in ISO 8601 format with 'Z' notation."""
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def generate_index(types_data):
    """Generates index.json with all known PURL types and updates the timestamp."""
    index_data = {
        "$schema": "https://purl-spec.org/schemas/purl-type-index.schema-1.0.json",
        "$id": "https://purl-spec.org/types/index.json",
        "title": "Package-URL Type Index",
        "description": "The canonical index of all known PURL types and their definitions. This index is auto-generated and should not be manually edited.",
        "last_updated": get_current_timestamp(),
        "types": types_data
    }

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2)

    print(f"✅ index.json updated successfully. Last updated: {index_data['last_updated']}")


def generate_purl_syntax(data):
    """Generates the PURL syntax dynamically based on required, optional, and prohibited parts."""
    definition = data.get("definition", {})

    # Start building the PURL syntax
    purl_syntax = "pkg:" + data.get("type", "unknown")

    # Namespace
    namespace = definition.get("namespace", {}).get("requirement", "optional")
    if namespace in ["required", "optional"]:
        purl_syntax += "/<namespace>"

    # Name (always required)
    purl_syntax += "/<name>"

    # Version (no `/` before `@`)
    version = definition.get("version", {}).get("requirement", "optional")
    if version in ["required", "optional"]:
        purl_syntax += "@<version>"

    # Qualifiers (no `/` before `?`)
    qualifiers_exist = "qualifiers" in definition and definition["qualifiers"]
    if qualifiers_exist:
        purl_syntax += "?<qualifiers>"

    # Subpath (no `/` before `#`)
    subpath = definition.get("subpath", {}).get("requirement", "optional")
    if subpath in ["required", "optional"]:
        purl_syntax += "#<subpath>"

    return purl_syntax


def generate_documentation(data):
    """Generates markdown documentation for a PURL type, covering all fields in the schema."""
    doc_filename = os.path.join(DOCS_DIR, f"{data['type']}.md")

    with open(doc_filename, "w", encoding="utf-8") as doc:
        # Header
        doc.write(f"# PURL Type Definition: {data.get('type', 'Unknown')}\n\n")
        doc.write(f"**Name:** {data.get('name', 'Unknown')}\n\n")
        doc.write(f"**Description:** {data.get('description', 'No description available.')}\n\n")
        doc.write(f"**Schema ID:** `{data.get('$id', 'Unknown')}`\n\n")

        # Generate PURL Syntax
        purl_syntax = generate_purl_syntax(data)
        doc.write("## PURL Syntax\n\n")
        doc.write("The structure of a PURL for this package type is:\n\n")
        doc.write("```\n")
        doc.write(purl_syntax + "\n")
        doc.write("```\n\n")

        # Ensure "definition" exists before trying to access its properties
        definition = data.get("definition", {})

        # PURL Components (Each gets its own section)
        for key in ["namespace", "name", "version"]:
            if key in definition:
                component = definition[key]
                doc.write(f"## {key.capitalize()}\n\n")

                doc.write(f"- **Requirement:** {component.get('requirement', 'optional').capitalize()}\n")

                allowed_chars = component.get("allowed_characters")
                if allowed_chars:
                    doc.write(f"- **Allowed Characters:** `{allowed_chars}`\n")

                case_rules = component.get("case_rules", {})
                sensitivity = case_rules.get("sensitivity")
                normalization = case_rules.get("normalization")

                if sensitivity:
                    doc.write(f"- **Case Sensitivity:** {sensitivity}\n")
                if normalization and normalization != "none":
                    doc.write(f"- **Normalization:** {normalization}\n")

                native_label = component.get("native_label")
                if native_label:
                    doc.write(f"- **Native Label:** {native_label}\n")

                doc.write("\n")

        # Subpath Section (if applicable)
        if "subpath" in definition:
            subpath = definition["subpath"]
            doc.write("## Subpath\n\n")
            doc.write(f"- **Requirement:** {subpath.get('requirement', 'optional').capitalize()}\n")
            if "native_label" in subpath:  # Only include if it exists
                doc.write(f"- **Native Label:** {subpath['native_label']}\n")
            doc.write(f"- **Description:** {subpath.get('description', 'No description provided.')}\n")
            doc.write("\n")

        # Qualifiers Table (if applicable)
        qualifiers = definition.get("qualifiers", [])
        if qualifiers:
            doc.write("## Qualifiers\n\n")
            doc.write("| Name | Requirement | Description |\n")
            doc.write("|------|-------------|-------------|\n")
            for qualifier in qualifiers:
                name = qualifier.get("name", "Unknown")
                requirement = qualifier.get("requirement", "optional").capitalize()
                description = qualifier.get("description", "No description provided.")
                doc.write(f"| {name} | {requirement} | {description} |\n")
            doc.write("\n")

        # Repository Section (if applicable)
        if "repository" in definition:
            repo = definition["repository"]
            doc.write("## Repository Information\n\n")
            doc.write(f"- **Uses Repository:** {'Yes' if repo.get('uses_repository', False) else 'No'}\n")
            if "default" in repo and repo["default"]:
                doc.write(f"- **Default Repository:** {repo['default'].get('name', 'Unknown')}\n")
                doc.write(f"  - **URL:** {repo['default'].get('url', 'Unknown')}\n")
                doc.write(f"  - **Description:** {repo['default'].get('description', 'No description provided.')}\n")
            if "description" in repo:
                doc.write(f"- **Additional Info:** {repo['description']}\n")
            doc.write("\n")

        # Examples Section (if applicable)
        examples = data.get("examples", [])
        if examples:
            doc.write("## Examples\n\n")
            for example in examples:
                doc.write(f"- `{example}`\n")
            doc.write("\n")

    print(f"✅ Documentation generated: {doc_filename}")


if __name__ == "__main__":
    types = []

    # Iterate through all JSON files in the types directory (excluding index.json)
    for filename in os.listdir(TYPES_DIR):
        if filename.endswith(".json") and filename != "index.json":
            filepath = os.path.join(TYPES_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Validate required fields
            if "type" not in data:
                print(f"⚠️ Skipping {filename}: Missing required fields.")
                continue

            # Add data to types list for index
            types.append({
                "type": data["type"],
                "description": data.get("description", ""),
                "definition_url": f"https://raw.githubusercontent.com/package-url/purl-spec/refs/heads/main/{filepath}"
            })

            # Generate documentation for this type
            generate_documentation(data)

    # Generate index file
    generate_index(types)
