# Grammar

## Canonical PURL

A *canonical* PURL string adheres to [the grammar in the standard](standard/grammar.md).

## Lenient PURL

While only *canonical* PURL strings conform to the standard, PURL strings
found in the wild are often malformed: they may contain redundant separators,
uppercase types, unencoded characters, empty components, or other deviations
from the canonical form.

The following grammar deliberately over-accepts: it describes the superset of inputs
that a PURL parser should attempt to process, rather than a second
conformance class. A string matching this grammar is not thereby a valid
PURL.  
Parsers should accept such input on a best-effort basis, normalize it according
to the parsing and canonicalization rules of [the standard](standard/specification.md)
and the ["How to parse a PURL" specification](how-to-parse.md),
and reject it only where no meaningful interpretation is possible.  
Emitters shall never produce lenient PURL strings; output shall always be in
canonical form.

A *lenient* PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).  
This grammar operates on a sequence of octets that is a
UTF-8 encoding per [RFC 3629](https://datatracker.ietf.org/doc/html/rfc3629);
input in any other transfer encoding must be transcoded to UTF-8
before being matched against this grammar.

```abnf
lenient-PURL = scheme ":" *"/" lenient-type
               [ "/" lenient-namespace ] "/" lenient-name *"/"
               [ "@" lenient-version ]
               [ "?" lenient-qualifiers ]
               [ "#" lenient-subpath ]

scheme = %x70.6B.67 ; constant with the value "pkg" (lowercase only)

; examples:
; - "foobar2000-plugin"
; - see more examples in the PURL test suite
lenient-type = ALPHA *( ALPHA / DIGIT / "." / "-" )

; examples:
; - "" - an empty string
; - "///" - many empty segments
; - "//foo//bar/baz///"
; - see more examples in the PURL test suite
lenient-namespace = lenient-namespace-segment *( "/" lenient-namespace-segment )
lenient-namespace-segment = *uchar

lenient-name = 1*uchar

; examples:
; - ""  - an empty string
; - "0.8.15"
; - see more examples in the PURL test suite
lenient-version = *uchar

; examples:
; - ""  - an empty string
; - "&&&" - many empty qualifiers
; - "FOO&bar=" - keys without values
; - "foo=123&bar=baz&repository_url=https:%2F%2Fexample.com%2Frepo"
; - see more examples in the PURL test suite
lenient-qualifiers = lenient-qualifier *( "&" lenient-qualifier )
lenient-qualifier = [ lenient-qualifier-key [ "=" lenient-qualifier-value ] ]
lenient-qualifier-key = ALPHA *( ALPHA / DIGIT / "." / "-" / "_" )
lenient-qualifier-value = *uchar

; examples:
; - "" - an empty string
; - "//foo//./bar/%2E%2E//" - not canonical but probably usable
; - "foo%2Fbar" - matches, but yields a parser error
; - see more examples in the PURL test suite
lenient-subpath = lenient-subpath-segment *( "/" lenient-subpath-segment )
lenient-subpath-segment = *uchar

uchar = UTF8-char ; as defined in RFC 3629, section 4
```

The rule `uchar` matches the UTF-8 encoding of any single
[Unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value) —
any code point in the ranges U+0000 to U+D7FF and U+E000 to U+10FFFF,
excluding the surrogate code points. The rule `UTF8-char` is defined by the
ABNF in [RFC 3629, section 4](https://datatracker.ietf.org/doc/html/rfc3629#section-4),
which excludes overlong encodings and encoded surrogates by construction.

Conformance to this grammar is necessary but not sufficient: the following
constraints of the specification are not expressible in ABNF and apply in
addition.

- Within each component, decoding is performed in two steps, in order:
  first, percent-encoded triplets are percent-decoded to characters;
  second, the percent-decoded component is decoded as UTF-8 per
  [RFC 3629](https://datatracker.ietf.org/doc/html/rfc3629).  
  While the grammar guarantees that the input itself is valid UTF-8,
  percent-encoded triplets may still yield arbitrary octets; a component in
  which the octets resulting from percent-decoding do not form a valid UTF-8
  encoding has no valid interpretation.
- When a string admits multiple parses under this grammar, component boundaries are
  determined by the parsing rules of [the standard](standard/specification.md)
  and the ["How to parse a PURL" specification](how-to-parse.md).