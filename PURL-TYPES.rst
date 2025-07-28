Package-URL Type definitions
============================

Each package manager, platform, type, or ecosystem has its own conventions and
protocols to identify, locate, and provision software packages.

The package **type** is the component of a Package-URL that is used to capture
this information with a short string such as ``maven``, ``npm``, ``nuget``, ``gem``,
``pypi``, etc.

These are known ``PURL`` package type definitions.

Definitions can also include types reserved for future use.

See also https://github.com/package-url/purl-spec and
`<PURL-SPECIFICATION.rst>`_ for the Package URL specification.

This document no longer contains a manually maintained list of PURL types.

Instead, all PURL type definitions are now maintained in a simple JSON document with
automatically generated documentation.


Where to find PURL Type information
--------------------------------------

- In the JSON Index listing of all defined PURL types at:
  `/purl-types-index.json <https://github.com/package-url/purl-spec/tree/main/purl-types-index.json>`_

- In individual JSON files, one for each PURL type definition at:
  `/types <https://github.com/package-url/purl-spec/tree/main/types>`_

- As Markdown documentation, generated from for each PURL type JSON definition at:
  `/types-doc <https://github.com/package-url/purl-spec/tree/main/types-doc>`_


How PURL Types are maintained
------------------------------

All PURL type definitions are maintained as JSON definition files  and JSON test files in the PURL
specification repository. These JSON files serve as the source of truth and define the
structure of each PURL type, including:

- Namespace and name formatting rules
- Supported qualifiers
- Repository requirements
- Mapping of PURL concepts to the native ecosystem concepts

On commit, a job automatically:

- Checks that all JSON files are schema-valid
- Formats all the JSON files
- Generates the ``purl-types-index.json`` file containing a list of defined known PURL types
- Generates human-readable documentation for each type


How to Propose a New PURL Type
------------------------------

To propose a new PURL type, create an **issue** and a corresponding **pull request** to the
repository with:

 - a new JSON definition file under `types/`.
 - a new JSON test file file under `tests/types/`.
 
  
Ensure that your proposal follows the **PURL Type Definition Schema** and includes all required
fields. For this see the README-dev.rst for details to run local checks.



Other candidate types to define
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``android`` for Android apk packages:
- ``apache`` for Apache projects packages:
- ``atom`` for Atom packages:
- ``bower`` for Bower JavaScript packages:
- ``brew`` for Homebrew packages:
- ``buildroot`` for Buildroot packages
- ``carthage`` for Cocoapods Cocoa packages:
- ``chef`` for Chef packages:
- ``chocolatey`` for Chocolatey packages
- ``clojars`` for Clojure packages:
- ``coreos`` for CoreOS packages:
- ``crystal`` for Crystal Shards packages:
- ``ctan`` for CTAN TeX packages:
- ``drupal`` for Drupal packages:
- ``dtype`` for DefinitelyTyped TypeScript type definitions:
- ``dub`` for D packages:
- ``ebuild`` for Gentoo Linux portage packages:
- ``eclipse`` for Eclipse projects packages:
- ``elm`` for Elm packages:
- ``gitea`` for Gitea-based packages:
- ``gitlab`` for GitLab-based packages:
- ``gradle`` for Gradle plugins
- ``guix`` for Guix packages:
- ``haxe`` for Haxe packages:
- ``helm`` for Kubernetes packages
- ``julia`` for Julia packages:
- ``melpa`` for Emacs packages
- ``meteor`` for Meteor JavaScript packages:
- ``nim`` for Nim packages:
- ``nix`` for Nixos packages:
- ``opam`` for OCaml packages:
- ``openwrt`` for OpenWRT packages:
- ``osgi`` for OSGi bundle packages:
- ``p2`` for Eclipse p2 packages:
- ``pear`` for Pear PHP packages:
- ``pecl`` for PECL PHP packages:
- ``perl6`` for Perl 6 module packages:
- ``platformio`` for PlatformIO packages:
- ``puppet`` for Puppet Forge packages:
- ``sourceforge`` for Sourceforge-based packages:
- ``sublime`` for Sublime packages:
- ``terraform`` for Terraform modules
- ``vagrant`` for Vagrant boxes
- ``vim`` for Vim scripts packages:
- ``wordpress`` for Wordpress packages:
- ``yocto`` for Yocto recipe packages:


License
~~~~~~~

This document is licensed under the MIT license.
