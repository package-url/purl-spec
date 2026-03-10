# Frequently Asked Questions

## Scheme

**QUESTION**: Can the **scheme** component be followed by a colon and two
slashes, like a URI?

**ANSWER**: No.  Since a PURL never contains a URL Authority, its
**scheme** should not be suffixed with double slash as in 'pkg://' and should
 use 'pkg:' instead. Otherwise this would be an invalid URI per RFC 3986 at
 https://tools.ietf.org/html/rfc3986#section-3.3:

    If a URI does not contain an authority component, then the path
    cannot begin with two slash characters ("//").

This rule applies to all slash '/' characters between the **scheme**'s colon
separator and the **type** component, e.g., ':/', '://', ':///' et al.

In its canonical form, a PURL shall not use any ':/' **scheme**
suffix and may only use ':' as a **scheme** suffix.  This means that:

- PURL parsers shall accept URLs such as 'pkg://' and shall ignore and
remove all such '/' characters.

- PURL builders should not create invalid URLs with one or more slash '/'
characters between 'pkg:' and the **type** component.

For example, although these two PURLs are strictly equivalent, the first is
in canonical form, while the second -- with a '//' between 'pkg:' and the
**type** 'gem' -- is an acceptable PURL but is an invalid URI/URL per RFC
3986:

    pkg:gem/ruby-advisory-db-check@0.12.4

    pkg://gem/ruby-advisory-db-check@0.12.4

**QUESTION**: Is the colon between **scheme** and **type** encoded? Can it be
encoded? If yes, how?

**ANSWER**: The "Rules for each PURL component" section provides that the
**scheme** shall be followed by an unencoded colon ':'.

In this case, the colon ':' between **scheme** and **type** is being used as
a separator, and consequently should be used as-is, never encoded and never
requiring any decoding. Moreover, it should be a parsing error if the colon
':' does not come directly after 'pkg'.  Tools are welcome to recover from
this error to help with malformed PURLs, but that is not a requirement.

## Type

**QUESTION**: What behavior is expected from a PURL spec implementation if a
**type** contains a character like a slash '/' or a colon ':'?

**ANSWER**: The "Rules for each PURL component" section provides that the
package **type** that list allowed characters shall be composed only of ASCII letters 
and numbers, period '.', and dash '-'

As a result, a PURL spec implementation shall return an error when
encountering a **type** that contains a prohibited character.

## Version

**QUESTION**: How do package managers handle the comparison and sorting of
versions?

**ANSWER**: Some package managers use versioning conventions such as SemVer
for NPMs or NEVRA conventions for RPMs. A package manager may define a procedure to
compare and sort versions, but there is no reliable and uniform way to do
such comparison consistently.

**QUESTION**: Why is the PURL **version** optional?

**ANSWER**: This is to support pointers to any version of a package or when you do
 not know the version (yet). This should not be abused but is useful and used
in practice. For example a package version may depend on another package
with no version specified.

## Qualifiers

**QUESTION**: What is the **qualifier** for a checksum like a SHA1?

**ANSWER**: The spec was originally ambiguous and used **checksum**
(singular) in one place and **checksums** (plural) in other places. This has
been discussed extensively in issues and PRs such as
https://github.com/package-url/purl-spec/issues/73 and
https://github.com/package-url/purl-spec/pull/209 . The official form
is **checksum** (singular). When writing a lenient parser, consider accepting
 **checksum** (singular) or  **checksums** (plural) when reading a PURL,
and always emit **checksum** (singular) when writing a PURL.

## Subpath

**QUESTION**: Can I use a PURL subpath with multiple subpaths, globs or regexes in a PURL?

**ANSWER**: **No.** Use multiple PURLs or other attributes outside of a PURL.

## Plus character

**QUESTION**: Can a PURL contain a plus character '+'?

**ANSWER**: Decoded individual PURL components can contain a plus. The 
encoded, canonical form can never contain an unencoded plus.

## From the wiki

**QUESTION**: Why create yet another standard with PURL?

**ANSWER**:**You were about to "XKCD" me with a link to https://xkcd.com/927/**: this
is not entirely correct as there is no other standard like PURL:
only some attempts to define something similar. It is a community effort to
define conventions to reference and locate packages. It builds on and clarifies
existing conventions used by existing tools.

**QUESTION**: Can I use an existing URL parsing library to parse a PURL?

**ANSWER**: **Yes and this is highly encouraged!** A PURL is a valid URL and should be
parseable by any conforming URL/URI parser that can accept any scheme. You can 
then focus on the specifics of PURL component encoding and decoding, component
normalization and additional parsing (e.g. for **qualifiers**) and component value validation.

**QUESTION**: Can I use the Authority (i.e. user:pass@host:port) of a URI/URI in a PURL?

**ANSWER**: **No.** There are several reasons: The rules for parsing user/host/password
and ports are complex and even more so when you add IDNA, punycode and IPv4/v6.
These would introduce subtle quirks if for instance the user/password was
used as a PURL **version**. 

While a host may be important to locate a package it is not required to
identify it: the exact same package may exist in multiple repositories,
local, remote or private mirrors. This is still the same package.

The Authority components come before the Path in a URL: this would
break the hierarchical nature of the PURL components and no longer make
them sortable as plain strings: this a good property when dealing
with many PURLs in a database or even small sorted lists in a UI.

To reference an alternative public or private package repository URL beyond
the default public repository for a PURL **type**, you can use the 
`repository_url` **qualifiers** **key/value** pair to specify another repository URL.

**QUESTION**: All familiar URLs contain `://`. Why is there no such thing in a PURL?

**ANSWER**: **Actually not all URLs contain a `://`** Consider for instance 
`mailto:jane@example.com`. This is a valid URL/URI but does not use a `://`.
In fact the URL spec says that if you are not using a host or Authority (See the
FAQ entry above) you must not use `://`; use a plain colon `:`
after a URL scheme (i.e. a PURL **type**).

**QUESTION**: Can I use a CPE instead of a PURL

**ANSWER**: **Not really... no and yes!** CPE https://en.wikipedia.org/wiki/Common_Platform_Enumeration
are URIs and fairly close to PURL concepts but they are rather complex and
there are subtle differences:`cpe:2.3:a:artifex:ghostscript:8_64:*:*:*:*:*:*:*`

CPEs originated in the world of proprietary software security and require a
'vendor' attribute before the 'name' attribute, somewhat similar to a purl
**namespace** but not exactly. These names are assigned centrally and
arbitrarily by NIST and Mitre. For instance, the vendor for `zlib` is
`GNU`: this does not make any sense.

In contrast, PURL names are not centrally or arbitrarily assigned or
created: they are naturally and directly derived from whatever name a
package author picked. Also CPEs specifies rather complex version semantics
and can be hard to parse and build. They often mesh poorly with the
world of software packages and are difficukt to map to actual
common software packages as used in software development.

Yet CPEs can be a useful additional reference when they exist to relate a
package to known NVD vulnerabilities (CVE). A valuable side project could
be to create and maintain mappings of PURL to known CPEs.

**QUESTION**: Why not use the ISO 19770-2 spec for SWID tags instead of a PURL?

**ANSWER**: **Avoid this...** This is a proprietary and opaque specification with a
centrally managed pay-for-play registry (tagvault). Its purpose is primarily
to help inventory installed proprietary software by assigning arbitrary tags 
to a software binary.

In contrast a PURL is an open way to identify and locate a software
package as used in modern software development with no arbitrary central
name assignments needed.


