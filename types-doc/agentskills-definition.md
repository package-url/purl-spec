<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: agentskills

- **Type Name:** Agent Skills
- **Description:** AI agent skills following the Agent Skills specification (SKILL.md format)
- **Schema ID:** `https://packageurl.org/types/agentskills-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:agentskills/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Default Repository URL:** https://github.com
- **Note:** `The default repository is GitHub, where most agent skills are published. Other registries such as ClawHub (clawhub.ai) can be specified using the repository_url qualifier.`

## Namespace definition

- **Requirement:** Required
- **Native Label:** owner or publisher
- **Note:** `The namespace is the skill publisher or repository owner. For GitHub-hosted skills, this is the GitHub user or organization (e.g., 'anthropics', 'microsoft'). For ClawHub skills, this is the publisher name. When a skill is discovered in the cross-client path (.agents/skills/) and the publisher cannot be determined from provenance files, use the reserved namespace 'cross-client'. It is not case sensitive and must be lowercased.`

## Name definition

- **Requirement:** Required
- **Native Label:** skill name
- **Note:** `The name is the skill name as defined in the SKILL.md frontmatter 'name' field. Skill names may only contain lowercase letters, numbers, and hyphens per the Agent Skills specification. Must not start or end with a hyphen or contain consecutive hyphens.`

## Version definition

- **Requirement:** Optional
- **Native Label:** version or commit
- **Note:** `The version is the skill version if available. May be a semantic version from a registry lock file (e.g., clawhub.lock), a git commit SHA, or a git tag. Versions are optional as many skills do not declare an explicit version in their SKILL.md frontmatter.`

## Qualifiers definition

| Key | Description |
|-----|-------------|
| `repository_url` | The URL of the skill registry or repository when not using the default GitHub repository. For example, 'https://clawhub.ai' for ClawHub-hosted skills. |
| `install_path` | The filesystem path where the skill is installed, relative to the scan root. For example, '.agents/skills/weather' or '.claude/skills/lint-fix'. |
| `scope` | The installation scope of the skill: 'project' for project-level skills or 'user' for user/global-level skills. |
| `client` | The target agent client for client-specific skill paths. For example, 'claude-code', 'cursor', 'windsurf', 'openclaw', 'fast-agent'. Skills in cross-client paths (.agents/skills/) do not require this qualifier. |

## Examples

- `pkg:agentskills/anthropics/xlsx`
- `pkg:agentskills/anthropics/theme-factory@d211d437`
- `pkg:agentskills/openclaw-community/weather@1.2.0?repository_url=https://clawhub.ai`
- `pkg:agentskills/microsoft/mcp-builder?scope=user`
- `pkg:agentskills/vercel-labs/deploy-to-vercel?scope=project&client=claude-code`
- `pkg:agentskills/internal/deploy?scope=project&install_path=.agents/skills/deploy`
- `pkg:agentskills/cross-client/data-pipeline?scope=user`

## Agent Skills Specification

This PURL type identifies packages conforming to the [Agent Skills specification](https://agentskills.io/specification), an open format for giving AI agents new capabilities. A skill is a directory containing a `SKILL.md` file with YAML frontmatter (`name`, `description`) and Markdown instructions, optionally bundled with scripts, references, and assets.

## Reference URLs

- [Agent Skills Specification](https://agentskills.io/specification)
- [Client Implementation Guide](https://agentskills.io/client-implementation/adding-skills-support)
- [Agent Skills GitHub Repository](https://github.com/agentskills/agentskills)
