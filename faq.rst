Frequently Asked Questions
==========================

Type
----

**QUESTION**: Can the ``type`` component start with a number?

No.  As the "Rules for each purl component" section provides, "The ``type``
MUST start with an ASCII letter."

**QUESTION**: Can the ``type`` component contain spaces?

No.  See the "Rules for each purl component" section:

    The package ``type`` MUST be composed only of ASCII letters and numbers,
    '.', '+' and '-' (period, plus, and dash).

**QUESTION**: Does the ``type`` need to be percent-encoded?

No.  This is addressed in the "Rules for each purl component" section:
"The ``type`` MUST be unencoded."

**QUESTION**: What behavior is expected from a purl spec implementation if a
``type`` contains a character like a slash '/' or a colon ':'?

The "Rules for each purl component" section provides that

    [t]he package ``type`` MUST be composed only of ASCII letters and numbers,
    '.', '+' and '-' (period, plus, and dash)

As a result, a purl spec implementation must return an error when encountering
a ``type`` that contains a prohibited character.
