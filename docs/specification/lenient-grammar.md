# Lenient Grammar

A *canonical* PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).


```abnf
lenient-PURL = scheme ":" *"/" lenient-type 
               [ "/" lenient-namespace ] "/" lenient-name *"/"
               [ "@" lenient-version ] 
               [ "?" lenient-qualifiers ] 
               [ "#" lenient-subpath ]

lenient-type = ALPHA *( alphanumeric / "." / "-" )

; exmaples:
; - "" - an empty string
; - "///" - many empty segments
; - "//foo//bar//"
lenient-namespace = lenient-namespace-segment *( "/" lenient-namespace-segment )
lenient-namespace-segment = *lenient-pchar

lenient-name = 1*lenient-pchar

; exmaples:
; - ""  - an empty string
; - "0.8.15"
lenient-version = *lenient-pchar

; examples:
; - ""  - an empty string
; - "&&&" - many empty qualifiers
; - "FOO&bar=" - keys without values
; - "foo=123&bar=baz"
lenient-qualifiers = lenient-qualifier *( "&" lenient-qualifier )
lenient-qualifier = lenient-qualifier-key [ "=" lenient-qualifier-value ]
lenient-qualifier-key = ALPA *( ALPHA / DIGIT )
lenient-qualifier-value = *lenient-pchar

; examples:
; - "" - an empty string
; - "//foo//./bar/%2E%2E//" - not canonical but probably usable
; - "foo%2Fbar" - parser error
lenient-subpath = lenient-subpath-segment *( "/" lenient-subpath-segment )
lenient-subpath-segment = *lenient-pchar

lenient-pchar = unreserved / pct-encoded

; Note -- The sequence of decoded octets MUST form
;         a valid UTF-8 encoding per [RFC3629].
pct-encoded = "%" HEXDIG HEXDIG


; the following are carried over from canonical PURL grammar

scheme = %x70.6B.67 ; constant with the value "pkg"

alphanumeric = ALPHA / DIGIT
punctuation = "." / "-" / "_" / "~"
separator = ":" / "/" / "@" / "?" / "=" / "&" / "#"

unreserved = alphanumeric / punctuation / ":"
reserved   = "/" / "@" / "?" / "=" / "&" / "#"
```
