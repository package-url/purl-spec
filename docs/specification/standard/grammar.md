# Grammar

A *canonical* PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
PURL = scheme ":" type
       [ "/" namespace ] "/" name
       [ "@" version ] [ "?" qualifiers ] [ "#" subpath ]

scheme = %x70.6B.67 ; constant with the value "pkg"

type = alpha-lowercase *( alpha-lowercase / DIGIT / "." / "-" )

namespace = namespace-segment *( "/" namespace-segment )
namespace-segment = 1*pchar-ns

name = 1*pchar-ns

version = 1*pchar

qualifiers = qualifier *( "&" qualifier )
qualifier = qualifier-key "=" qualifier-value
qualifier-key = alpha-lowercase *( alpha-lowercase / DIGIT )
qualifier-value = 1*pchar-ns

subpath = subpath-segment *( "/" subpath-segment )
subpath-segment = [ ".." pchar-ns
                  / "."  subpath-segment-sc
                  /      subpath-segment-sc
                  ] *pchar-ns
subpath-segment-sc = alphanumeric / "-" / "_" / "~" / pct-enc-ns

alphanumeric = ALPHA / DIGIT
alpha-lowercase = %61-7A ; a-z
punctuation = "." / "-" / "_" / "~"
separator = ":" / "/" / "@" / "?" / "=" / "&" / "#"

unreserved = alphanumeric / punctuation / ":"
reserved   = "/" / "@" / "?" / "=" / "&" / "#"

pchar    = pchar-ns / "%2F"
pchar-ns = unreserved / pct-enc-ns

; Note -- The sequence of decoded octets MUST form
;         a valid UTF-8 encoding per [RFC3629].
pct-enc-ns = "%" ( ( "0" / "1" ) HEXDIG
                        ; %x00-1F
                 / "2" ( DIGIT / "A" / "B" / "C" )
                        ; %x20-2F except %x2D ("-") %x2E (".") and %x2F ("/")
                 / "3" ( DIGIT / "B" / "C" / "D" / "E" / "F" )
                        ; %x30-3F except %x3A (":")
                 / "40"
                        ; %x40-4F except %x41-4F (A-O)
                 / "5" ( "B" / "C" / "D" / "E" )
                        ; %x50-5F except %x50-5A (P-Z) %x5F ("_")
                 / "60"
                        ; %x60-6F except %x61-6F (a-o)
                 / "7" ( "B" / "C" / "D" / "F" )
                        ; %x70-7F except %x70-7A (p-z) %x7E ("~")
                 / ( "8" / "9" / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG
                        ; %x80-FF
                 ) ; all allowed percent encoded characters except %x2F ("/")
```
