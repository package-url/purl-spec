# Package-URL Grammar

A PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

```abnf
;; ATTENTION: The following draft is AI generated and was note entirely revisited by a human, yet.
;; Simple query ran on Fable5: 
:: Read all files in https://github.com/package-url/purl-spec/tree/main/docs/specification/standard - do not read any other documents in the repo. Create me an ABNF for the thing described in this standard.

create me an ABNF for the thing described in this standard. 

; Package-URL (PURL) — ABNF derived from the PURL Core Specification
; https://github.com/package-url/purl-spec/tree/fe214b861021ff32ad495627e3031d370c319b9e/docs/specification/standard
; Syntax: RFC 5234 ABNF
;
;   scheme:type/namespace/name@version?qualifiers#subpath

purl            = scheme ":" purl-path
                  [ "?" qualifiers ]
                  [ "#" subpath ]

purl-path       = type "/" [ namespace "/" ] name [ "@" version ]
;; REVIEW: does the purl spec call this a `purl-path`???


; ---------------------------------------------------------------
; Scheme — constant "pkg".
; Note (parser leniency, non-canonical): parsers SHALL accept and
; strip one or more "/" after "pkg:", e.g. "pkg://".
; ---------------------------------------------------------------
scheme          = %s"pkg"
;; REVIEW: this %s"" is readable, but is an ABNF extension - see RFC7405 - which needs to be called out

; ---------------------------------------------------------------
; Type — ASCII letters/digits, ".", "-", "+"? No: only letters,
; digits, period and dash; must start with a letter; never
; percent-encoded. Canonical form is lowercase.
; ---------------------------------------------------------------
type            = ALPHA *( ALPHA / DIGIT / "." / "-" )
                  ; canonical form: lowercase only:
                  ; type = lc-alpha *( lc-alpha / DIGIT / "." / "-" )
;; REVIEW: per ABNF, comments must start at line start, or after a rule - not after some spaces.


; ---------------------------------------------------------------
; Namespace — optional; one or more non-empty percent-encoded
; segments separated by a single "/". Leading/trailing slashes
; are stripped in canonical form (not represented here).
; ---------------------------------------------------------------
namespace       = segment *( "/" segment )

; ---------------------------------------------------------------
; Name — required; a non-empty percent-encoded string.
; ---------------------------------------------------------------
name            = 1*pchar

; ---------------------------------------------------------------
; Version — optional; opaque percent-encoded string.
; ---------------------------------------------------------------
version         = 1*pchar

; ---------------------------------------------------------------
; Qualifiers — one or more key=value pairs separated by "&".
; Keys: lowercase ASCII letters, digits, ".", "-", "_";
; start with a letter; unique; never percent-encoded.
; Values: non-empty percent-encoded strings.
; ":" may appear unencoded in values per the encoding rules.
; ---------------------------------------------------------------
qualifiers      = qualifier *( "&" qualifier )
qualifier       = qkey "=" qvalue
qkey            = lc-alpha *( lc-alpha / DIGIT / "." / "-" / "_" )
qvalue          = 1*( pchar / ":" )

; ---------------------------------------------------------------
; Subpath — zero or more segments separated by "/"; segments are
; non-empty, percent-encoded, and (decoded) not "." or "..".
; Leading/trailing slashes stripped in canonical form.
; ---------------------------------------------------------------
subpath         = segment *( "/" segment )

; ---------------------------------------------------------------
; Common building blocks
; ---------------------------------------------------------------
; A non-empty percent-encoded segment. The constraint that a
; decoded segment is not "." or ".." (subpath only) cannot be
; fully expressed in ABNF and applies as a semantic rule.
segment         = 1*pchar

; Permitted, non-separator characters of a canonical PURL:
; alphanumerics, the punctuation ".", "-", "_", "~", and
; percent-encoded triplets.
pchar           = unreserved / pct-encoded
unreserved      = ALPHA / DIGIT / "." / "-" / "_" / "~"
pct-encoded     = "%" HEXDIG HEXDIG

lc-alpha        = %x61-7A          ; a-z

; Core rules used (RFC 5234): ALPHA, DIGIT, HEXDIG

```