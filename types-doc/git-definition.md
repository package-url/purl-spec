<!--  NOTE: Auto-generated from the JSON PURL type definition.
Do not manually edit this file. Edit the JSON type definition instead. -->

# PURL Type Definition: git

- **Type Name:** Git
- **Description:** Git-based source packages
- **Schema ID:** `https://packageurl.org/types/git-definition.json`

## PURL Syntax

The structure of a PURL for this package type is:

    pkg:git/<namespace>/<name>@<version>?<qualifiers>#<subpath>

## Repository Information

- **Use Repository:** Yes
- **Note:** There is no default package repository, this should be implied from namespace.

## Namespace definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** The url path to the git host
- **Note:** `The source host for the git repository. See: https://git-scm.com/docs/git-clone.html#_git_urls`

## Name definition

- **Requirement:** Required
- **Case Sensitive:** Yes
- **Native Label:** repository name with owner
- **Note:** `The path on the host to the git repository. See: https://git-scm.com/docs/git-clone.html#_git_urls`

## Version definition

- **Requirement:** Optional
- **Native Label:** A git reference
- **Note:** `The version is a git reference (https://git-scm.com/book/en/v2/Git-Internals-Git-References). Ideally a commit or tag.`

## Examples

- `pkg:git/codeberg.org/forgejo/forgejo/@a72d2c07cfca03b55371089de6aa230d8c951fa0#options/locale_readme.md`
- `pkg:git/cygwin.com/cgit/newlib-cygwin@6d049c54c3314da31d9ffac133a6a2f2dfecaac2`
- `pkg:git/projects.blender.org/blender/blender.git`
- `pkg:git/gitlab.gnome.org/GNOME/adwaita-fonts`
