This README explains the use of decision documentation for the **purl-spec** 
project.

## Context and Problem

GitHub discussions, issues and pull requests are the primary documentation for
the development of the PURL specification and PURL data elements such as PURL
types and test cases. This works well for most changes, but there are some 
designs or other decisions where the GH issue format is limiting because:
- Using the body (first comment) of an issue for a proposal is problematic 
because any changes are not visible to a reader
- Comments for an issue are not threaded which typically makes an extended
series of comments hard to trace back to the original proposal and eventually
hard to follow at all.

## Solution

Our solution for making and recording major decisions needs to remain in the 
domain of our project repository to keep our project communications in one 
place. We are adapting a template and process from the [ADR project](https://github.com/adr/madr) for the **purl-spec** project. Our current approach is much simpler 
than ADR.

The key components of our current solution are:
- Decision documents are stored in the `docs/decisions` folder. They are not 
part of the PURL specification.
- Each decision document name is prefixed with a 3 digit sequential number. 
These sequence numbers are not re-used; e.g. we retain copies of documents 
that are 'rejected', 'deprecated' or 'superseded' with their original numbers 
and names.
- A decision document is created using the `decision_doc-template.md` file in 
this folder. 
- The key purposes for a decision document are to provide (1) a concise
proposal and (2) summary level information on its disposition.
- A change to a decision document requires a pull request and follows the
normal process for review and approval by the project maintainers.
- Comments other than those essential inside a pull request should be captured
 in a GH discussion or issue and referenced by links in the decision document.
- We plan to publish 'concluded' status documents to the [website](https://www.packageurl.org) along with guidance to review 'proposed' or other decision documents in GitHub. 


<!-- We have elected to use the ADR materials under the CC0-1. license -->
