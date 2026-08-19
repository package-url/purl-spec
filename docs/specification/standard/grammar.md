# Grammar

A *canonical* PURL string adheres to the following grammar,
using syntax as per [RFC 5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
PURL = scheme ":" type
       [ "/" namespace ] "/" name
       [ "@" version ] [ "?" qualifiers ] [ "#" subpath ]

; --- structure ---

scheme = %x70.6B.67 ; constant with the value "pkg" (lowercase only)

type = alpha-lc *( alpha-lc / DIGIT / "." / "-" )

namespace = namespace-segment *( "/" namespace-segment )
namespace-segment = 1*pchar-ns

name = 1*pchar

version = 1*pchar

qualifiers = qualifier *( "&" qualifier )
qualifier = qualifier-key "=" qualifier-value
qualifier-key = alpha-lc *( alpha-lc / DIGIT / "." / "-" / "_" )
qualifier-value = 1*pchar

subpath = subpath-segment *( "/" subpath-segment )
subpath-segment = subpath-segment-sc *pchar-ns     ; no leading "."
                / "." subpath-segment-sc *pchar-ns ; forbid segment "."
                / ".." 1*pchar-ns                  ; forbid segment ".."
                       ; excludes the exact segments "." and ".."
subpath-segment-sc = ( alphanumeric
                     / "-" / "_" / "~"
                     / colon )     ; = `unreserved` without "."
                   / pct-encoded-ns
                          ; safe characters

; --- character classes ---

alphanumeric = ALPHA / DIGIT
alpha-lc = %x61-7A ; a-z
punctuation = "." / "-" / "_" / "~"
percent = "%"
separator = ":" / "/" / "@" / "?" / "=" / "&" / "#"
colon = ":"

unreserved = alphanumeric / punctuation / colon
reserved   = "/" / "@" / "?" / "=" / "&" / "#"

; `reserved` / `separator` are not referenced directly;
; listed to document characters that require percent-encoding

pchar    = unreserved / pct-encoded
pchar-ns = unreserved / pct-encoded-ns
                ; -ns suffix = variant that forbids an encoded slash "/" (%2F)

; --- percent-encoding ---

pct-encoded    = pct-encoded-ns / percent "2" "F"
pct-encoded-ns = percent (
                      ( "0" / "1" ) HEXDIG
                         ; %00-1F
                    / "2" ( DIGIT / "A" / "B" / "C" )
                         ; %20-2F except %2D ("-") and %2E (".") and %2F ("/")
                    / "3" ( "B" / "C" / "D" / "E" / "F" )
                         ; %30-3F except %30-39 (0-9) and %3A (":")
                    / "4" "0"
                         ; %40-4F except %41-4F (A-O)
                    / "5" ( "B" / "C" / "D" / "E" )
                         ; %50-5F except %50-5A (P-Z) and %5F ("_")
                    / "6" "0"
                         ; %60-6F except %61-6F (a-o)
                    / "7" ( "B" / "C" / "D" / "F" )
                         ; %70-7F except %70-7A (p-z) and %7E ("~")
                    / ( "8" / "9" / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG
                         ; %80-FF
                    )
```

Conformance to this grammar is necessary but not sufficient: the following
constraints of the specification are not expressible in ABNF and apply in
addition.

- Each `qualifier-key` shall be unique within `qualifiers`.
- The octets decoded from a sequence of `pct-encoded`/`pct-encoded-ns` shall form a
  valid UTF-8 encoding per [RFC 3629](https://datatracker.ietf.org/doc/html/rfc3629).
- Type-specific rules may further restrict any component.
