Frequently Asked Questions
==========================

Components
~~~~~~~~~~

Scheme
------

Q: Can the scheme component be followed by a colon and two slashes, like a URI?

A: No.  Since a ``purl`` never contains a URL Authority, its ``scheme`` MUST NOT be suffixed with double slash as in 'pkg://' and SHOULD use instead 'pkg:'. Otherwise this would be an invalid URI per rfc3986 at https://tools.ietf.org/html/rfc3986#section-3.3::

    If a URI does not contain an authority component, then the path
    cannot begin with two slash characters ("//").

It is therefore incorrect to use such '://' scheme suffix as the URL would no longer be valid otherwise. This rule applies to all slash '/' characters between the scheme's colon separator and the type component, e.g., ':/', '://', ':///' et al.  In its canonical form, a ``purl`` MUST NOT use any such ':/' ``scheme`` suffix and may only use ':' as a ``scheme`` suffix.

- ``purl`` parsers MUST accept URLs such as 'pkg://'and MUST ignore -- i.e., normalize by deleting -- all such '/' characters.
- ``purl`` builders MUST NOT create invalid URLs with such double slash '//'.
- For example these two purls are strictly equivalent and the first is in canonical form. The second ``purl`` with a '//' is an acceptable ``purl`` but is an invalid URI/URL per rfc3986::

    pkg:gem/ruby-advisory-db-check@0.12.4
    pkg://gem/ruby-advisory-db-check@0.12.4

----

Q: Is the colon between scheme and type encoded? Can it be encoded? If yes, how?

A: The "Rules for each ``purl`` component" section provides that "[t]he scheme and type MUST be separated by a colon ':'".  In addition, the "Character encoding" section provides that "the '#', '?', '@' and ':' characters MUST remain unencoded and displayed as-is when used as separators."

The colon ':' between scheme and type is being used as a separator, and consequently SHOULD be used as-is, never encoded and never requiring any decoding. Moreover, it SHOULD be a parsing error if the colon ':' does not come directly after 'pkg'.  Tools are welcome to recover from this error to help with damaged PURLs, but that's not a requirement.


Type
----

- to come


Namespace
---------

- to come


Name
----

- to come


Version
-------

- to come


Qualifiers
----------

- to come


Subpath
-------

- to come
