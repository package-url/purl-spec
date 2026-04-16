# Git purl type
The git purl type is a primitive type intended to be used as a base case for encoding information about a code base which exists under git version control.

## Definitions
namespace: The namespace for this purl type is defined as the url path to the git host. 
eg. The `host` in git terminology.
https://git-scm.com/docs/git-clone.html#_git_urls 

name: The name for this purl type is the path on the host to the codebase 
eg. The `path-to-git-repo` in git terminology.
https://git-scm.com/docs/git-clone.html#_git_urls 

version: The verison for this type defines a specific point in the lineage of the codebase. Generally this is a commit or tag, but can be any valid git reference.
eg. The `git reference` in git terminology
https://git-scm.com/book/en/v2/Git-Internals-Git-References