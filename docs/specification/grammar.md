# Grammar

## Canonical PURL

A *canonical* PURL string adheres to [the grammar in the standard](standard/grammar.md).

## Lenient PURL

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

; exmaples:
; - "" - an empty string
; - "///" - many empty segments
; - "//foo//bar//"
lenient-namespace = lenient-namespace-segment *( "/" lenient-namespace-segment )
lenient-namespace-segment = *unicode

lenient-name = 1*unicode

; exmaples:
; - ""  - an empty string
; - "0.8.15"
lenient-version = *unicode

; examples:
; - ""  - an empty string
; - "&&&" - many empty qualifiers
; - "FOO&bar=" - keys without values
; - "foo=123&bar=baz"
lenient-qualifiers = lenient-qualifier *( "&" lenient-qualifier )
lenient-qualifier = lenient-qualifier-key [ "=" lenient-qualifier-value ]
lenient-qualifier-key = ALPA *( ALPHA / DIGIT )
lenient-qualifier-value = *unicode

; examples:
; - "" - an empty string
; - "//foo//./bar/%2E%2E//" - not canonical but probably usable
; - "foo%2Fbar" - parser error
lenient-subpath = lenient-subpath-segment *( "/" lenient-subpath-segment )
lenient-subpath-segment = *unicode

; Note -- The sequence of octets MUST form
;         a valid UTF-8 encoding per [RFC3629].
unicode = %x00-FF
```
