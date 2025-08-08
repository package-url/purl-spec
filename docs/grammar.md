# Grammar

ABNF syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf

purl              = scheme ":" *"/" type
                    [ 1*"/" namespace ] 1*"/" name *"/"
                    [ "@" version ] [ "?" qualifiers ] [ "#" *"/" subpath *"/" ]
                            ; leading and trailing slashes allowed here and there
purl-canonical    = scheme ":"      type-canonical
                    [   "/" namespace ]   "/" name
                    [ "@" version ] [ "?" qualifiers ] [ "#"      subpath      ]

scheme            = %x70.6B.67    ; lowercase string "pkg"
                            ; per ABNF spec: strings are case insensitive [...] To specify a rule that is case sensitive, specify the characters individually.

type              = ALPHA    *( ALPHA    / DIGIT / "." / "-" )
type-canonical    = LOWALPHA *( LOWALPHA / DIGIT / "." / "-" )

namespace         = namespace-segment *( "/" namespace-segment )
namespace-segment = 1*namespace-sc
namespace-sc      = ALPHA / DIGIT / "." / "-" / "_" / "~"
                  / "%" ( %x30-31 / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG    ; unicode before   %20
                  / "%"   %x32         ( DIGIT / "A" / "B" / "C" / "D" / "E" )    ; unicode %2? - except "/"(%2F)
                  / "%" ( %x33-39 / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG    ; everything after %2F
                            ; namespace safe characters

name              = 1*PCT-ENCODED

version           = 1*PCT-ENCODED

qualifiers        = qualifier *( "&" qualifier )
qualifier         = qualifier-key "=" qualifier-value
qualifier-key     = LOWALPHA *( LOWALPHA / DIGIT / "." / "-" / "_" )
qualifier-value   = 1*PCT-ENCODED

subpath           = subpath-segment *( "/" subpath-segment )
                  / 0<subpath-sc>    ; empty
subpath-segment   = subpath-sc         *( subpath-sc / PCT-DOT )
                  / PCT-DOT subpath-sc *( subpath-sc / PCT-DOT )    ; prevent ".." and "."
                  / PCT-DOT PCT-DOT   1*( subpath-sc / PCT-DOT )    ; prevent ".."
subpath-sc        = ALPHA / DIGIT / "-" / "_" / "~"                               ; no "." 
                  / "%" ( %x30-31 / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG    ; unicode before   %20
                  / "%"   %x32               ( DIGIT / "A" / "B" / "C" / "D" )    ; unicode %2? - except "."(%2E) and "/"(%2F)
                  / "%" ( %x33-39 / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG    ; everything after %2F
                            ; subpath safe characters

LOWALPHA    = %x61-7A    ; a-z

PCT-ENCODED = PERM-ALPHANUM / PERM-PUNCT / PERM-ESCAPED
PCT-DOT     = "." / "%2E"

; permitted character classes
PERM-ALPHANUM = ALPHA / DIGIT
PERM-PUNCT    = "." / "-" / "_" / "~"
PERM-ESCAPED  = "%" HEXDIG HEXDIG
PERM-DELIM    = ":" / "/" / "@" / "?" / "=" / "&" / "#"

```
