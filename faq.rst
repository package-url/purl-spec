Frequently Asked Questions
==========================

The following FAQs are organized into

- a "Components" section that includes each of the seven PURL components
  (``scheme``, ``type``, ``namespace``, ``name``, ``version``, ``qualifiers``
  and ``subpath``), and

- a "General" section containing a mix of questions and answers that don't fit
  neatly into a component-focused category.

If you have a question about the PURL specification and don't find an answer
below, you can open an issue `here <https://github.com/package-url/purl-spec/issues/new?template=Blank+issue>`_.

Components
~~~~~~~~~~

Scheme
------

[to come]

----

Type
----

**Question**: Can the ``type`` component start with a number?

No.  As the "Rules for each purl component" section provides, "The ``type``
MUST start with an ASCII letter."

**Question**: Can the ``type`` component contain spaces?

No.  See the "Rules for each purl component" section:

    The package ``type`` MUST be composed only of ASCII letters and numbers,
    '.', '+' and '-' (period, plus, and dash).

**Question**: Does the ``type`` need to be percent-encoded?

No.  This is addressed in the "Rules for each purl component" section:
"The ``type`` MUST be unencoded."

**Question**: What behavior is expected from a PURL spec implementation if a
``type`` contains a character like a slash '/' or a colon ':'?

The "Rules for each purl component" section provides that

    [t]he package ``type`` MUST be composed only of ASCII letters and numbers,
    '.', '+' and '-' (period, plus, and dash)

As a result, a PURL spec implementation must return an error when encountering
a ``type`` that contains a prohibited character.

----

Namespace
---------

[to come]

----

Name
----

[to come]

----

Version
-------

[to come]

----

Qualifiers
----------

[to come]

----

Subpath
-------

[to come]
