
We build and release software by consuming and producing software
packages such as NPMs, RPMs, Rubygems, etc.

A `puurl` is a URL string used to identify a package in a mostly
universal and uniform way across programing languages, package
managers and packaing conventions and different tools, APIs and databases.

This identification is necessary and useful such that tools, databases
and APIS can reference the same software package using a simple and
expressive syntax and conventions based on familiar URLs.


puurl
~~~~~

`puurl` stands for **package "mostly" universal URL**.

A `puurl` is a URL composed of six parts: `type://namespace/name@version?qualifiers#path`

- **type**: such as maven, npm, gem, pypi, etc. This is a URL `scheme`.
- **namespace**: such as a maven groupid, a Docker registry or owner, a GithUb user or organization.
- **name**: the name of the package.
- **version**: the version of the package.
- **qualifiers**: extra qualifying data for a package such as an OS, architecture, a distro, etc.
- **path**: a sub path within a package.

At the minimum a `type` and a `name` may be needed to indentify a package.
A `version` is often essential for precise identification.
Other parts are optional and are often specific to a `type`.


Some examples 
~~~~~~~~~~~~~

- a Docker image with a specific id as version. From gcr.io::

    docker:gcr.io/customer/dockerimage@sha256:244fd47e07d1004f0aed9c 

- a Docker image with a specific tag as version. From the public Docker hub::

    docker:cassandra@cassandra
    
- a Maven source JAR (here the qualifiers point to a source jar)::

    maven:org.apache.xmlgraphics/batik-anim@1.9.1?packaging=sources

- a Go dependency with a path inside a Go package repo::

    godep:google.golang.org/genproto#googleapis/api/annotations  

- a source RPM::

    rpm:fedora-25/curl@7.50.3-1.fc25?arch=src

- The i386 build of an RPM::

    rpm:fedora-25/curl@7.50.3-1.fc25?arch=i386

- The i386 build of a Dedian Jessie package::

    deb:jessie/curl@7.50.3-1?arch=i386

- Django on Pypi::

    pypi:django@1.11.1

- A Rubygem::

    gem:ruby-advisory-db-check@0.12.4

- A Rubygem for the Java platform::

    gem:jruby-launcher@1.1.2?platform=java 

- An NPM::

    npm:foobar@12.3.1

- A scoped NPM package::

    npm:%40angular/animation@12.3.1


Rules for each `puurl` part
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A `puurl` string is an ASCII string. Some parts can encode other
characters beyond ASCII: these parts must then be in UTF-8 and
percent-encoded.


- **type**:

  - The `type` is composed only of ASCII letters and numbers,
    '.', '+' and '-' and '_' (period, plus, dash and underscore). 
  - It cannot start with a number.
  - It must NOT be percent-encoded.
  - It is case insensitive. The canonical form is lowercase. 
  - It cannot contains spaces.

- **namespace**:

  - The `namespace` contains zero or more segments, separated by slash '/'. 
  - Leading and trailing slashes '/' are not significant and should be
    stripped in the canonical form.
  - Each segment must be a percent-encoded string. 
  - A segment must not contain '/' when percent-decoded. 

- **name**: must be a percent-encoded string.

- **version**: must be a percent-encoded string.

- **qualifiers**: 

  - This is a query string composed of zero or more `key=value` pairs
    each separated by a '&' ampersand. A `key` and `value` are
    separated by the equal '=' character
  - A `key` must be unique within the keys of the `qualifiers` string. 
  - A `value` cannot be an empty string: a key/value pair with an empty
    value is the same as no key/value at all  
  - For each pair of `key` = `value`:
  
    - The `key` must be composed only of ASCII letters and numbers, 
      '.' and '-' and '_' (period, dash and underscore)
    - A `key` cannot start with a number
    - A `key` must NOT be percent-encoded
    - It is case insensitive. The canonical form is lowercase 
    - It cannot contains spaces
    - A `value` must be must be a percent-encoded string

- **path**:

  - The `path` contains zero or more segments, separated by slash '/' 
  - Leading and trailing slashes '/' are not significant and should be
    stripped in the canonical form
  - Each segment must be a percent-encoded string 
  - When percent-decoded, a segment:

    - must not contain a '/'
    - must not be any of '..' or '.'
  
  - The `path` must be interpreted as relative to the root of the package


How to build `puurl` string from its parts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on the conventions defined in this document, building a string
works from left to right.


 - Start a `puurl` string with the `type` as a lowercase string

   - Append '//:' to the `puurl`

 - If the `namespace` is not empty

   - Split the `namespace` on '/'
   - Percent-encode each segment
   - Join the segments with '/'
   - Append this to the `puurl`
   - Append '/' to the `puurl`
   - Append the percent-encoded name to the `puurl`

 - If the `namespace` is empty:

   - Append the percent-encoded name to the `puurl`

 - If the `version` is not empty:

   - Append '@' to the `puurl`
   - Append the percent-encoded version to the `puurl`

 - If the `qualifiers` are not empty:

   - Append '?' to the `puurl`
   - For each key/value pair:
   
     - create a string by joining the lowercase `key`, the equal '=' 
       sign and the percent-encoded `value`

   - sort this list of strings lexicographically
   - join this list of strings with a '&'
   - Append this to the `puurl`

 - If the `path` is not empty:
 
   - Append '#' to the `puurl`
   - Split the `path` on '/'
   - Discard empty, '.' and '..' segments
   - Percent-encode each segment
   - Join the segments with '/'
   - Append this to the `puurl`


How to parse a `puurl` string in its parts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on the conventions defined in this document, parsing works from
right to left.

- Split the `puurl` string once from right on '#'
 
  - The left side is the `remainder`
  - Strip the right side from leading and trailing '/'
  - Split this on '/'
  - Discard any empty string segment from that split
  - Discard any '.' or  '..' segment from that split
  - Percent-decode each segment and join them back in a '/'
    slash-separated string. This is the `path`

- Split the `remainder` once from right on '?'
 
  - The right side is the `qualifiers`
  - The left side is the `remainder`
  - Split the `qualifiers` on '&'. Each part is a `key=value` pair
  - For each pair, split the `key=value` once from left on '=':

    - The `key` is the lowercase left side
    - The `value` is the percent-decoded right side

- Split the `remainder` once from left on ':'
 
  - The left side lowercased is the `type`
  - The right side is the `remainder`

- Strip the `remainder` from leading and trailing '/'
 
  - Split this once from right on '/'
  - The right side is the `name` after percent-decoding
  - The left side is the `remainder`

- Split the `remainder` on '/'
 
  - Discard any empty segment from that split
  - Percent-decode each segment and join them back in a '/'
    slash-separated string
  - This is the `namespace`


Relations with the whatwg URLs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the relationships between the parts of a `puurl` and a
URL as defined at https://url.spec.whatwg.org/#url-representation :

- `puurl` `type`: this is the URL `scheme`.
- `puurl` `namespace`, `name` and `version` parts: these collectively map to the URL `path`. 
- `puurl` `qualifiers`: this maps to the URL `query`
- `puurl` `path`: this is the URL `fragment`

Note: In a `puurl` there is no special mapping of parts to the URL `username`,
`password`, `host` and `port` parts.


Known implementations
~~~~~~~~~~~~~~~~~~~~~

- in Python:
- in Ruby:
- in Go:
- in JavaScript:
- in Perl:
- for the JVM:


Related work
~~~~~~~~~~~~

- JForg XRAY
- Google Grafeas
- Libraries.io
- versioneye
- OpenShift fabric8
- Here.com OSRK
- ScanCode


Other considerations
~~~~~~~~~~~~~~~~~~~~

- A `puurl` is a valid URL that conforms to the URL spec at https://url.spec.whatwg.org/
 
- `https://`, `http://` and `ftp://` URL schemes are not valid `puurl` `type`.

- When a package is from an alternative package `repository` (e.g.
  not from the default `repository` for its `type`) a `puurl` may be
  supplemented by an other and separate attribute pointing to this
  alternative  package `repository` URL.

- When a package is from available through its `type` protocol, 
  a `puurl` may be supplemented by an other and separate attribute
  pointing to a direct and regular web download URL.

- other possible names: `puuid` or `puid` for Package "mostly"
  Universal IDentifiers. `puuid` means trees in Estonian.
