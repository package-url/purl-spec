Frequently Asked Questions
==========================

Scheme
~~~~~~

**QUESTION**: Can the ``scheme`` component be followed by a colon and two slashes, like a URI?

**ANSWER**: No.  Since a ``purl`` never contains a URL Authority, its ``scheme`` should not be suffixed with double slash as in 'pkg://' and should use 'pkg:' instead. Otherwise this would be an invalid URI per RFC 3986 at https://tools.ietf.org/html/rfc3986#section-3.3::

    If a URI does not contain an authority component, then the path
    cannot begin with two slash characters ("//").

This rule applies to all slash '/' characters between the ``scheme``'s colon separator and the ``type`` component, e.g., ':/', '://', ':///' et al.

In its canonical form, a ``purl`` must not use any such ':/' ``scheme`` suffix and may only use ':' as a ``scheme`` suffix.  This means that:

- ``purl`` parsers must accept URLs such as 'pkg://' and must ignore and remove all such '/' characters.
- ``purl`` builders should not create invalid URLs with one or more slash '/' characters between 'pkg:' and the ``type`` component.

For example, although these two purls are strictly equivalent, the first is in canonical form, while the second -- with a '//' between 'pkg:' and the ``type`` 'gem' -- is an acceptable purl but is an invalid URI/URL per RFC 3986::

    pkg:gem/ruby-advisory-db-check@0.12.4

    pkg://gem/ruby-advisory-db-check@0.12.4


**QUESTION**: Is the colon between ``scheme`` and ``type`` encoded? Can it be encoded? If yes, how?

**ANSWER**: The "Rules for each ``purl`` component" section provides that the ``scheme`` MUST be followed by an unencoded colon ':'.

In this case, the colon ':' between ``scheme`` and ``type`` is being used as a separator, and consequently should be used as-is, never encoded and never requiring any decoding. Moreover, it should be a parsing error if the colon ':' does not come directly after 'pkg'.  Tools are welcome to recover from this error to help with malformed purls, but that's not a requirement.


Type
~~~~

**QUESTION**: What behavior is expected from a purl spec implementation if a
``type`` contains a character like a slash '/' or a colon ':'?

**ANSWER**: The "Rules for each purl component" section provides that the
package ``type``

    MUST be composed only of ASCII letters and numbers, period '.', plus '+',
    and dash '-'.

As a result, a purl spec implementation must return an error when encountering
a ``type`` that contains a prohibited character.


Version
~~~~~~~

**QUESTION**: How do package ``types`` handle the comparison and sorting of
versions?

**ANSWER**: Some package ``types`` use versioning conventions such as SemVer
for NPMs or NEVRA conventions for RPMS. A ``type`` may define a procedure to
compare and sort versions, but there is no reliable and uniform way to do such
comparison consistently.
