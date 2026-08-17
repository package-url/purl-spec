# Grammar

## Canonical PackageURL

See [grammar in the standard](standard/grammar.md).

## Lenient PackageURL

A lenient PURL string adheres to the following grammar,
using syntax as per [RFC5234: Augmented BNF for Syntax Specifications: ABNF](https://datatracker.ietf.org/doc/html/rfc5234).

Built on the grammar of canonical PackageURL and reuses rules from it.

```abnf
lenient-PURL = scheme ":" *"/"
               lenient-type
               [ 1*"/" namespace *"/" ]
               1*"/" name *"/"
               [ "@" version ]
               [ "?" qualifiers ]
               [ "#" *"/" subpath *"/" ]

lenient-type = ALPHA *( ALPHA / DIGIT / "." / "-" )
```
