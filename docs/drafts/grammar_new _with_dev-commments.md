# Package-URL Grammar

A PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
;; scheme:type/namespace/name@version?qualifiers#subpath

; canonical PackageURL string
purl = scheme ":" 
       type 
       [ "/" namespace ]
       "/" name 
       [ "@" version ] 
       [ "?" qualifiers ] 
       [ "#" subpath ]

; parsing PackageURL string
;; TO BE DISCUSSED: the spec usess "shall" all over, bt then gives exceptions for almost everything.
;;                  do we need to allow the separators without a component?
;;                  - like `["@" [version] ]`
;;                  - like `["#" [subpath] ]` - see discussion on subpath
purl-lenient = scheme ":" *"/" ; REMARK: PURL parsers shall accept URLs where the **scheme** and colon ':' are followed by one or more slash '/' characters, such as 'pkg://', and shall ignore and remove all such '/' characters.
               type-lenient
               [ 1*"/" namespace-lenient *"/" ]  ; REMARK: All leading and trailing slashes '/' are not significant and should be stripped in the canonical form. They are not part of the **namespace**.
               1*"/" name *"/" ; REMARK: All leading and trailing slashes '/' are not significant and should be stripped in the canonical form. They are not part of the **name**.
               [ "@" version ]
               [ "?" qualifiers ]
               [ "#" *"/" subpath *"/" ]

;; Section "Rules for each PURL component"

;; Sub-section "Scheme"
; constant with the value "pkg"
scheme = %x70.6B.67

;; Sub-section "Type"
type = alpha-lowercase *(alpha-lowercase / DIGIT / "." / "-")
type-lenient = ALPHA *(ALPHA / DIGIT / "." / "-")

;; Sub-section "Namespace"
namespace = namespace-segment *( "/" namespace-segment )
namespace-lenient = namespace-segment *( "/" namespace-segment )
;; TODO: When percent-decoded, a segment:
;;       - shall not contain any slash '/' characters
;;       - may contain any Unicode character other than '/' unless the package's **type** definition provides otherwise
namespace-segment = 1*( alphanumeric-characters / percent-encoded )

;; Sub-section "Name"
name = 1*( alphanumeric-characters / percent-encoded )

;; Sub-section "Version"
version = 1*( alphanumeric-characters / percent-encoded )

;; Sub-section "Qualifiers"
qualifiers = qualifier *("&" qualifier)
;; TO BE DISCUSSED: dowe need a lenient form? docs say: a **key=value** pair with an empty
  **value** is the same as if no **key=value** pair exists for this **key**.
qualifier = qualifiers-key "=" qualifiers-value
qualifier-key = alpha-lowercase *(alpha-lowercase / DIGIT)
;; TODO: A **value** may contain any Unicode character and all characters shall be encoded as described in the _Character encoding_ clause.
qualifier-value = 1*percent-encoded

;; Sub-section "Subpath"
;; TO BE DISCUSSED: subpath may be empty according to spec
;; > prefixed by a '#' separator when not empty [...]
;; > The **subpath** contains zero or more segments [...]
subpath = [ subpath-segment *("/" subpath-segment) ]
subpath-segment = 1*(ALPHA / DIGIT / percent-encoded)  ; TODO may contain any Unicode character other than '/' unless the package's **type** definition provides otherwise.

subpath-segment

;; Section "Permitted characters"
alphanumeric-characters = ALPHA / DIGIT
percent-character = "%"
punctuation-characters = "." / "-" / "_" / "~"
separator-characters = ":" / "/" / "@" / "?" / "=" / "&" / "#"

;; sction "Character encoding"

;; TODO: The following characters shall not be percent-encoded:
;;       - the Alphanumeric Characters
;;       - the Punctuation Characters
;;       - the Separator Characters when being used as PURL separators
;;       - the colon ':', whether used as a Separator Character or otherwise
;;       - the percent sign '%' when used to represent a percent-encoded character
percent-encoded = "%" 2HEXDIG
percent-encoded-space = "%20"

;; section "Case folding"
alpha-lowercase = %61-7A ; a-z

```
