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
to the parsing and canonicalization rules of [the standard](standard/specification.md),
and reject it only where no meaningful interpretation is possible.  
Emitters shall never produce lenient PURL strings; output shall always be in
canonical form.

A *lenient* PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
lenient-PURL = scheme ":" *"/" lenient-type
               [ "/" lenient-namespace ] "/" lenient-name *"/"
               [ "@" lenient-version ]
               [ "?" lenient-qualifiers ]
               [ "#" lenient-subpath ]

scheme = %x70.6B.67 ; constant with the value "pkg"

lenient-type = ALPHA *( ALPHA / DIGIT / "." / "-" )

; examples:
; - "" - an empty string
; - "///" - many empty segments
; - "//foo//bar//"
lenient-namespace = lenient-namespace-segment *( "/" lenient-namespace-segment )
lenient-namespace-segment = *uoctet

lenient-name = 1*uoctet

; examples:
; - ""  - an empty string
; - "0.8.15"
lenient-version = *uoctet

; examples:
; - ""  - an empty string
; - "&&&" - many empty qualifiers
; - "FOO&bar=" - keys without values
; - "foo=123&bar=baz&repository_url=https:%2F%2Fexample.com%2Frepo"
lenient-qualifiers = lenient-qualifier *( "&" lenient-qualifier )
lenient-qualifier = [ lenient-qualifier-key [ "=" lenient-qualifier-value ] ]
lenient-qualifier-key = ALPHA *( ALPHA / DIGIT / "." / "-" / "_" )
lenient-qualifier-value = *uoctet

; examples:
; - "" - an empty string
; - "//foo//./bar/%2E%2E//" - not canonical but probably usable
; - "foo%2Fbar" - matches, but yields a parser error
lenient-subpath = lenient-subpath-segment *( "/" lenient-subpath-segment )
lenient-subpath-segment = *uoctet

uoctet = %x00-FF
```

Conformance to this grammar is necessary but not sufficient: the following
constraints of the specification are not expressible in ABNF and apply in
addition.

- After percent-decoding, the octets of each component shall form a valid
  UTF-8 encoding per [RFC 3629](https://datatracker.ietf.org/doc/html/rfc3629).
- When a string admits multiple parses under this grammar, component boundaries are
  determined by the parsing rules of [the standard](standard/specification.md)
  and the ["How to parse" specification](how-to-parse.md).
