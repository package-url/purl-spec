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

; examples:
; - "" - an empty string
; - "///" - many empty segments
; - "//foo//bar//"
lenient-namespace = lenient-namespace-segment *( "/" lenient-namespace-segment )
lenient-namespace-segment = *utf8-octet

lenient-name = 1*utf8-octet

; examples:
; - ""  - an empty string
; - "0.8.15"
lenient-version = *utf8-octet

; examples:
; - ""  - an empty string
; - "&&&" - many empty qualifiers
; - "FOO&bar=" - keys without values
; - "foo=123&bar=baz&repository_url=https:%2F%2Fexample.com%2Frepo"
lenient-qualifiers = lenient-qualifier *( "&" lenient-qualifier )
lenient-qualifier = [ lenient-qualifier-key [ "=" lenient-qualifier-value ] ]
lenient-qualifier-key = ALPHA *( ALPHA / DIGIT / "." / "-" / "_" )
lenient-qualifier-value = *utf8-octet

; examples:
; - "" - an empty string
; - "//foo//./bar/%2E%2E//" - not canonical but probably usable
; - "foo%2Fbar" - parser error
lenient-subpath = lenient-subpath-segment *( "/" lenient-subpath-segment )
lenient-subpath-segment = *utf8-octet

utf8-octet = %x00-FF
```

Conformance to this grammar is necessary but not sufficient: the following
constraints of the specification are not expressible in ABNF and apply in
addition.

- The octets decoded from a sequence of `utf8-octet` shall form a
  valid UTF-8 encoding per [RFC 3629](https://datatracker.ietf.org/doc/html/rfc3629).
