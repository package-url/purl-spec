<!-- 2026-05-01 10:10:09 (PT) Friday.  Created in VSCode on my 3530. -->
# This is a test .md file

- Let's create a row with scheme content to test how crowded this will look, especially with this large font.  And this intro:

- File info:

  - ID: jmh01

  - PURL: 'pkg:alpha/beta/gama@1.0.0?key=value#some/sub/path'

  - File source: 'src/2026-parse-purl/parse-purl-step-by-step-2026.05.01_v01.py'

  - Test PURL source: 'src/2026-purl-input-test-files/test-purls-for-how-to-parse-2026-04-22-v01.json'

  - Date: 2026-05-01 13:15 Fri

- The proposed how-to-parse starts just below:

---------------------------------------------------------

# How to Parse (test_group = "base")

Notes:

- This guide assumes that readers have familiarized themselves with:

  - the ECMA-427 specification (https://ecma-tc54.github.io/ECMA-427/#sec-purl-specification) and

  - the terms of the relevant [type]-definition.json file (https://github.com/package-url/purl-spec/tree/main/types) (collectively the 'PURL SPEC').

- Strict compliance: This document describes the parsing process for the 'base' test case.  With the exception of normalization steps described below, a parser is expected to raise an error if the input string fails in any way to comply with the 'PURL SPEC'.

- While this workflow moves primarily left-to-right, certain steps to identify optional PURL components (e.g., 'qualifiers' and 'subpaths') are handled most efficiently from the far right of the prospective PURL string.

- INPUT PURL (used below to illustrate the steps): 'pkg:alpha/beta/gama@1.0.0?key=value#some/sub/path'



<table>
<colgroup>
  <col width="50%">
  <col width="50%">
</colgroup>
<tr>
<th>Base</th>
<th>Advanced</th>
</tr>
<tr>
<td>

## 1. Scheme

- Split the input string once from the far left on ':'.

- The left side is the 'scheme'.

  - 'scheme' = 'pkg'

- The right side is the 'SCHEME REMAINDER'.

  - 'SCHEME REMAINDER' = 'alpha/beta/gama@1.0.0?key=value#some/sub/path'

- Strip all leading and trailing slashes '/' (e.g., '/', '//', '///' and so on) from the 'SCHEME REMAINDER'.

  - 'SCHEME REMAINDER' = 'alpha/beta/gama@1.0.0?key=value#some/sub/path'


</td>
<td>

## 1. Scheme

- Split the input string once from the far left on ':'.

- The left side is the 'scheme'.

  - 'scheme' = 'pkg'

- The right side is the 'SCHEME REMAINDER'.

  - 'SCHEME REMAINDER' = 'alpha/beta/gama@1.0.0?key=value#some/sub/path'

- Strip all leading and trailing slashes '/' (e.g., '/', '//', '///' and so on) from the 'SCHEME REMAINDER'.

  - 'SCHEME REMAINDER' = 'alpha/beta/gama@1.0.0?key=value#some/sub/path'
</td>
</tr>

<tr>
  <td>

## 2. Type

- Split the 'SCHEME REMAINDER' once from the left on '/'.

- The left side is the 'type'.

  - 'type' = 'alpha'

- The right side is the 'TYPE REMAINDER'.

  - 'TYPE REMAINDER' = 'beta/gama@1.0.0?key=value#some/sub/path'
  </td>
  <td>

## 2. Type

- Split the 'SCHEME REMAINDER' once from the left on '/'.

- The left side is the 'type'.

  - 'type' = 'alpha'

- The right side is the 'TYPE REMAINDER'.

  - 'TYPE REMAINDER' = 'beta/gama@1.0.0?key=value#some/sub/path'
  </td>
</tr>

<tr>
  <td>

## 3. Namespace

- In this 'namespace' section, we'll begin by collecting some data from the far right of the input string -- for the 'subpath' and 'qualifiers' components (if any).

### A. Split 'TYPE REMAINDER'

- Split the 'TYPE REMAINDER' once from the right on '#'.

- The left side is the 'NAMESPACE-QUALIFIERS SEGMENT'

  - 'NAMESPACE-QUALIFIERS SEGMENT' = 'beta/gama@1.0.0?key=value'

- The right side is the 'SUBPATH STRING'

  - 'SUBPATH STRING' = 'some/sub/path'

- We'll return to the 'SUBPATH STRING' in section 7. Subpath below.

------

### B. Split 'NAMESPACE-QUALIFIERS SEGMENT'

- Split the 'NAMESPACE-QUALIFIERS SEGMENT' once from the right on '?'.

- The left side is the 'NAMESPACE-VERSION SEGMENT'

  - 'NAMESPACE-VERSION SEGMENT' = 'beta/gama@1.0.0'

- The right side is the 'QUALIFIERS STRING'

  - 'QUALIFIERS STRING' = 'key=value'

- We'll return to the 'QUALIFIERS STRING' in section 6. Qualifiers below.

------

### C. Split 'NAMESPACE-VERSION SEGMENT'

- Split the 'NAMESPACE-VERSION SEGMENT' once from the right on '/'.

- The left side is the 'NAMESPACE STRING'

  - 'NAMESPACE STRING' = 'beta'

- The right side is the 'NAME-VERSION SEGMENT'

  - 'NAME-VERSION SEGMENT' = 'gama@1.0.0'

- If the 'NAMESPACE STRING' has no value, there is no 'namespace'.

- If the 'NAMESPACE STRING' has a value:
  - Remove all leading and trailing slashes '/'.
  - Split the 'NAMESPACE STRING' on '/'.
  - Percent-decode each segment.
  - UTF-8-decode each segment if needed in your programming language.
  - Join the segments back with a '/'.

- This is the 'namespace':

  - 'namespace' = 'beta'
  </td>
  <td>

## 3. Namespace

- In this 'namespace' section, we'll begin by collecting some data from the far right of the input string -- for the 'subpath' and 'qualifiers' components (if any).

### A. Split 'TYPE REMAINDER'

- Split the 'TYPE REMAINDER' once from the right on '#'.

- The left side is the 'NAMESPACE-QUALIFIERS SEGMENT'

  - 'NAMESPACE-QUALIFIERS SEGMENT' = 'beta/gama@1.0.0?key=value'

- The right side is the 'SUBPATH STRING'

  - 'SUBPATH STRING' = 'some/sub/path'

- We'll return to the 'SUBPATH STRING' in section 7. Subpath below.

------

### B. Split 'NAMESPACE-QUALIFIERS SEGMENT'

- Split the 'NAMESPACE-QUALIFIERS SEGMENT' once from the right on '?'.

- The left side is the 'NAMESPACE-VERSION SEGMENT'

  - 'NAMESPACE-VERSION SEGMENT' = 'beta/gama@1.0.0'

- The right side is the 'QUALIFIERS STRING'

  - 'QUALIFIERS STRING' = 'key=value'

- We'll return to the 'QUALIFIERS STRING' in section 6. Qualifiers below.

------

### C. Split 'NAMESPACE-VERSION SEGMENT'

- Split the 'NAMESPACE-VERSION SEGMENT' once from the right on '/'.

- The left side is the 'NAMESPACE STRING'

  - 'NAMESPACE STRING' = 'beta'

- The right side is the 'NAME-VERSION SEGMENT'

  - 'NAME-VERSION SEGMENT' = 'gama@1.0.0'

- If the 'NAMESPACE STRING' has no value, there is no 'namespace'.

- If the 'NAMESPACE STRING' has a value:
  - Remove all leading and trailing slashes '/'.
  - Split the 'NAMESPACE STRING' on '/'.
  - Percent-decode each segment.
  - UTF-8-decode each segment if needed in your programming language.
  - Join the segments back with a '/'.

- This is the 'namespace':

  - 'namespace' = 'beta'
  </td>
</tr>

<tr>
  <td>

## 4. Name

- In the prior section, we defined the 'NAME-VERSION SEGMENT' as 'gama@1.0.0'.

- Split the 'NAME-VERSION SEGMENT' once from the right on '@'.

- The left side is the 'NAME STRING'.

  - 'NAME STRING' = 'gama'

- The right side is the 'VERSION STRING'.

  - 'VERSION STRING' = '1.0.0'

- Remove all leading and trailing slashes '/' from the 'NAME STRING'.
- Percent-decode the 'NAME STRING'.
- UTF-8-decode the 'NAME STRING' if needed in your programming language.

- This is the 'name':

  - 'name' = 'gama'
  </td>
  <td>

## 4. Name

- In the prior section, we defined the 'NAME-VERSION SEGMENT' as 'gama@1.0.0'.

- Split the 'NAME-VERSION SEGMENT' once from the right on '@'.

- The left side is the 'NAME STRING'.

  - 'NAME STRING' = 'gama'

- The right side is the 'VERSION STRING'.

  - 'VERSION STRING' = '1.0.0'

- Remove all leading and trailing slashes '/' from the 'NAME STRING'.
- Percent-decode the 'NAME STRING'.
- UTF-8-decode the 'NAME STRING' if needed in your programming language.

- This is the 'name':

  - 'name' = 'gama'
  </td>
</tr>

<tr>
  <td>

## 5. Version

- In the previous section, we defined 'VERSION STRING' as '1.0.0'.

- Percent-decode the 'VERSION STRING'.
- UTF-8-decode the 'VERSION STRING' if needed in your programming language.

- This is the 'version':

  - 'version' = '1.0.0'
  </td>
  <td>

## 5. Version

- In the previous section, we defined 'VERSION STRING' as '1.0.0'.

- Percent-decode the 'VERSION STRING'.
- UTF-8-decode the 'VERSION STRING' if needed in your programming language.

- This is the 'version':

  - 'version' = '1.0.0'
  </td>
</tr>

<tr>
  <td>

## 6. Qualifiers

- In section 3.B, we defined the 'QUALIFIERS STRING':

  - 'QUALIFIERS STRING' = 'key=value'

- Split the 'qualifiers' on '&'. Each part is a 'key=value' pair.

- For each pair, split the 'key=value' once from the left on '='.

  - The 'key' is the left side.

  - Percent-decode the right side -- this is the 'value'.

  - UTF-8-decode the 'value- if needed in your programming language.

- This is the 'qualifiers' object:
  </td>
  <td>

## 6. Qualifiers

- In section 3.B, we defined the 'QUALIFIERS STRING':

  - 'QUALIFIERS STRING' = 'key=value'

- Split the 'qualifiers' on '&'. Each part is a 'key=value' pair.

- For each pair, split the 'key=value' once from the left on '='.

  - The 'key' is the left side.

  - Percent-decode the right side -- this is the 'value'.

  - UTF-8-decode the 'value- if needed in your programming language.

- This is the 'qualifiers' object:
  </td>
</tr>

<tr>
  <td>

## 7. Subpath

- We defined the 'SUBPATH STRING' is section 3.A:

  - 'SUBPATH STRING' = 'some/sub/path'

- Remove all leading and trailing slashes '/'.
- Split the 'SUBPATH STRING' on '/'.
- Percent-decode each segment.
- UTF-8-decode each segment if needed in your programming language.
- Join the segments back with a '/'.

- This is the 'subpath':

  - 'subpath' = 'some/sub/path'
  </td>
  <td>

## 7. Subpath

- We defined the 'SUBPATH STRING' is section 3.A:

  - 'SUBPATH STRING' = 'some/sub/path'

- Remove all leading and trailing slashes '/'.
- Split the 'SUBPATH STRING' on '/'.
- Percent-decode each segment.
- UTF-8-decode each segment if needed in your programming language.
- Join the segments back with a '/'.

- This is the 'subpath':

  - 'subpath' = 'some/sub/path'
  </td>
</tr>

<tr>
  <td>

## Summary

INPUT PURL: 'pkg:alpha/beta/gama@1.0.0?key=value#some/sub/path'

Parsed INPUT PURL:

- scheme = 'pkg'
- type = 'alpha'
- namespace = 'beta'
- name = 'gama'
- version = '1.0.0'
- qualifiers =
```
{
  "key": "value"
}
```
- subpath = 'some/sub/path'
  </td>
  <td>

## Summary

INPUT PURL: 'pkg:alpha/beta/gama@1.0.0?key=value#some/sub/path'

Parsed INPUT PURL:

- scheme = 'pkg'
- type = 'alpha'
- namespace = 'beta'
- name = 'gama'
- version = '1.0.0'
- qualifiers =
```
{
  "key": "value"
}
```
- subpath = 'some/sub/path'
  </td>
</tr>

</table>



That's all for now!
