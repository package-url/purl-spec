---
name: Change registered PURL type
about: Document requirements to change a registered PURL type
title: 'Change registered PURL type: '
labels: PURL type change
assignees: ''

---

This is an issue template for proposing a *major* change or changes to the definition of a registered 
PURL type meaning a change to the structure of a `<purl-type>.definition.json` file.

There are generally two levels of changes to a registered PURL type:
- A *minor* change such as an update or correction of the documentation of a PURL **type**
component or examples. *Minor* changes do not require the use of this issue template, but should
be labeled "PURL type change".
- A *major* change that affects the structure of the PURL **type** definition such as adding
a PURL **type** component to the definition or changing whether a PURL **type** component
is optional/prohibited/required.

To request changes(s) to a registered PURL **type** you should explain:
- [ ] What are the specific changes to the PURL **type** component definitions?
- [ ] Why are the changes needed?
- [ ] What input do you have from the relevant package ecosystem/community?
- [ ] What is the expected impact on tools that use the "pre-change" PURL **type** definition?
- [ ] Can you provide a tool or documentation for converting "pre-change" PURLs?
- [ ] Are there any open questions or concerns about the proposed change(s)?

A draft PR is a good way to document the specific proposed changes for the PURL component level definitions 
in the format of a `<purl-type>.definition.json` file. A PR is not a substitute for an issue for a *major* 
change because an issue should be the primary forum for the initial discussion.

A PR to change a registered PURL **type** will normally require changes to the **type**-specific test cases.

See https://www.packageurl.org/docs/purl/purl-types for overview information about PURL **type**s.

*NB: This is the first draft of this template.*
