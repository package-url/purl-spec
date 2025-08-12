## A ``purl`` is a URL

- A ``purl`` is a valid URL and URI that conforms to the URL definitions or
  specifications at:
  - https://tools.ietf.org/html/rfc3986
  - https://en.wikipedia.org/wiki/URL#Syntax
  - https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax
  - https://url.spec.whatwg.org/
- This is a valid URL because it is a locator even though it has no Authority
  URL component: each ``type`` has a default repository location when defined.
- The ``purl`` components are mapped to these URL components:
  - ``purl`` ``scheme``: this is a URL ``scheme`` with a constant value: ``pkg``
  - ``purl`` ``type``, ``namespace``, ``name`` and ``version`` components: these are
    collectively mapped to a URL ``path``
  - ``purl`` ``qualifiers``: this maps to a URL ``query``
  - ``purl`` ``subpath``: this is a URL ``fragment``
  - In a ``purl`` there is no support for a URL Authority (e.g. NO
    ``username``, ``password``, ``host`` and ``port`` components).
- Special URL schemes as defined in https://url.spec.whatwg.org/ such as
  ``file://``, ``https://``, ``http://`` and ``ftp://`` are NOT valid ``purl`` types.
  They are valid URL or URI schemes but they are not ``purl``.
  They may be used to reference URLs in separate attributes outside of a ``purl``
  or in a ``purl`` qualifier.
- Version control system (VCS) URLs such ``git://``, ``svn://``, ``hg://`` or as
  defined in Python pip or SPDX download locations are NOT valid ``purl`` types.
  They are valid URL or URI schemes but they are not ``purl``.
  They are a closely related, compact and uniform way to reference VCS URLs.
  They may be used as references in separate attributes outside of a ``purl`` or
  in a ``purl`` qualifier.
