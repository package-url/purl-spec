# Grammar of a `purl` string

ABNF syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
purl                      = scheme ":" *"/" type
                            [ 1*"/" namespace           ] 1*"/" name *"/"
                            [ "@" version ] [ "?" qualifiers           ] [ "#" *"/" subpath      *"/" ]
                             ; leading and trailing slashes allowed here and there
purl-canonical            = scheme ":"      type-canonical
                            [   "/" namespace-canonical ]   "/" name
                            [ "@" version ] [ "?" qualifiers-canonical ] [ "#"      subpath-canonical ]

scheme                    = %x70.6B.67    ; lowercase string "pkg"

type                      =    ALPHA *(    ALPHA / DIGIT / "." / "-" )
type-canonical            = LOWALPHA *( LOWALPHA / DIGIT / "." / "-" )

namespace                 = namespace-segment *( 1*"/" namespace-segment )
namespace-canonical       = namespace-segment *(   "/" namespace-segment )
namespace-segment         = 1*namespace-sc
namespace-sc              = PERM-ALPHANUM
                          / PERM-PUNCTUATION
                          / "%" ( PERM-ESCAPED-00-1F
                                / PERM-ESCAPED-20-2C    ; 20-2F - except separator "/"(%2F) and general exclusion "-"(%2D) and "."(%2E) 
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

subpath                   = subpath-segment           *( 1*"/" subpath-segment           )
                          / 0<subpath-sc>    ; empty
subpath-canonical         = subpath-segment-canonical *(   "/" subpath-segment-canonical )
                          / 0<subpath-sc>    ; empty
subpath-segment           =               1*( subpath-sc / "." / "%2E" )
subpath-segment-canonical = [ "." ] subpath-sc *( subpath-sc / "." )    ; prevent "." and ".." standalone
                          / "." "."           1*( subpath-sc / "." )    ; prevent ".." standalone
subpath-sc                = PERM-ALPHANUM
                          / "-" / "_" / "~"             ; PERM-PUNCTUATION except "."
                          / "%" ( PERM-ESCAPED-00-1F
                                / PERM-ESCAPED-20-2C    ; 20-2F - except separator "/"(%2F) and special char "."(%2E) and general exclusion "-"(%2D)
                                / PERM-ESCAPED-30-FF )
                            ; subpath safe characters

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

; applied purl spec rules for general character encoding
PERM-ESCAPED-00-1F =   %x30-31                                       HEXDIG    ; 00-1F
PERM-ESCAPED-20-2C =   %x32                     ( DIGIT / "A" / "B" / "C" )    ; 20-2C
PERM-ESCAPED-2D-2F =                     ; except following characters: "-"     (2D)
                                         ; except following characters: "."     (2E)
                   /   %x32                                             "F"    ; 2F
PERM-ESCAPED-30-FF =                     ; except following characters: "0"-"9" (30-39)
                                         ; except following characters: ":"     (3A)
                       %x33                 ( "B" / "C" / "D" / "E" / "F" )    ; 3B-3F
                   /   %x34                                            %x30    ; 40
                                         ; except following characters: "A"-"Z" (41-5A)
                   /   %x35                       ( "B" / "C" / "D" / "E" )    ; 5B-5E
                                         ; except following characters: "_"     (5F)
                   /   %x36                                            %x30    ; 60
                                         ; except following characters: "a"-"z" (61-7A)
                   /   %x37                             ( "B" / "C" / "D" )    ; 7B-7D
                                         ; except following characters: "~"     (7E)
                   /   %x37                                             "F"    ; 7F
                   / ( %x38-39 / "A" / "B" / "C" / "D" / "E" / "F" ) HEXDIG    ; 80-FF
```
