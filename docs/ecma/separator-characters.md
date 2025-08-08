# ``purl`` separators

This is how each of the Separator Characters is used:

- ':' (colon) is the separator between ``scheme`` and ``type``
- '/' (slash) is the separator between ``type``, ``namespace`` and ``name``
- '/' (slash) is the separator between ``subpath`` segments
- '@' (at sign) is the separator between ``name`` and  ``version``
- '?' (question mark) is the separator before ``qualifiers``
- '=' (equals) is the separator between a ``key`` and a ``value`` of a
  ``qualifier``
- '&' (ampersand) is the separator between ``qualifiers`` (each being a
  ``key=value`` pair)
- '#' (number sign) is the separator before ``subpath``
