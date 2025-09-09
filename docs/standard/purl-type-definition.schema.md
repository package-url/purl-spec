
# Package-URL Type Definition Schema
Each package manager, platform, type, or ecosystem has its own conventions and
protocols to identify, locate, and provision software packages. The package 
**type** is the component of a Package-URL that is used to capture
this information with a short string such as debian, gem, maven, npm, nuget, 
gem or pypi.

The PURL Type Definition JSON Schema is the reference implementation for the 
Ecma standard. See Annex A for a copy of the purl-type-definition.schema.json
 file content.

## PURL type definition data
The Package-URL standard includes the schema for defining a purl type, but
it does not include the purl type definitions themselves. The purl type 
definitions are registered with a community approval process and stored in 
the package-url/purl-spec repository at the following locations:

- The JSON Index listing of all defined PURL types at:
  https://github.com/package-url/purl-spec/tree/main/purl-types-index.json
- A separate JSON files for each PURL type definition at:
  https://github.com/package-url/purl-spec/tree/main/types
- A generated Markdown documentation for each PURL type JSON definition at:
  https://github.com/package-url/purl-spec/tree/main/types-doc


**Type:** Object<br>
**Description:** Schema to specify a Package-URL (PURL) type as a structured definition.

| Property                                           | Type            | Title/Description       |
| -------------------------------------------------- | --------------- | ----------------------- |
| - [$schema](#schema )                              | object          | JSON schema             |
| + [$id](#id )                                      | string          | PURL type definition id |
| + [type](#type )                                   | string          | PURL type               |
| + [type_name](#type_name )                         | string          | Type name               |
| + [description](#description )                     | string          | Description             |
| + [repository](#repository )                       | object          | Repository              |
| + [namespace_definition](#namespace_definition )   | object          | Namespace definition    |
| + [name_definition](#name_definition )             | object          | Name definition         |
| - [version_definition](#version_definition )       | object          | Version definition      |
| - [qualifiers_definition](#qualifiers_definition ) | array of object | Qualifiers definition   |
| - [subpath_definition](#subpath_definition )       | object          | Subpath definition      |
| + [examples](#examples )                           | array of string | PURL examples           |
| - [note](#note )                                   | string          | Note                    |
| - [reference_urls](#reference_urls )               | array of string | Reference URLs          |

## 1 JSON schema
### Property: Package-URL Type Definition > $schema

**Type:** Object<br>
**Description:** Contains the URL of the JSON schema for Package-URL type definition.

## 2 PURL type definition id
### Property: Package-URL Type Definition > $id

**Type:** String <br>
**Required:** Yes <br>
**Description:** The unique identifier URI for this PURL type definition.

| Restrictions                       |                              | 
| ---------------------------------- | ---------------------------- |
| **Must match regular expression:** | ^pkg:[a-z][a-z0-9-\.]+/.*$   |    

## 3 PURL type
### Property: Package-URL Type Definition > type

**Type:** String <br>
**Required:** Yes <br>
**Description:** The type string for this Package-URL type.

**Examples:**
- "maven"
- "npm"
- "pypi"

| Restrictions                       |                              | 
| ---------------------------------- | ---------------------------- |
| **Must match regular expression:** | ^pkg:[a-z][a-z0-9-\.]+/.*$   |    

## 4 Type name
### Property: Package-URL Type Definition > type_name

**Type:** String <br>
**Required:** Yes <br>
**Description:** The name for this PURL type.

**Examples:**
- "Apache Maven"
- "Python Package"

## 5 Description
### Property: Package-URL Type Definition > description

**Type:** String <br>
**Required:** Yes <br>
**Description:** The description of this PURL type.

## 6 Repository
### Property: Package-URL Type Definition > repository

**Type:** Object <br>
**Required:** Yes <br>
**Additional properties:** Not allowed <br>
**Description:** Package repository usage for this PURL type.

| Property                                                        | Type    | Title/Description      |
| --------------------------------------------------------------- | ------- | ---------------------- |
| + [use_repository](#repository_use_repository )                 | boolean | Use repository         |
| - [default_repository_url](#repository_default_repository_url ) | string  | Default repository URL |
| - [note](#repository_note )                                     | string  | Note                   |

### 6.1 Repository Use repository
#### Property: Package-URL Type Definition > repository > use_repository

**Type:** Boolean <br>
**Required:** Yes <br>
**Default:** false <br>
**Description:** true if this PURL type use a public package repository.

### 6.2 Default repository URL
#### Property: Package-URL Type Definition > repository > default_repository_url

**Type:** String <br>
**Required:** No <br>
**Format:** URI <br>
**Description:** The default public repository URL for this PURL type

### 6.3 Note
#### Property: Package-URL Type Definition > repository > note

**Type:** String <br>
**Required:** No <br>
**Description:** Extra note text.

## 7 Namespace definition
### Property: Package-URL Type Definition > namespace_definition

**Type:** Object <br>
**Required:** Yes <br>
**Additional properties:** Any type allowed <br>
**Description:** Definition of the namespace component for this PURL type.

| Property                                                              | Type             | Title/Description                           |
| --------------------------------------------------------------------- | ---------------- | ------------------------------------------- |
| - [permitted_characters](#namespace_definition_permitted_characters ) | string           | Permitted characters in this PURL component |
| - [case_sensitive](#namespace_definition_case_sensitive )             | boolean          | Case sensitive                              |
| - [normalization_rules](#namespace_definition_normalization_rules )   | array of string  | Normalization rules                         |
| - [native_name](#namespace_definition_native_name )                   | string           | Native name                                 |
| - [note](#namespace_definition_note )                                 | string           | Note                                        |
| + [requirement](#namespace_definition_requirement )                   | enum (of string) | Component requirement                       |

### 7.1 Permitted characters in this PURL component
#### Property: Package-URL Type Definition > namespace_definition > permitted_characters

**Type:** String <br>
**Required:** No <br>
**Format:** regex <br>
**Description:** Regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this must be a subset of the 'Permitted characters' defined in the PURL specification.

### 7.2 Case sensitive
#### Property: Package-URL Type Definition > namespace_definition > case_sensitive

**Type:** Boolean <br>
**Required:** No <br>
**Default:** true <br>
**Description:** true if this PURL component is case sensitive. If false, the canonical form must be lowercased.

### 7.3 Normalization rules
#### Property: Package-URL Type Definition > namespace_definition > normalization_rules

**Type:** Array of string <br>
**Required:** No <br>
**Description:** List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

**Each item of this array must be:** normalization_rules items

#### Property: Package-URL Type Definition > namespace_definition > normalization_rules > normalization_rules items

**Type:** String <br>
**Required:** No <br>

### 7.4 Native name
#### Property: Package-URL Type Definition > namespace_definition > native_name

**Type:** String <br>
**Required:** No <br>
**Description:** The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

### 7.5 Note
#### Property: Package-URL Type Definition > namespace_definition > note

**Type:** String <br>
**Required:** No <br>
**Description:** Extra note text.

### 7.6 Component requirement
#### Property: Package-URL Type Definition > namespace_definition > requirement

**Type:** Enum (of string) <br>
**Required:** No <br>
**Description:** States if this PURL component is required, optional, or prohibited.

**Must be one of:**
* "required"
* "optional"
* "prohibited"

## 8 Name definition
### Property: Package-URL Type Definition > name_definition

**Type:** Object <br>
**Required:** Yes <br>
**Additional properties:** Any type allowed <br>
**Description:** Definition of the name component for this PURL type.

| Property                                                         | Type            | Title/Description                           |
| ---------------------------------------------------------------- | --------------  | ------------------------------------------- |
| - [permitted_characters](#name_definition_permitted_characters ) | string          | Permitted characters in this PURL component |
| - [case_sensitive](#name_definition_case_sensitive )             | boolean         | Case sensitive                              |
| - [normalization_rules](#name_definition_normalization_rules )   | array of string | Normalization rules                         |
| - [native_name](#name_definition_native_name )                   | string          | Native name                                 |
| - [note](#name_definition_note )                                 | string          | Note                                        |

### 8.1 Permitted characters in this PURL component
#### Properties: Package-URL Type Definition > name_definition > permitted_characters

**Type:** String <br>
**Required:** No <br>
**Format:** regex <br>
**Description:** Regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this must be a subset of the 'Permitted characters' defined in the PURL specification.

### 8.2 Case sensitive
#### Properties: Package-URL Type Definition > name_definition > case_sensitive

**Type:** Boolean <br>
**Required:** No <br>
**Default:** true <br>
**Description:** true if this PURL component is case sensitive. If false, the canonical form must be lowercased.

### 8.3 Normalization rules
#### Property: Package-URL Type Definition > name_definition > normalization_rules

**Type:** Array of string <br>
**Required:** No <br>
**Description:** List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

##### Property: Package-URL Type Definition > name_definition > normalization_rules > normalization_rules items

**Each item of this array must be:** normalization_rules items
 
**Type:** String <br>
**Required:** No <br>

### 8.4 Native name
#### Property: Package-URL Type Definition > name_definition > native_name

**Type:** String <br>
**Required:** No <br>
**Description:** The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

### 8.5 Note
#### Property: Package-URL Type Definition > name_definition > note

**Type:** String <br>
**Required:** No <br>
**Description:** Extra note text.

## 9 Version definition
###  Property: Package-URL Type Definition > version_definition

**Type:** Object <br>
**Required:** No <br>
**Additional properties:** Any type allowed <br>
**Description:** Definition of the version component for this PURL type.

| Property                                                         | Type            | Title/Description                           |
| ---------------------------------------------------------------- | --------------  | ------------------------------------------- |
| - [permitted_characters](#name_definition_permitted_characters ) | string          | Permitted characters in this PURL component |
| - [case_sensitive](#name_definition_case_sensitive )             | boolean         | Case sensitive                              |
| - [normalization_rules](#name_definition_normalization_rules )   | array of string | Normalization rules                         |
| - [native_name](#name_definition_native_name )                   | string          | Native name                                 |
| - [note](#name_definition_note )                                 | string          | Note                                        |

### 9.1 Permitted characters in this PURL component
#### Property: Package-URL Type Definition > version_definition > permitted_characters

**Type:** String <br>
**Required:** No <br>
**Format:** regex <br>
**Description:** Regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this must be a subset of the 'Permitted characters' defined in the PURL specification.

### 9.2  Case sensitive
#### Property: Package-URL Type Definition > version_definition > case_sensitive

**Type:** Boolean <br>
**Required:** No <br>
**Default:** true <br>
**Description:** true if this PURL component is case sensitive. If false, the canonical form must be lowercased.

### 9.3 Normalization rules
#### Property: Package-URL Type Definition > version_definition > normalization_rules

**Type:** Array of string <br>
**Required:** No <br>
**Description:** List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

**Each item of this array must be:** normalization_rules items

#### Property: Package-URL Type Definition > version_definition > normalization_rules > normalization_rules items
 
**Type:** String <br>
**Required:** No <br>

### 9.4  Native name
####  Property: Package-URL Type Definition > version_definition > native_name

**Type:** String <br>
**Required:** No <br>
**Description:** The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

### 9.5  Note
#### Property: Package-URL Type Definition > version_definition > note

**Type:** String <br>
**Required:** No <br>
**Description:** Extra note text.

## 10 Qualifiers definition
### Property: Package-URL Type Definition > qualifiers_definition

**Type:** Array of object <br>
**Required:** No <br>
**Description:** Definition for the qualifiers specific to this PURL type.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                       | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- |
| Qualifiers definition                                 | Definition of a qualifier specific to this PURL type. |

### 10.1 Qualifiers definition
#### Property: Package-URL Type Definition > qualifiers_definition > Qualifiers definition

**Type:** Object <br>
**Required:** No <br>
**Additional properties:** Not allowed <br>
**Description:** Definition of a qualifier specific to this PURL type.

| Property                                                       | Type             | Title/Description     |
| -------------------------------------------------------------- | ---------------- | --------------------- |
| + [key](#qualifiers_definition_items_key )                     | string           | Qualifier key         |
| - [requirement](#qualifiers_definition_items_requirement )     | enum (of string) | Component requirement |
| + [description](#qualifiers_definition_items_description )     | string           | Description           |
| - [default_value](#qualifiers_definition_items_default_value ) | string           | Default value         |
| - [native_name](#qualifiers_definition_items_native_name )     | string           | Native name           |

### 10.2 Qualifier key
#### Property: Package-URL Type Definition > qualifiers_definition > Qualifiers definition > key

**Type:** String <br>
**Required:** Yes <br>
**Description:** The key for the qualifier.

### 10.3 Component requirement
#### Property: Package-URL Type Definition > qualifiers_definition > Qualifiers definition > requirement

**Type:** Enum (of string) <br>
**Required:** No <br>
**Description:** States if this PURL component is required, optional, or prohibited.

**Must be one of:**
* "required"
* "optional"
* "prohibited"

### 10.4 Description
#### Property: Package-URL Type Definition > qualifiers_definition > Qualifiers definition > description

**Type:** String <br>
**Required:** Yes <br>
**Description:** The description of this qualifier.

### 10.5 Default value
#### Property: Package-URL Type Definition > qualifiers_definition > Qualifiers definition > default_value

**Type:** String <br>
**Required:** No <br>
**Description:** The optional default value of this qualifier if not provided.

### 10.6 Native name
#### Property: Package-URL Type Definition > qualifiers_definition > Qualifiers definition > native_name

**Type:** String <br>
**Required:** No <br>
**Description:** The equivalent native name for this qualifier key.

## 11 Subpath definition
### Property: Package-URL Type Definition > subpath_definition

**Type:** Object <br>
**Required:** No <br>
**Additional properties:** Any type allowed <br>
**Description:** Definition for the subpath for this PURL type.

| Property                                                         | Type            | Title/Description                           |
| ---------------------------------------------------------------- | --------------  | ------------------------------------------- |
| - [permitted_characters](#name_definition_permitted_characters ) | string          | Permitted characters in this PURL component |
| - [case_sensitive](#name_definition_case_sensitive )             | boolean         | Case sensitive                              |
| - [normalization_rules](#name_definition_normalization_rules )   | array of string | Normalization rules                         |
| - [native_name](#name_definition_native_name )                   | string          | Native name                                 |
| - [note](#name_definition_note )                                 | string          | Note                                        |

### 11.1 Permitted characters in this PURL component
#### Property: Package-URL Type Definition > subpath_definition > permitted_characters

**Type:** String <br>
**Required:** No <br>
**Format:** regex <br>
**Description:** Regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this must be a subset of the 'Permitted characters' defined in the PURL specification.

### 11.2 Case sensitive
#### Property: Package-URL Type Definition > subpath_definition > case_sensitive

**Type:** Boolean <br>
**Required:** No <br>
**Default:** true <br>
**Description:** true if this PURL component is case sensitive. If false, the canonical form must be lowercased.

### 11.3 Normalization rules
#### Property: Package-URL Type Definition > subpath_definition > normalization_rules

**Type:** Array of string <br>
**Required:** No <br>
**Description:** List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

**Each item of this array must be:** normalization_rules items

#### Property: Package-URL Type Definition > subpath_definition > normalization_rules > normalization_rules items

**Type:** String <br>
**Required:** No <br>

### 11.4 Native name
#### Property: Package-URL Type Definition > subpath_definition > native_name

**Type:** String <br>
**Required:** No <br>
**Description:** The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.

### 11.5 Note
#### Property: Package-URL Type Definition > subpath_definition > note

**Type:** String <br>
**Required:** No <br>
|**Description:** Extra note text.

## 12 PURL examples
### Property: Package-URL Type Definition > examples

**Type:** Array of string <br>
**Required:** Yes <br>
**Description:** Example of valid, canonical PURLs for this package type.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | 1                  |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

###  Property: Package-URL Type Definition > examples > examples items

**Each item of this array must be:** examples_items

**Type:** String <br>
**Required:** No <br>

| Restrictions                      |                               |
| --------------------------------- | ------------------------------|
| **Must match regular expression:** | ^pkg:[a-z][a-z0-9-\.]+/.*$   |          

## 13 Note
### Property: Package-URL Type Definition > note

**Type:** String <br>
**Required:** No <br>
**Description:** Note about this PURL type.

## 14 Reference URLs
### Property: Package-URL Type Definition > reference_urls

**Type:** Array of string <br>
**Required:** No <br>
**Description:** Optional list of informational reference URLs about this PURL type.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

**Each item of this array must be:** reference_urls items

### Property: Package-URL Type Definition > reference_urls > reference_urls items

**Type:** String <br>
**Required:** No <br>
|**Format:** URI
