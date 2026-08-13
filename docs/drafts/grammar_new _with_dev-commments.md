# Package-URL Grammar

A PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
;; scheme:type/namespace/name@version?qualifiers#subpath

; Canonical PackageURL string
purl = scheme ":" 
       type 
       [ "/" namespace ]
       "/" name 
       [ "@" version ] 
       [ "?" qualifiers ] 
       [ "#" subpath ]

; Parsing PackageURL string
;; TO BE DISCUSSED: the spec usess "shall" all over, bt then gives exceptions for almost everything.
;;                  do we need to allow the separators without a component?
;;                  - like `["@" [version] ]`
;;                  - like `["#" [subpath] ]` - see discussion on subpath
purl-lenient = scheme ":" *"/" ;; REMARK: PURL parsers shall accept URLs where the **scheme** and colon ':' are followed by one or more slash '/' characters, such as 'pkg://', and shall ignore and remove all such '/' characters.
               type-lenient
               [ 1*"/" namespace *"/" ]  ;; REMARK: All leading and trailing slashes '/' are not significant and should be stripped in the canonical form. They are not part of the **namespace**.
               1*"/" name *"/" ;; REMARK: All leading and trailing slashes '/' are not significant and should be stripped in the canonical form. They are not part of the **name**.
               [ "@" version ]
               [ "?" qualifiers ]
               [ "#" *"/" subpath *"/" ]  ;; REMARK: Leading and trailing slashes '/' are not significant and should be stripped in the canonical form.

;; Section "Rules for each PURL component"

;; Sub-section "Scheme"
; constant with the value "pkg"
scheme = %x70.6B.67

;; Sub-section "Type"
type = alpha-lowercase *( alpha-lowercase / DIGIT / "." / "-" )
type-lenient = ALPHA *( ALPHA / DIGIT / "." / "-" )

;; Sub-section "Namespace"
namespace = namespace-segment *( "/" namespace-segment )
;; TO BE DISCUSSED:
;; - spec: When percent-decoded, a segment: [...] may contain any Unicode character other than '/' unless the package's **type** definition provides otherwise
;; - so the type definition make '/' an allowed encoded character here? - so basically we have no exclusions???
namespace-segment = 1*( pchar-ns )

;; Sub-section "Name"
name = 1*( pchar-ns )

;; Sub-section "Version"
version = 1*( pchar )

;; Sub-section "Qualifiers"
qualifiers = qualifier *( "&" qualifier )
;; TO BE DISCUSSED: do we need a lenient form? docs say: a **key=value** pair with an empty
  **value** is the same as if no **key=value** pair exists for this **key**.
qualifier = qualifiers-key "=" qualifiers-value
qualifier-key = alpha-lowercase *( alpha-lowercase / DIGIT )
qualifier-value = 1*( pchar-ns )

;; Sub-section "Subpath"
;; TO BE DISCUSSED: subpath may be empty according to spec
;; > prefixed by a '#' separator when not empty [...]
;; > The **subpath** contains zero or more segments [...]
subpath = [ subpath-segment *( "/" subpath-segment ) ]
subpath-segment = [ ".." pchar-ns
                  / "." ( alphanumeric-characters / "-" / "_" / "~" / pct-encoded-ns )
                  / ( alphanumeric-characters / "-" / "_" / "~" / pct-encoded-ns )
                  ] *( pchar-ns )
   

;; Section "Permitted characters"
alphanumeric-characters = ALPHA / DIGIT
punctuation-characters = "." / "-" / "_" / "~"
separator-characters = ":" / "/" / "@" / "?" / "=" / "&" / "#"  ;; REMARK: not used - can be dropped from gramar
percent-character = "%"

unreserved = alphanumeric-characters / punctuation-characters

pchar    = unreserved / pct-encoded
pchar-ns = unreserved / pct-encoded-ns


;; sction "Character encoding"

pct-encoded    = percent-character ( pct-encoded-nli-ascii-ns / "2F" / pct-encoded-nli-utf8-multi )
pct-encoded-ns = percent-character ( pct-encoded-nli-ascii-ns    /     pct-encoded-nli-utf8-multi )

pct-encoded-nli-ascii-ns = ( "0" / "1" ) HEXDIG                        ; %x00-1F
                         / "2" ( DIGIT / "A" / "B" / "C" )             ; %x20-2F except %x2D ("-") %x2E (".") %x2F ("/")
                         / "3" ( DIGIT / "B" / "C" / "D" / "E" / "F" ) ; except %x3A (":")
                         / "40"                                        ; %x40-4F except %x41-4F (A-O)
                         / "5" ( "B" / "C" / "D" / "E" )               ; %x50-5F except %x50-5A (P-Z) %x5F ("_")
                         / "60"                                        ; %x60-6F except %x61-6F (a-o)
                         / "7" ( "B" / "C" / "D" / "F" )               ; %x70-7F except %x70-7A (p-z) %x7E ("~")
pct-encoded-nli-utf8-multi = pct-encoded-nli-utf8-multi2 
                           / pct-encoded-nli-utf8-multi3
                           / pct-encoded-nli-utf8-multi4
; UTF8-2 / UTF8-3 / UTF8-4 ; - taken from https://datatracker.ietf.org/doc/html/rfc3629#section-4
; NOTE -- The authoritative definition of UTF-8 is in [UNICODE].  This
;         grammar is believed to describe the same thing Unicode describes, but
;         does not claim to be authoritative.  Implementors are urged to rely
;         on the authoritative source, rather than on this ABNF.
pct-encoded-nli-utf8-multi2 = ( "C" ("2" / "3" / "4" / "5" / "6" / "7" / "8" / "9" / "A" / "B" / "C" / "D" / "E" / "F" ) / "D" HEXDIG ) pct-encoded-utf8-trail ; %xC2-DF UTF8-tail
pct-encoded-nli-utf8-multi3 = "E0" percent-character ( "A" / "B" ) HEXDIG pct-encoded-utf8-trail ; %xE0 %xA0-BF UTF8-tail 
                            / "E" ( "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9" / "A" / "B" / "C" ) 2( pct-encoded-utf8-trail ); %xE1-EC 2( UTF8-tail ) 
                            / "ED" percent-character ( "8" / "9" ) HEXDIG pct-encoded-utf8-trail ; %xED %x80-9F UTF8-tail 
                            / "E" ( "E" / "F" ) 2( pct-encoded-utf8-trail ) ; %xEE-EF 2( UTF8-tail )
pct-encoded-nli-utf8-multi4 = "F0" percent-character ( "9" / "A" / "B" ) HEXDIG 2( pct-encoded-utf8-trail ) ; %xF0 %x90-BF 2( UTF8-tail ) 
                            / "F" ( "1" / "2" / "3" ) 3( pct-encoded-utf8-trail )                           ; %xF1-F3 3( UTF8-tail ) 
                            / "F4" percent-character "8" HEXDIG 2( pct-encoded-utf8-trail )                 ; %xF4 %x80-8F 2( UTF8-tail )
pct-encoded-utf8-trail = percent-character ("8" / "9" / "A" / "B" ) HEXDIG  ; %x80-BF

;; section "Case folding"
alpha-lowercase = %61-7A ; a-z

```
