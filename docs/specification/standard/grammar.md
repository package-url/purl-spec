# Grammar

A *canonical* PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
PURL = scheme ":" type
       [ "/" namespace ] "/" name
       [ "@" version ] [ "?" qualifiers ] [ "#" subpath ]

scheme = %x70.6B.67 ; constant with the value "pkg"

type = alpha-lc *( alpha-lc / DIGIT / "." / "-" )

namespace = namespace-segment *( "/" namespace-segment )
namespace-segment = 1*pchar-ns

name = 1*pchar-ns

version = 1*pchar

qualifiers = qualifier *( "&" qualifier )
qualifier = qualifier-key "=" qualifier-value
qualifier-key = alpha-lc *( alpha-lc / DIGIT / "." / "-" / "_" )
qualifier-value = 1*pchar-ns

subpath = subpath-segment *( "/" subpath-segment )
subpath-segment = ( ".." pchar-ns
                  / "."  subpath-segment-sc
                  /      subpath-segment-sc
                  ) *pchar-ns
subpath-segment-sc = alphanumeric / "-" / "_" / "~" / pct-enc-ns

alphanumeric = ALPHA / DIGIT
alpha-lc = %x61-7A ; a-z
punctuation = "." / "-" / "_" / "~"
separator = ":" / "/" / "@" / "?" / "=" / "&" / "#"

unreserved = alphanumeric / punctuation / ":"
reserved   = "/" / "@" / "?" / "=" / "&" / "#"

pchar    = pchar-ns / "%2F"
pchar-ns = unreserved / pct-enc-ns

; Note -- The sequence of decoded octets MUST form
;         a valid UTF-8 encoding per [RFC3629].
pct-enc-ns = "%" ( ( "0" / "1" ) HEXDIG
                        ; %00-1F
                 / "2" ( DIGIT / "A" / "B" / "C" )
                        ; %20-2F except %2D ("-") %2E (".") and %2F ("/")
                 / "3" ( "B" / "C" / "D" / "E" / "F" )
                        ; %30-3F except %30-39 (0-9) %3A (":")
                 / "40"
                        ; %40-4F except %41-4F (A-O)
                 / "5" ( "B" / "C" / "D" / "E" )
                        ; %50-5F except %50-5A (P-Z) %5F ("_")
                 / "60"
                        ; %60-6F except %61-6F (a-o)
                 / "7" ( "B" / "C" / "D" / "F" )
                        ; %70-7F except %70-7A (p-z) %7E ("~")
                 / ( "8" / "9" / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG
                        ; %80-FF
                 ) ; all allowed percent encoded characters except %2F ("/")
```
