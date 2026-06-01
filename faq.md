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
package **type** that list allowed characters shall be composed only of ASCII letters and numbers, period '.', and dash '-'

As a result, a PURL spec implementation shall return an error when
encountering a **type** that contains a prohibited character.

## Version

**QUESTION**: How do package **types** handle the comparison and sorting of
versions?

**ANSWER**: Some package **types** use versioning conventions such as SemVer
for NPMs or NEVRA conventions for RPMs. A **type** may define a procedure to
compare and sort versions, but there is no reliable and uniform way to do
such comparison consistently.

## Plus character

**QUESTION**: Can a PURL contain a plus character '+'?

**ANSWER**: Decoded individual PURL components can contain a plus. The 
encoded, canonical form can never contain an unencoded plus.

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
