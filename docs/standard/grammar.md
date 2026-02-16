# Package-URL Grammar

A PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
purl                      = scheme ":" *"/" type
                            [ 1*"/" namespace           ] 1*"/" name *"/"
                            [ "@" version ] [ "?" qualifiers           ]
                            [ "#" *"/" subpath      *"/" ]
                            ; leading/trailing slashes allowed here and there
purl-canonical            = scheme ":"      type-canonical
                            [   "/" namespace-canonical ]   "/" name
                            [ "@" version ] [ "?" qualifiers-canonical ]
                            [ "#"      subpath-canonical ]


scheme                    = %x70.6B.67    ; lowercase string "pkg"

type                      =    ALPHA *(    ALPHA / DIGIT / "." / "-" )
type-canonical            = LOWALPHA *( LOWALPHA / DIGIT / "." / "-" )

namespace                 = namespace-segment *( 1*"/" namespace-segment )
namespace-canonical       = namespace-segment *(   "/" namespace-segment )
namespace-segment         = 1*namespace-sc
namespace-sc              = PERM-ALPHANUM
                          / PERM-PUNCTUATION
                          / "%" ( PERM-ESCAPED-00-1F
                                / PERM-ESCAPED-20-2C
                                ; except puntuation: "-"   (2D)
                                ; except puntuation: "."   (2E)
                                ; except the separator "/" (2F)
                                / PERM-ESCAPED-30-FF )
                            ; namespace safe characters

name                      = 1*PCT-ENCODED

version                   = 1*PCT-ENCODED

qualifiers                = qualifier           *( "&" qualifier           )
qualifiers-canonical      = qualifier-canonical *( "&" qualifier-canonical )
qualifier                 = qualifier-key           "=" [ qualifier-value ]
qualifier-canonical       = qualifier-key-canonical "="   qualifier-value
qualifier-key             =    ALPHA *(    ALPHA / DIGIT / "." / "-" / "_" )
qualifier-key-canonical   = LOWALPHA *( LOWALPHA / DIGIT / "." / "-" / "_" )
qualifier-value           = 1*PCT-ENCODED

subpath                   = [ subpath-segment
                              *( 1*"/" subpath-segment           )
                            ]    ; zero or more segments
subpath-canonical         = [ subpath-segment-canonical
                              *(   "/" subpath-segment-canonical )
                            ]    ; zero or more segments
subpath-segment           =                   1*( subpath-sc / "." / "%2E" )
subpath-segment-canonical = [ "." ] subpath-sc *( subpath-sc / "." )
                            ; prevent "." and ".." standalone
                          / "." "."           1*( subpath-sc / "." )
                            ; prevent ".." standalone
subpath-sc                = PERM-ALPHANUM
                          / "-" / "_" / "~"  ; PERM-PUNCTUATION except "."
                          / "%" ( PERM-ESCAPED-00-1F
                                / PERM-ESCAPED-20-2C
                                ; except puntuation: "-"      (2D)
                                ; except the special char "." (2E)
                                ; except the separator "/"    (2F)
                                / PERM-ESCAPED-30-FF )
                            ; subpath safe characters


UPRALPHA    = %x41-5A    ; A-Z
LOWALPHA    = %x61-7A    ; a-z

PCT-ENCODED = PERM-ALPHANUM
            / PERM-PUNCTUATION
            / ":"    ; a specific separator that must not be encoded
            / PERM-ESCAPED

; permitted character classes
PERM-ALPHANUM    = ALPHA / DIGIT
PERM-PUNCTUATION = "." / "-" / "_" / "~"
PERM-SEPARATOR   = ":" / "/" / "@" / "?" / "=" / "&" / "#"
PERM-ESCAPED     = "%" ( PERM-ESCAPED-00-1F
                       / PERM-ESCAPED-20-2C
                       / PERM-ESCAPED-2D-2F
                       / PERM-ESCAPED-30-FF )
PERM-SPACE       = "%20"    ; escaped space

; applied purl spec rules for general character encoding
PERM-ESCAPED-00-1F = %x30-31                               HEXDIG    ; 00-1F
PERM-ESCAPED-20-2C = %x32             ( DIGIT / "A" / "B" / "C" )    ; 20-2C
PERM-ESCAPED-2D-2F = ; except puntuation "-"                          (2D)
                     ; except puntuation "."                          (2E)
                     %x32                                     "F"    ; 2F
PERM-ESCAPED-30-FF = ; except alphanumeric "0"-"9"                    (30-39)
                     ; except colon: ":"                              (3A)
                     %x33         ( "B" / "C" / "D" / "E" / "F" )    ; 3B-3F
                   / %x34                                    %x30    ; 40
                     ; except alphanumeric "A"-"Z"                    (41-5A)
                   / %x35               ( "B" / "C" / "D" / "E" )    ; 5B-5E
                     ; except puntuation: "_"                         (5F)
                   / %x36                                    %x30    ; 60
                     ; except alphanumeric "a"-"z"                    (61-7A)
                   / %x37                     ( "B" / "C" / "D" )    ; 7B-7D
                     ; except puntuation "~"                          (7E)
                   / %x37                                     "F"    ; 7F
                   / %x38-39                               HEXDIG    ; 80-9F
                   / ( "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG    ; A0-FF
```
