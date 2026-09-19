# Package-URL Type Definition Schema

The PURL Type Definition JSON Schema is the reference data model that is used 
to define PURL types in a structured way. Each PURL type is specified in a 
JSON document that matches this schema. These JSON documents are then used to 
generate PURL type documentation and to support PURL libraries and tools so 
that they can more easily parse, build, and validate PURLs by type in a 
consistent and standardized manner across programming languages and technology 
stacks.

**6 Package-URL Type Definition Schema**

The PURL Type Definition JSON Schema is the reference data model that is used 
to define PURL types in a structured way. Each PURL type is specified in a 
JSON document that matches this schema. These JSON documents are then used to 
generate PURL type documentation and to support PURL libraries and tools so 
hat they can more easily parse, build, and validate PURLs by type in a 
consistent and standardized manner across programing languages and technology stacks.

**Location:** /  
**Type:** Object

Schema to specify a Package-URL (PURL) type as a structured definition.

Table 2: Properties for the root object

| **Property**          | **Type** | **Requirement** | **Description**                                                                                                                                                                                     |
| --------------------- | -------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                  | String   | Required        | The type string for this Package-URL type.                                                                                                                                                          |
| type_name             | String   | Required        | The name for this PURL type.                                                                                                                                                                        |
| description           | String   | Required        | The description of this PURL type.                                                                                                                                                                  |
| repository            | Object   | Required        | The package repository usage for this PURL type.                                                                                                                                                    |
| namespace_definition  | Array    | Required        | Definition of the namespace component for this PURL type. The PURL namespace component shall be required, optional or prohibited for a specific PURL type definition.                               |
| name_definition       | Array    | Required        | Definition of the name component for this PURL type. The PURL name component is required for all PURL type definitions.                                                                             |
| version_definition    | Array    | Optional        | Definition of the version component for this PURL type. The PURL version component is optional for a specific PURL type definition.                                                                 |
| qualifiers_definition | Array    | Optional        | Definition of the qualifiers specific to this PURL type. The PURL qualifiers component is optional for a specific PURL type, but a qualifiers key or keys may be required for a specific PURL type. |
| subpath_definition    | Array    | Optional        | The definition for the subpath for this PURL type. The PURL subpath component is optional for a specific PURL type definition.                                                                      |
| examples              | Array    | Required        | Example of valid, canonical PURLs for this package type.                                                                                                                                            |
| note                  | String   | Optional        | Note about this PURL type.                                                                                                                                                                          |
| reference_urls        | Array    | Optional        | Optional list of informational reference URLs about this PURL type.                                                                                                                                 |

**6.1 PURL type**

**Location:** /type  
**Property:** type (Required)  
**Type:** String  
**Pattern Constraint:** ^\[a-z\]\[a-z0-9-\\.\]+\$

The type string for this Package-URL type.

Example 1 (Informative)mavenExample 2 (Informative)npmExample 3 (Informative)pypi

**6.2 Type name**

**Location:** /type_name  
**Property:** type_name (Required)  
**Type:** String

The name for this PURL type.

Example 1 (Informative)Apache MavenExample 2 (Informative)Python Package

**6.3 Description**

**Location:** /description  
**Property:** description (Required)  
**Type:** String

The description of this PURL type.

**6.4 Repository**

**Location:** /repository  
**Property:** repository (Required)  
**Type:** Object

The package repository usage for this PURL type.

Table 3: Properties for the repository object

| **Property**           | **Type** | **Requirement** | **Description**                                              |
| ---------------------- | -------- | --------------- | ------------------------------------------------------------ |
| use_repository         | Boolean  | Required        | **true** if this PURL type uses a public package repository. |
| default_repository_url | String   | Optional        | The default public repository URL for this PURL type.        |
| note                   | String   | Optional        | Extra note text.                                             |

**6.4.1 Use repository**

**Location:** /repository/use_repository  
**Property:** use_repository (Required)  
**Type:** Boolean

**true** if this PURL type uses a public package repository.

**6.4.2 Default repository URL**

**Location:** /repository/default_repository_url  
**Property:** default_repository_url (Optional)  
**Type:** String  
**Format:** URI as specified in [RFC 3986](https://www.ietf.org/rfc/rfc3986.html)

The default public repository URL for this PURL type.

**6.4.3 Note**

**Location:** /repository/note  
**Property:** note (Optional)  
**Type:** String

Extra note text.

**6.5 Namespace definition**

**Location:** /namespace_definition  
**Property:** namespace_definition (Required)  
**Type:** Object

Definition of the namespace component for this PURL type. The PURL namespace 
component shall be required, optional or prohibited for a specific PURL type 
definition.

Table 4: Properties for the namespace_definition object

| **Property**         | **Type** | **Requirement** | **Description**                                                                                                                                                                                                                                                                                                |
| -------------------- | -------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| requirement          | Array    | Required        | States that the PURL namespace component is optional, required or prohibited for a PURL type.                                                                                                                                                                                                                  |
| permitted_characters | String   | Optional        | A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive       | Boolean  | Optional        | **true** if this PURL component is case sensitive. If **false**, the canonical form shall be lowercased.                                                                                                                                                                                                       |
| normalization_rules  | Array    | Optional        | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.                                                                        |
| native_name          | String   | Optional        | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.                                                                                                                                         |
| note                 | String   | Optional        | Extra note text.                                                                                                                                                                                                                                                                                               |

**6.5.1 Namespace requirement**

**Location:** /namespace_definition/requirement  
**Property:** requirement (Required)  
**Type:** String

States that the PURL namespace component is optional, required or prohibited 
for a PURL type.

_Shall be one of:_

- Component optional requirement
- Component required requirement
- Component prohibited requirement

**6.5.2 Component optional requirement**

**Type:** String  
**Constant:** optional

States that this PURL component is optional for a PURL type.

**6.5.3 Component required requirement**

**Type:** String  
**Constant:** required

States that this PURL component is required for a PURL type.

**6.5.4 Component prohibited requirement**

**Type:** String  
**Constant:** prohibited

States that this PURL component is prohibited for a PURL type.

**6.5.5 Permitted characters in this PURL component**

**Location:** /namespace_definition/permitted_characters  
**Property:** permitted_characters (Optional)  
**Type:** String  
**Format:** A regular expression dialect defined by [ECMA-262](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/)

A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) dialect) 
defining the 'Permitted characters' for this component of this Package-URL 
type. If provided, this shall be a subset of the 'Permitted characters' 
defined in the PURL specification.

**6.5.6 Case sensitive**

**Location:** /namespace_definition/case_sensitive  
**Property:** case_sensitive (Optional)  
**Type:** Boolean  
**Default Value:** **true**

**true** if this PURL component is case sensitive. If **false**, the canonical
 form shall be lowercased.

**6.5.7 Normalization rules**

**Location:** /namespace_definition/normalization_rules  
**Property:** normalization_rules (Optional)  
**Type:** array (of String)

List of rules to normalize this component for this PURL type. These are 
plain text, unstructured rules as some require programming and cannot be 
enforced only with a schema. Tools are expected to apply these rules 
programmatically. Each item of this array shall be a string.

_All items shall be unique._

**6.5.8 Native name**

**Location:** /namespace_definition/native_name  
**Property:** native_name (Optional)  
**Type:** String

The native name of this PURL component in the package ecosystem. For instance,
 the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' 
 PURL type.

**6.5.9 Note**

**Location:** /namespace_definition/note  
**Property:** note (Optional)  
**Type:** String

Extra note text.

**6.6 Name definition**

**Location:** /name_definition  
**Property:** name_definition (Required)  
**Type:** Object

Definition of the name component for this PURL type. The PURL name component 
is required for all PURL type definitions.

Table 5: Properties for the name_definition object

| **Property**         | **Type** | **Requirement** | **Description**                                                                                                                                                                                                                                                                                                |
| -------------------- | -------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| requirement          | Array    | Required        | States that the PURL name component is always required.                                                                                                                                                                                                                                                        |
| permitted_characters | String   | Optional        | A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive       | Boolean  | Optional        | **true** if this PURL component is case sensitive. If **false**, the canonical form shall be lowercased.                                                                                                                                                                                                       |
| normalization_rules  | Array    | Optional        | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.                                                                        |
| native_name          | String   | Optional        | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.                                                                                                                                         |
| note                 | String   | Optional        | Extra note text.                                                                                                                                                                                                                                                                                               |

**6.6.1 Name component requirement**

**Location:** /name_definition/requirement  
**Property:** requirement (Required)  
**Type:** String

States that the PURL name component is always required.

_Shall be one of:_

- Component required requirement

**6.6.2 Component required requirement**

**Type:** String  
**Constant:** required

States that this PURL component is required for a PURL type.

**6.6.3 Permitted characters in this PURL component**

**Location:** /name_definition/permitted_characters  
**Property:** permitted_characters (Optional)  
**Type:** String  
**Format:** A regular expression dialect defined by [ECMA-262](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/)

A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) 
dialect) defining the 'Permitted characters' for this component of this 
Package-URL type. If provided, this shall be a subset of the 'Permitted 
characters' defined in the PURL specification.

**6.6.4 Case sensitive**

**Location:** /name_definition/case_sensitive  
**Property:** case_sensitive (Optional)  
**Type:** Boolean  
**Default Value:** **true**

**true** if this PURL component is case sensitive. If **false**, the canonical
 form shall be lowercased.

**6.6.5 Normalization rules**

**Location:** /name_definition/normalization_rules  
**Property:** normalization_rules (Optional)  
**Type:** array (of String)

List of rules to normalize this component for this PURL type. These are plain 
text, unstructured rules as some require programming and cannot be enforced 
only with a schema. Tools are expected to apply these rules programmatically. 
Each item of this array shall be a string.

_All items shall be unique._

**6.6.6 Native name**

**Location:** /name_definition/native_name  
**Property:** native_name (Optional)  
**Type:** String

The native name of this PURL component in the package ecosystem. For instance,
 the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

**6.6.7 Note**

**Location:** /name_definition/note  
**Property:** note (Optional)  
**Type:** String

Extra note text.

**6.7 Version definition**

**Location:** /version_definition  
**Property:** version_definition (Optional)  
**Type:** Object

Definition of the version component for this PURL type. The PURL version 
component is optional for a specific PURL type definition.

Table 6: Properties for the version_definition object

| **Property**         | **Type** | **Requirement** | **Description**                                                                                                                                                                                                                                                                                                |
| -------------------- | -------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| requirement          | Array    | Required        | States that the PURL version is optional.                                                                                                                                                                                                                                                                      |
| permitted_characters | String   | Optional        | A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive       | Boolean  | Optional        | **true** if this PURL component is case sensitive. If **false**, the canonical form shall be lowercased.                                                                                                                                                                                                       |
| normalization_rules  | Array    | Optional        | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.                                                                        |
| native_name          | String   | Optional        | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.                                                                                                                                         |
| note                 | String   | Optional        | Extra note text.                                                                                                                                                                                                                                                                                               |

**6.7.1 Version requirement**

**Location:** /version_definition/requirement  
**Property:** requirement (Required)  
**Type:** String

States that the PURL version is optional.

_Shall be one of:_

- Component optional requirement

**6.7.2 Component optional requirement**

**Type:** String  
**Constant:** optional

States that this PURL component is optional for a PURL type.

**6.7.3 Permitted characters in this PURL component**

**Location:** /version_definition/permitted_characters  
**Property:** permitted_characters (Optional)  
**Type:** String  
**Format:** A regular expression dialect defined by [ECMA-262](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/)

A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) 
dialect) defining the 'Permitted characters' for this component of this 
Package-URL type. If provided, this shall be a subset of the 'Permitted 
characters' defined in the PURL specification.

**6.7.4 Case sensitive**

**Location:** /version_definition/case_sensitive  
**Property:** case_sensitive (Optional)  
**Type:** Boolean  
**Default Value:** **true**

**true** if this PURL component is case sensitive. If **false**, the canonical
 form shall be lowercased.

**6.7.5 Normalization rules**

**Location:** /version_definition/normalization_rules  
**Property:** normalization_rules (Optional)  
**Type:** array (of String)

List of rules to normalize this component for this PURL type. These are plain 
text, unstructured rules as some require programming and cannot be enforced 
only with a schema. Tools are expected to apply these rules programmatically. 
Each item of this array shall be a string.

_All items shall be unique._

**6.7.6 Native name**

**Location:** /version_definition/native_name  
**Property:** native_name (Optional)  
**Type:** String

The native name of this PURL component in the package ecosystem. For instance,
 the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' 
 PURL type.

**6.7.7 Note**

**Location:** /version_definition/note  
**Property:** note (Optional)  
**Type:** String

Extra note text.

**6.8 Qualifiers definition**

**Location:** /qualifiers_definition  
**Property:** qualifiers_definition (Optional)  
**Type:** Array

Definition of the qualifiers specific to this PURL type. The PURL qualifiers 
component is optional for a specific PURL type, but a qualifiers key or keys 
may be required for a specific PURL type. Each item of this array shall be a 
Qualifiers definition object.

**6.8.1 Qualifiers definition**

**Location:** /qualifiers_definition/\[\]  
**Type:** Object

The definition of a qualifier specific to this PURL type.

Table 7: Properties for the qualifiers_definition object

| **Property**  | **Type** | **Requirement** | **Description**                                                           |
| ------------- | -------- | --------------- | ------------------------------------------------------------------------- |
| key           | String   | Required        | The key for the qualifier.                                                |
| requirement   | Array    | Optional        | States that a PURL qualifier key is optional or required for a PURL type. |
| description   | String   | Required        | The description of this qualifier.                                        |
| default_value | String   | Optional        | The optional default value of this qualifier if not provided.             |
| native_name   | String   | Optional        | The equivalent native name for this qualifier key.                        |

**6.8.1.1 Qualifier key**

**Location:** /qualifiers_definition/\[\]/key  
**Type:** String

The key for the qualifier.

**6.8.1.2 Qualifier key requirement**

**Location:** /qualifiers_definition/\[\]/requirement  
**Type:** String

States that a PURL qualifier key is optional or required for a PURL type.

_Shall be one of:_

- Component optional requirement
- Component required requirement

**6.8.1.3 Component optional requirement**

**Type:** String  
**Constant:** optional

States that this PURL component is optional for a PURL type.

**6.8.1.4 Component required requirement**

**Type:** String  
**Constant:** required

States that this PURL component is required for a PURL type.

**6.8.1.5 Description**

**Location:** /qualifiers_definition/\[\]/description  
**Type:** String

The description of this qualifier.

**6.8.1.6 Default value**

**Location:** /qualifiers_definition/\[\]/default_value  
**Type:** String

The optional default value of this qualifier if not provided.

**6.8.1.7 Native name**

**Location:** /qualifiers_definition/\[\]/native_name  
**Type:** String

The equivalent native name for this qualifier key.

_All items shall be unique._

**6.9 Subpath definition**

**Location:** /subpath_definition  
**Property:** subpath_definition (Optional)  
**Type:** Object

The definition for the subpath for this PURL type. The PURL subpath component 
is optional for a specific PURL type definition.

Table 8: Properties for the subpath_definition object

| **Property**         | **Type** | **Requirement** | **Description**                                                                                                                                                                                                                                                                                                |
| -------------------- | -------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| requirement          | Array    | Required        | States that the PURL subpath is optional.                                                                                                                                                                                                                                                                      |
| permitted_characters | String   | Optional        | A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this shall be a subset of the 'Permitted characters' defined in the PURL specification. |
| case_sensitive       | Boolean  | Optional        | **true** if this PURL component is case sensitive. If **false**, the canonical form shall be lowercased.                                                                                                                                                                                                       |
| normalization_rules  | Array    | Optional        | List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.                                                                        |
| native_name          | String   | Optional        | The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.                                                                                                                                         |
| note                 | String   | Optional        | Extra note text.                                                                                                                                                                                                                                                                                               |

**6.9.1 Subpath requirement**

**Location:** /subpath_definition/requirement  
**Property:** requirement (Required)  
**Type:** String

States that the PURL subpath is optional.

_Shall be one of:_

- Component optional requirement

**6.9.2 Component optional requirement**

**Type:** String  
**Constant:** optional

States that this PURL component is optional for a PURL type.

**6.9.3 Permitted characters in this PURL component**

**Location:** /subpath_definition/permitted_characters  
**Property:** permitted_characters (Optional)  
**Type:** String  
**Format:** A regular expression dialect defined by [ECMA-262](https://www.ecma-international.org/publications-and-standards/standards/ecma-262/)

A regular expression ([ECMA-262](https://ecma-international.org/publications-and-standards/standards/ecma-262/) dialect) 
defining the 'Permitted characters' for this component of this Package-URL 
type. If provided, this shall be a subset of the 'Permitted characters' 
defined in the PURL specification.

**6.9.4 Case sensitive**

**Location:** /subpath_definition/case_sensitive  
**Property:** case_sensitive (Optional)  
**Type:** Boolean  
**Default Value:** **true**

**true** if this PURL component is case sensitive. If **false**, the canonical
 form shall be lowercased.

**6.9.5 Normalization rules**

**Location:** /subpath_definition/normalization_rules  
**Property:** normalization_rules (Optional)  
**Type:** array (of String)

List of rules to normalize this component for this PURL type. These are plain 
text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically. Each item of this array shall be a string.

_All items shall be unique._

**6.9.6 Native name**

**Location:** /subpath_definition/native_name  
**Property:** native_name (Optional)  
**Type:** String

The native name of this PURL component in the package ecosystem. For instance,
 the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' 
 PURL type.

**6.9.7 Note**

**Location:** /subpath_definition/note  
**Property:** note (Optional)  
**Type:** String

Extra note text.

**6.10 PURL examples**

**Location:** /examples  
**Property:** examples (Required)  
**Type:** array (of String)  
**Pattern Constraint:** ^pkg:\[a-z\]\[a-z0-9-\\.\]+/.\*\$

Example of valid, canonical PURLs for this package type. Each item of this 
array shall be a string.

_All items shall be unique._

**6.11 Note**

**Location:** /note  
**Property:** note (Optional)  
**Type:** String

Note about this PURL type.

**6.12 Reference URLs**

**Location:** /reference_urls  
**Property:** reference_urls (Optional)  
**Type:** array (of String)  
**Format:** URI as specified in [RFC 3986](https://www.ietf.org/rfc/rfc3986.html)

Optional list of informational reference URLs about this PURL type. Each item 
of this array shall be a string.
