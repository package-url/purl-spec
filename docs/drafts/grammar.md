# Package-URL Grammar

A PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
;; ATTENTION: The following draft is AI generated and was note entirely revisited by a human, yet.
;; Simple query ran on Fable5: 
:: Read all files in https://github.com/package-url/purl-spec/tree/main/docs/specification/standard - do not read any other documents in the repo. Create me an ABNF for the thing described in this standard.

;; Package-URL (PURL) — ABNF
;; Derived from the Package-URL Core Specification
;; https://github.com/package-url/purl-spec/tree/fe214b861021ff32ad495627e3031d370c319b9e/docs/specification/standard
;;
;;     pkg:<type>/<namespace>/<name>@<version>?<qualifiers>#<subpath>

purl              = scheme ":" type
                    "/" [ namespace "/" ] name
                    [ "@" version ]
                    [ "?" qualifiers ]
                    [ "#" subpath ]

; a constant with the value "pkg" (case-sensitive)
scheme            = %x70.6B.67

; shall start with an ASCII letter; case insensitive, canonical form is lowercase
type              = ascii-letter *( ascii-letter / ascii-number / "." / "-" )

namespace         = namespace-segment *( "/" namespace-segment )
namespace-segment = percent-encoded-string

name              = percent-encoded-string

version           = percent-encoded-string

qualifiers        = qualifier *( "&" qualifier )
qualifier         = key "=" value

; shall start with an ASCII letter; shall not be percent-encoded
key               = lowercase-ascii-letter
                    *( lowercase-ascii-letter / ascii-number / "." / "-" / "_" )

value             = percent-encoded-string

subpath           = subpath-segment *( "/" subpath-segment )
subpath-segment   = percent-encoded-string

; unencoded: Alphanumeric Characters, Punctuation Characters, and colon ':'
percent-encoded-string    = 1*( alphanumeric-character
                              / punctuation-character
                              / ":"
                              / percent-encoded-character )
percent-encoded-character = "%" hex-digit hex-digit
:: REVIEW: must not include an encoded version of ":" or any alpha or such punctuations... 

alphanumeric-character    = ascii-letter / ascii-number

; period '.', dash '-', underscore '_', tilde '~'
punctuation-character     = "." / "-" / "_" / "~"

ascii-letter              = %x41-5A / %x61-7A
lowercase-ascii-letter    = %x61-7A
ascii-number              = %x30-39
hex-digit                 = ascii-number / %x41-46 / %x61-66
```