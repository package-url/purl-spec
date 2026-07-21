# Git purl type
The git purl type is a primitive type intended to be used as a base case for encoding information about a code base which exists under git version control. The motivation for this purl type is to ensure that any code which is built on a git forge can be indexed primarily for the purposes of vulnerability management.

## Original registration

The transport choice for a git connection is explicitly out of scope for this type. The rational for omitting the transport is twofold; 
1. the content is not changed by choice of transport, and
2. the additional complexity that would result from encoding the transport is non-trivial.

Trailing `.git` suffixes are permitted and a discussion of the rational behind that choice can be seen here:
https://github.com/package-url/purl-spec/pull/823#discussion_r2891679635

## Definition notes

The specific parameters for this type have been constructed to be as similar as possible to the upstream git protocol definitions at:
https://git-scm.com/book/en/v2/Git-Internals-Git-References
Specific reference links are provided in the `types/git-definition.json` file.

## Usage notes

When a richer purl type is available users are advised to use that type over the primitive `git` type. 

Example: When referencing code on the GitHub platform the `GitHub` purl type should be preferred. The choice of the `GitHub` type will inform the reader of additional features that may be of value (Issues, discussions, packages, etc...).

## More Information
