# Specification

``purl`` stands for **package URL**.

A ``purl`` is a URL composed of seven components::

> scheme:type/namespace/name@version?qualifiers#subpath

Components are separated by a specific character for unambiguous parsing.

The definition for each components is:

- **scheme**: this is the URL scheme with the constant value of "pkg". One of
  the primary reason for this single scheme is to facilitate the future official
  registration of the "pkg" scheme for package URLs. Required.
- **type**: the package "type" or package "protocol" such as maven, npm, nuget,
  gem, pypi, etc. Required.
- **namespace**: some name prefix such as a Maven groupid, a Docker image owner,
  a GitHub user or organization. Optional and type-specific.
- **name**: the name of the package. Required.
- **version**: the version of the package. Optional.
- **qualifiers**: extra qualifying data for a package such as an OS,
  architecture, a distro, etc. Optional and type-specific.
- **subpath**: extra subpath within a package, relative to the package root.
  Optional.

Components are designed such that they form a hierarchy from the most significant
on the left to the least significant components on the right.

A ``purl`` must NOT contain a URL Authority i.e. there is no support for
``username``, ``password``, ``host`` and ``port`` components. A ``namespace``
segment may sometimes look like a ``host`` but its interpretation is specific
to a ``type``.
