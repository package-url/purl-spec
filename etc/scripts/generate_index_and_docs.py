#!/usr/bin/env python

import json
from pathlib import Path

"""
Generate Markdown documents, one for each PURL type definition JSON document.
"""


def generate_purl_syntax(definition) -> str:
    """
    Return a PURL syntax template generated dynamically from a definition object, using required,
    optional, and prohibited component definitions.
    """

    namespace = definition.get("namespace_definition", {}).get("requirement", "optional")
    if namespace in ["required", "optional"]:
        namespace = "/<namespace>"
    else:
        namespace = ""

    purl_syntax = f"pkg:{definition['type']}{namespace}/<name>@<version>?<qualifiers>#<subpath>"

    return purl_syntax


def get_yes_no(value):
    """Return a human-readable yes/no from a boolean value"""
    return "Yes" if value else "No"


def generate_documentation(definition) -> str:
    """
    Return a documentation for a PURL type definition.
    """
    lines = []
    lines.append("<!--  NOTE: Auto-generated from the JSON PURL type definition.")
    lines.append("Do not manually edit this file. Edit the JSON type definition instead. -->")
    lines.append("")

    lines.append(f"# PURL Type Definition: {definition['type']}")
    lines.append("")
    lines.append(f"- **Type Name:** {definition['type_name']}")
    lines.append(f"- **Description:** {definition['description']}")
    lines.append(f"- **Schema ID:** `{definition['$id']}`")
    lines.append("")

    # Generate PURL Syntax
    purl_syntax = generate_purl_syntax(definition)
    lines.append("## PURL Syntax")
    lines.append("")
    lines.append("The structure of a PURL for this package type is:")
    lines.append("")
    lines.append(f"    {purl_syntax}")
    lines.append("")

    # Repository comes 1st
    lines.append("## Repository Information")
    lines.append("")
    repository = definition["repository"]
    use_repository = repository["use_repository"]
    lines.append(f"- **Use Repository:** {get_yes_no(use_repository)}")
    if default_repository_url := repository.get("default_repository_url"):
        lines.append(f"- **Default Repository URL:** {default_repository_url}")
    if note := repository.get("note"):
        lines.append(f"- **Note:** {note}")
    lines.append("")

    # PURL Components (Each gets its own section)
    for key in [
        "namespace_definition",
        "name_definition",
        "version_definition",
        "subpath_definition",
    ]:
        component = definition.get(key)
        if not component:
            continue

        component_label = (" ".join(key.split("_"))).capitalize()
        lines.append(f"## {component_label}")
        lines.append("")

        if req := component.get("requirement"):
            # only for namespace
            lines.append(f"- **Requirement:** {req.capitalize()}")

        if permitted_characters := component.get("permitted_characters"):
            lines.append(f"- **Permitted Characters:** `{permitted_characters}`")

        if case_sensitive := component.get("case_sensitive"):
            lines.append(f"- **Case Sensitive:** {get_yes_no(case_sensitive)}")

        if normalization_rules := component.get("normalization_rules"):
            lines.append(f"- **Normalization rules:**")
            for rule in normalization_rules:
                lines.append(f"  - {rule}")

        if native_name := component.get("native_name"):
            lines.append(f"- **Native Label:** {native_name}")

        if note := component.get("note"):
            lines.append(f"- **Note:** `{note}`")

        lines.append("")

    if qualifiers := definition.get("qualifiers_definition"):
        lines.append("## Qualifiers Definition")
        lines.append("")
        lines.append("| Key  | Requirement | Native name | Default Value | Description |")
        lines.append("|------|-------------|-------------|---------------|-------------|")
        for qualifier in qualifiers:
            key = qualifier["key"]
            req = qualifier.get("requirement", "optional").capitalize()
            native = qualifier.get("native_name", "")
            default = qualifier.get("default_value", "")
            description = qualifier.get("description", "")
            lines.append(f"| {key} | {req} | {native} | {default} | {description} |")
        lines.append("")

    lines.append("## Examples")
    lines.append("")
    for example in definition["examples"]:
        lines.append(f"- `{example}`")
    lines.append("")

    if reference_urls := definition.get("reference_urls"):
        lines.append("## Reference URLs")
        lines.append("")
        for url in reference_urls:
            lines.append(f"- `{url}`")
        lines.append("")

    if note := definition.get("note"):
        lines.append("## Note")
        lines.append("")
        lines.append(note)
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        selected_types = f"{sys.argv[1]}-definition.json"
    else:
        selected_types = "*-definition.json"

    types = []
    types_dir = Path("types")

    for filepath in types_dir.glob(selected_types):
        data = json.loads(filepath.read_text())
        ptype = data["type"]
        types.append(ptype)
        md = generate_documentation(data)
        mddoc = Path("types-doc") / f"{ptype}-definition.md"
        mddoc.write_text(md, newline="\n")
        print(f"PURL Type Documentation generated for {mddoc}")

    idxdoc =  Path("purl-types-index.json")
    idx = json.dumps(sorted(types), indent=2) + "\n"
    idxdoc.write_text(idx, newline="\n")
    print(f"PURL Types Index generated at {idxdoc}")
