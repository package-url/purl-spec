Package URL specification v1.0.X
================================

The Package URL core specification defines a versioned and formalized format,
syntax, and rules used to represent and validate ``purl``.

A ``purl`` or package URL is an attempt to standardize existing approaches to
reliably identify and locate software packages.

A ``purl`` is a URL string used to identify and locate a software package in a
mostly universal and uniform way across programming languages, package managers,
packaging conventions, tools, APIs and databases.

Such a package URL is useful to reliably reference the same software package
using a simple and expressive syntax and conventions based on familiar URLs.

See <PURL-TYPES.rst>_ for known type definitions.

Check also this short ``purl`` presentation (with video) at FOSDEM 2018
https://fosdem.org/2018/schedule/event/purl/ for an overview.


``purl`` stands for **package URL**.

A ``purl`` is a URL composed of seven components::

    scheme:type/namespace/name@version?qualifiers#subpath

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
``username``, ``password``, ``host`` and ``port`` components. A ``namespace`` segment may
sometimes look like a ``host`` but its interpretation is specific to a ``type``.


Some ``purl`` examples
~~~~~~~~~~~~~~~~~~~~

::

    pkg:bitbucket/birkenfeld/pygments-main@244fd47e07d1014f0aed9c
    pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie
    pkg:gem/ruby-advisory-db-check@0.12.4
    pkg:github/package-url/purl-spec@244fd47e07d1004f0aed9c
    pkg:golang/google.golang.org/genproto#googleapis/api/annotations
    pkg:maven/org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources
    pkg:npm/foobar@12.3.1
    pkg:nuget/EnterpriseLibrary.Common@6.0.1304
    pkg:pypi/django@1.11.1
    pkg:rpm/fedora/curl@7.50.3-1.fc25?arch=i386&distro=fedora-25


A ``purl`` is a URL
~~~~~~~~~~~~~~~~~

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
  They are a closely related, compact and uniform way to reference vcs URLs.
  They may be used as references in separate attributes outside of a ``purl`` or
  in a ``purl`` qualifier.


Rules for each ``purl`` component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``purl`` string is an ASCII URL string composed of seven components.

Some components are allowed to use other characters beyond ASCII: these
components must then be UTF-8-encoded strings and percent-encoded as defined in
the "Character encoding" section.

The rules for each component are:

- **scheme**:

  - The ``scheme`` is a constant with the value "pkg"
  - Since a ``purl`` never contains a URL Authority, its ``scheme`` must not be
    suffixed with double slash as in 'pkg://' and should use instead
    'pkg:'. Otherwise this would be an invalid URI per rfc3986 at
    https://tools.ietf.org/html/rfc3986#section-3.3::

        If a URI does not contain an authority component, then the path
        cannot begin with two slash characters ("//").

    It is therefore incorrect to use such '://' scheme suffix as the URL would
    no longer be valid otherwise. In its canonical form, a ``purl`` must
    NOT use such '://' ``scheme`` suffix but only ':' as a ``scheme`` suffix.
  - ``purl`` parsers must accept URLs such as 'pkg://' and must ignore the '//'.
  - ``purl`` builders must not create invalid URLs with such double slash '//'.
  - The ``scheme`` is followed by a ':' separator
  - For example these two purls are strictly equivalent and the first is in
    canonical form. The second ``purl`` with a '//' is an acceptable ``purl`` but is
    an invalid URI/URL per rfc3986::

            pkg:gem/ruby-advisory-db-check@0.12.4
            pkg://gem/ruby-advisory-db-check@0.12.4


- **type**:

  - The package ``type`` is composed only of ASCII letters and numbers, '.', '+'
    and '-' (period, plus, and dash)
  - The ``type`` cannot start with a number
  - The ``type`` cannot contains spaces
  - The ``type`` must NOT be percent-encoded
  - The ``type`` is case insensitive. The canonical form is lowercase


- **namespace**:

  - The optional ``namespace`` contains zero or more segments, separated by slash
    '/'
  - Leading and trailing slashes '/' are not significant and should be stripped
    in the canonical form. They are not part of the ``namespace``
  - Each ``namespace`` segment must be a percent-encoded string
  - When percent-decoded, a segment:

    - must not contain a '/'
    - must not be empty

  - A URL host or Authority must NOT be used as a ``namespace``. Use instead a
    ``repository_url`` qualifier. Note however that for some types, the
    ``namespace`` may look like a host.


- **name**:

  - The ``name`` is prefixed by a '/' separator when the ``namespace`` is not empty
  - This '/' is not part of the ``name``
  - A ``name`` must be a percent-encoded string


- **version**:

  - The ``version`` is prefixed by a '@' separator when not empty
  - This '@' is not part of the ``version``
  - A ``version`` must be a percent-encoded string

  - A ``version`` is a plain and opaque string. Some package ``types`` use versioning
    conventions such as SemVer for NPMs or NEVRA conventions for RPMS. A ``type``
    may define a procedure to compare and sort versions, but there is no
    reliable and uniform way to do such comparison consistently.


- **qualifiers**:

  - The ``qualifiers`` string is prefixed by a '?' separator when not empty
  - This '?' is not part of the ``qualifiers``
  - This is a query string composed of zero or more ``key=value`` pairs each
    separated by a '&' ampersand. A ``key`` and ``value`` are separated by the equal
    '=' character
  - These '&' are not part of the ``key=value`` pairs.
  - ``key`` must be unique within the keys of the ``qualifiers`` string
  - ``value`` cannot be an empty string: a ``key=value`` pair with an empty ``value``
    is the same as no key/value at all for this key
  - For each pair of ``key`` = ``value``:

    - The ``key`` must be composed only of ASCII letters and numbers, '.', '-' and
      '_' (period, dash and underscore)
    - A ``key`` cannot start with a number
    - A ``key`` must NOT be percent-encoded
    - A ``key`` is case insensitive. The canonical form is lowercase
    - A ``key`` cannot contains spaces
    - A ``value`` must be a percent-encoded string
    - The '=' separator is neither part of the ``key`` nor of the ``value``


- **subpath**:

  - The ``subpath`` string is prefixed by a '#' separator when not empty
  - This '#' is not part of the ``subpath``
  - The ``subpath`` contains zero or more segments, separated by slash '/'
  - Leading and trailing slashes '/' are not significant and should be stripped
    in the canonical form
  - Each ``subpath`` segment must be a percent-encoded string
  - When percent-decoded, a segment:

    - must not contain a '/'
    - must not be any of '..' or '.'
    - must not be empty

  - The ``subpath`` must be interpreted as relative to the root of the package


Character encoding
~~~~~~~~~~~~~~~~~~

For clarity and simplicity a ``purl`` is always an ASCII string. To ensure that
there is no ambiguity when parsing a ``purl``, separator characters and non-ASCII
characters must be UTF-encoded and then percent-encoded as defined at::

    https://en.wikipedia.org/wiki/Percent-encoding

Use these rules for percent-encoding and decoding ``purl`` components:

- the ``type`` must NOT be encoded and must NOT contain separators

- the '#', '?', '@' and ':' characters must NOT be encoded when used as
  separators. They may need to be encoded elsewhere

- the ':' ``scheme`` and ``type`` separator does not need to and must NOT be encoded.
  It is unambiguous unencoded everywhere

- the '/' used as ``type``/``namespace``/``name`` and ``subpath`` segments separator
  does not need to and must NOT be percent-encoded. It is unambiguous unencoded
  everywhere

- the '@' ``version`` separator must be encoded as ``%40`` elsewhere
- the '?' ``qualifiers`` separator must be encoded as ``%3F`` elsewhere
- the '=' ``qualifiers`` key/value separator must NOT be encoded
- the '#' ``subpath`` separator must be encoded as ``%23`` elsewhere

- All non-ASCII characters must be encoded as UTF-8 and then percent-encoded

It is OK to percent-encode ``purl`` components otherwise except for the ``type``.
Parsers and builders must always percent-decode and percent-encode ``purl``
components and component segments as explained in the "How to parse" and "How to
build" sections.


How to build ``purl`` string from its components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Building a ``purl`` ASCII string works from left to right, from ``type`` to
``subpath``.

Note: some extra type-specific normalizations are required.
See the "Known types section" for details.

To build a ``purl`` string from its components:


- Start a ``purl`` string with the "pkg:" ``scheme`` as a lowercase ASCII string

- Append the ``type`` string  to the ``purl`` as a lowercase ASCII string

  - Append '/' to the ``purl``

- If the ``namespace`` is not empty:

  - Strip the ``namespace`` from leading and trailing '/'
  - Split on '/' as segments
  - Apply type-specific normalization to each segment if needed
  - UTF-8-encode each segment if needed in your programming language
  - Percent-encode each segment
  - Join the segments with '/'
  - Append this to the ``purl``
  - Append '/' to the ``purl``
  - Strip the ``name`` from leading and trailing '/'
  - Apply type-specific normalization to the ``name`` if needed
  - UTF-8-encode the ``name`` if needed in your programming language
  - Append the percent-encoded ``name`` to the ``purl``

- If the ``namespace`` is empty:

  - Apply type-specific normalization to the ``name`` if needed
  - UTF-8-encode the ``name`` if needed in your programming language
  - Append the percent-encoded ``name`` to the ``purl``

- If the ``version`` is not empty:

  - Append '@' to the ``purl``
  - UTF-8-encode the ``version`` if needed in your programming language
  - Append the percent-encoded version to the ``purl``

- If the ``qualifiers`` are not empty and not composed only of key/value pairs
  where the ``value`` is empty:

  - Append '?' to the ``purl``
  - Build a list from all key/value pair:

    - discard any pair where the ``value`` is empty.
    - UTF-8-encode each ``value`` if needed in your programming language
    - If the ``key`` is ``checksums`` and this is a list of ``checksums`` join this
      list with a ',' to create this qualifier ``value``
    - create a string by joining the lowercased ``key``, the equal '=' sign and
      the percent-encoded ``value`` to create a qualifier

  - sort this list of qualifier strings lexicographically
  - join this list of qualifier strings with a '&' ampersand
  - Append this string to the ``purl``

- If the ``subpath`` is not empty and not composed only of empty, '.' and '..'
  segments:

  - Append '#' to the ``purl``
  - Strip the ``subpath`` from leading and trailing '/'
  - Split this on '/' as segments
  - Discard empty, '.' and '..' segments
  - Percent-encode each segment
  - UTF-8-encode each segment if needed in your programming language
  - Join the segments with '/'
  - Append this to the ``purl``


How to parse a ``purl`` string in its components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parsing a ``purl`` ASCII string into its components works from right to left,
from ``subpath`` to ``type``.

Note: some extra type-specific normalizations are required.
See the "Known types section" for details.

To parse a ``purl`` string in its components:

- Split the ``purl`` string once from right on '#'

  - The left side is the ``remainder``
  - Strip the right side from leading and trailing '/'
  - Split this on '/'
  - Discard any empty string segment from that split
  - Discard any '.' or  '..' segment from that split
  - Percent-decode each segment
  - UTF-8-decode each segment if needed in your programming language
  - Join segments back with a '/'
  - This is the ``subpath``

- Split the ``remainder`` once from right on '?'

  - The left side is the ``remainder``
  - The right side is the ``qualifiers`` string
  - Split the ``qualifiers`` on '&'. Each part is a ``key=value`` pair
  - For each pair, split the ``key=value`` once from left on '=':

    - The ``key`` is the lowercase left side
    - The ``value`` is the percent-decoded right side
    - UTF-8-decode the ``value`` if needed in your programming language
    - Discard any key/value pairs where the value is empty
    - If the ``key`` is ``checksums``, split the ``value`` on ',' to create
      a list of ``checksums``

  - This list of key/value is the ``qualifiers`` object

- Split the ``remainder`` once from left on ':'

  - The left side lowercased is the ``scheme``
  - The right side is the ``remainder``

- Strip the ``remainder`` from leading and trailing '/'

  - Split this once from left on '/'
  - The left side lowercased is the ``type``
  - The right side is the ``remainder``

- Split the ``remainder`` once from right on '@'

  - The left side is the ``remainder``
  - Percent-decode the right side. This is the ``version``.
  - UTF-8-decode the ``version`` if needed in your programming language
  - This is the ``version``

- Split the ``remainder`` once from right on '/'

  - The left side is the ``remainder``
  - Percent-decode the right side. This is the ``name``
  - UTF-8-decode this ``name`` if needed in your programming language
  - Apply type-specific normalization to the ``name`` if needed
  - This is the ``name``

- Split the ``remainder`` on '/'

  - Discard any empty segment from that split
  - Percent-decode each segment
  - UTF-8-decode the each segment if needed in your programming
    language
  - Apply type-specific normalization to each segment if needed
  - Join segments back with a '/'
  - This is the ``namespace``


Known ``purl`` types
~~~~~~~~~~~~~~~~~~~~

There are several known ``purl`` package type definitions tracked in the
separate `<PURL-TYPES.rst>`_ document.

Known ``qualifiers`` key/value pairs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: Do not abuse ``qualifiers``: it can be tempting to use many qualifier
keys but their usage should be limited to the bare minimum for proper package
identification to ensure that a ``purl`` stays compact and readable in most cases.

Additional, separate external attributes stored outside of a ``purl`` are the
preferred mechanism to convey extra long and optional information such as a
download URL, vcs URL or checksums in an API, database or web form.


With this warning, the known ``key`` and ``value`` defined here are valid for use in
all package types:

- ``repository_url`` is an extra URL for an alternative, non-default package
  repository or registry.  When a package does not come from the default public
  package repository for its ``type`` a ``purl`` may be qualified with this extra
  URL. The default repository or registry of a ``type`` is documented in the
  "Known ``purl`` types" section.

- ``download_url`` is an extra URL for a direct package web download URL to
  optionally qualify a ``purl``.

- ``vcs_url`` is an extra URL for a package version control system URL to
  optionally qualify a ``purl``. The syntax for this URL should be as defined in
  Python pip or the SPDX specification. See
  https://github.com/spdx/spdx-spec/blob/cfa1b9d08903/chapters/3-package-information.md#37-package-download-location

  - TODO: incorporate the details from SPDX here.

- ``file_name`` is an extra file name of a package archive.

- ``checksum`` is a qualifier for one or more checksums stored as a
  comma-separated list. Each item in the ``value`` is in form of
  ``lowercase_algorithm:hex_encoded_lowercase_value`` such as
  ``sha1:ad9503c3e994a4f611a4892f2e67ac82df727086``.
  For example (with checksums truncated for brevity) ::

       checksum=sha1:ad9503c3e994a4f,sha256:41bf9088b3a1e6c1ef1d


Tests
~~~~~

To support the language-neutral testing of ``purl`` implementations, a test suite
is provided as JSON document named ``test-suite-data.json``. This JSON document
contains an array of objects. Each object represents a test with these key/value
pairs some of which may not be normalized:

- **purl**: a ``purl`` string.
- **canonical**: the same ``purl`` string in canonical, normalized form
- **type**: the ``type`` corresponding to this ``purl``.
- **namespace**: the ``namespace`` corresponding to this ``purl``.
- **name**: the ``name`` corresponding to this ``purl``.
- **version**: the ``version`` corresponding to this ``purl``.
- **qualifiers**: the ``qualifiers`` corresponding to this ``purl`` as an object of
  {key: value} qualifier pairs.
- **subpath**: the ``subpath`` corresponding to this ``purl``.
- **is_invalid**: a boolean flag set to true if the test should report an
  error

To test ``purl`` parsing and building, a tool can use this test suite and for
every listed test object, run these tests:

- parsing the test canonical ``purl`` then re-building a ``purl`` from these parsed
  components should return the test canonical ``purl``

- parsing the test ``purl`` should return the components parsed from the test
  canonical ``purl``

- parsing the test ``purl`` then re-building a ``purl`` from these parsed components
  should return the test canonical ``purl``

- building a ``purl`` from the test components should return the test canonical ``purl``


License
~~~~~~~

This document is licensed under the MIT license
