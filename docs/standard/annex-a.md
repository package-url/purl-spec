# A Schemas

This annex provides copies of the current Package-URL schemas. The format
is JSON Schema version draft-07 (https://json-schema.org/draft-07)

## A.1 PURL Type Definition

The schema shown below is available in electronic form at:
https://github.com/package-url/purl-spec/blob/main/schemas/purl-type-definition.schema.json

```
  1 | {
  2 |   "$schema": "http://json-schema.org/draft-07/schema#",
  3 |   "$id": "https://packageurl.org/schemas/purl-type-definition.schema-1.0.json",
  4 |   "title": "Package-URL Type Definition",
  5 |   "description": "Schema to specify a Package-URL (PURL) type as a structured definition.",
  6 |   "type": "object",
  7 |   "additionalProperties": false,
  8 |   "definitions": {
  9 |     "requirement": {
 10 |       "title": "Component requirement",
 11 |       "description": "States if this PURL component is required, optional, or prohibited.",
 12 |       "type": "string",
 13 |       "enum": [
 14 |         "required",
 15 |         "optional",
 16 |         "prohibited"
 17 |       ],
 18 |       "meta:enum": {
 19 |         "required": "This PURL component is required for this PURL type.",
 20 |         "optional": "This PURL component is optional for this PURL type.",
 21 |         "prohibited": "This PURL component is prohibited: it must not be present for this PURL type."
 22 |       }
 23 |     },
 24 |     "purl_component_definition": {
 25 |       "title": "PURL component definition",
 26 |       "description": "PURL component definition properties that apply to most PURL components",
 27 |       "type": "object",
 28 |       "properties": {
 29 |         "permitted_characters": {
 30 |           "title": "Permitted characters in this PURL component",
 31 |           "description": "Regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this component of this Package-URL type. If provided, this must be a subset of the 'Permitted characters' defined in the PURL specification.",
 32 |           "type": "string",
 33 |           "format": "regex"
 34 |         },
 35 |         "case_sensitive": {
 36 |           "title": "Case sensitive",
 37 |           "description": "true if this PURL component is case sensitive. If false, the canonical form must be lowercased.",
 38 |           "type": "boolean",
 39 |           "default": true
 40 |         },
 41 |         "normalization_rules": {
 42 |           "title": "Normalization rules",
 43 |           "description": "List of rules to normalize this component for this PURL type. These are plain text, unstructured rules as some require programming and cannot be enforced only with a schema. Tools are expected to apply these rules programmatically.",
 44 |           "type": "array",
 45 |           "uniqueItems": true,
 46 |           "items": {
 47 |             "type": "string"
 48 |           }
 49 |         },
 50 |         "native_name": {
 51 |           "title": "Native name",
 52 |           "description": "The native name of this PURL component in the package ecosystem. For instance, the 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type.",
 53 |           "type": "string"
 54 |         },
 55 |         "note": {
 56 |           "title": "Note",
 57 |           "description": "Extra note text.",
 58 |           "type": "string"
 59 |         }
 60 |       }
 61 |     }
 62 |   },
 63 |   "required": [
 64 |     "$id",
 65 |     "type",
 66 |     "type_name",
 67 |     "description",
 68 |     "repository",
 69 |     "namespace_definition",
 70 |     "name_definition",
 71 |     "examples"
 72 |   ],
 73 |   "properties": {
 74 |     "$schema": {
 75 |       "title": "JSON schema",
 76 |       "description": "Contains the URL of the JSON schema for Package-URL type definition.",
 77 |       "constant": "https://packageurl.org/schemas/purl-type.schema-1.0.json",
 78 |       "format": "uri"
 79 |     },
 80 |     "$id": {
 81 |       "title": "PURL type definition id",
 82 |       "description": "The unique identifier URI for this PURL type definition.",
 83 |       "type": "string",
 84 |       "pattern": "^https:\\/\\/packageurl\\.org/types/[a-z0-9-]+-definition\\.json$"
 85 |     },
 86 |     "type": {
 87 |       "title": "PURL type",
 88 |       "description": "The type string for this Package-URL type.",
 89 |       "type": "string",
 90 |       "pattern": "^[a-z][a-z0-9-\\.]+$",
 91 |       "examples": [
 92 |         "maven",
 93 |         "npm",
 94 |         "pypi"
 95 |       ]
 96 |     },
 97 |     "type_name": {
 98 |       "title": "Type name",
 99 |       "description": "The name for this PURL type.",
100 |       "type": "string",
101 |       "examples": [
102 |         "Apache Maven",
103 |         "Python Package"
104 |       ]
105 |     },
106 |     "description": {
107 |       "title": "Description",
108 |       "description": "The description of this PURL type.",
109 |       "type": "string"
110 |     },
111 |     "repository": {
112 |       "title": "Repository",
113 |       "description": "Package repository usage for this PURL type.",
114 |       "type": "object",
115 |       "additionalProperties": false,
116 |       "required": [
117 |         "use_repository"
118 |       ],
119 |       "properties": {
120 |         "use_repository": {
121 |           "title": "Use repository",
122 |           "description": "true if this PURL type use a public package repository.",
123 |           "type": "boolean",
124 |           "default": false
125 |         },
126 |         "default_repository_url": {
127 |           "title": "Default repository URL",
128 |           "description": "The default public repository URL for this PURL type",
129 |           "type": "string",
130 |           "format": "uri"
131 |         },
132 |         "note": {
133 |           "title": "Note",
134 |           "description": "Extra note text.",
135 |           "type": "string"
136 |         }
137 |       }
138 |     },
139 |     "namespace_definition": {
140 |       "title": "Namespace definition",
141 |       "description": "Definition of the namespace component for this PURL type.",
142 |       "type": "object",
143 |       "required": [
144 |         "requirement"
145 |       ],
146 |       "properties": {
147 |         "requirement": {
148 |           "$ref": "#/definitions/requirement"
149 |         }
150 |       },
151 |       "allOf": [
152 |         {
153 |           "$ref": "#/definitions/purl_component_definition"
154 |         }
155 |       ]
156 |     },
157 |     "name_definition": {
158 |       "title": "Name definition",
159 |       "description": "Definition of the name component for this PURL type.",
160 |       "type": "object",
161 |       "allOf": [
162 |         {
163 |           "$ref": "#/definitions/purl_component_definition"
164 |         }
165 |       ]
166 |     },
167 |     "version_definition": {
168 |       "title": "Version definition",
169 |       "description": "Definition of the version component for this PURL type.",
170 |       "type": "object",
171 |       "allOf": [
172 |         {
173 |           "$ref": "#/definitions/purl_component_definition"
174 |         }
175 |       ]
176 |     },
177 |     "qualifiers_definition": {
178 |       "title": "Qualifiers definition",
179 |       "description": "Definition for the qualifiers specific to this PURL type.",
180 |       "type": "array",
181 |       "additionalItems": false,
182 |       "uniqueItems": true,
183 |       "items": {
184 |         "title": "Qualifiers definition",
185 |         "description": "Definition of a qualifier specific to this PURL type.",
186 |         "type": "object",
187 |         "additionalProperties": false,
188 |         "required": [
189 |           "key",
190 |           "description"
191 |         ],
192 |         "properties": {
193 |           "key": {
194 |             "title": "Qualifier key",
195 |             "description": "The key for the qualifier.",
196 |             "type": "string"
197 |           },
198 |           "requirement": {
199 |             "$ref": "#/definitions/requirement"
200 |           },
201 |           "description": {
202 |             "title": "Description",
203 |             "description": "The description of this qualifier.",
204 |             "type": "string"
205 |           },
206 |           "default_value": {
207 |             "title": "Default value",
208 |             "description": "The optional default value of this qualifier if not provided.",
209 |             "type": "string"
210 |           },
211 |           "native_name": {
212 |             "title": "Native name",
213 |             "description": "The equivalent native name for this qualifier key.",
214 |             "type": "string"
215 |           }
216 |         }
217 |       }
218 |     },
219 |     "subpath_definition": {
220 |       "title": "Subpath definition",
221 |       "description": "Definition for the subpath for this PURL type.",
222 |       "type": "object",
223 |       "allOf": [
224 |         {
225 |           "$ref": "#/definitions/purl_component_definition"
226 |         }
227 |       ]
228 |     },
229 |     "examples": {
230 |       "title": "PURL examples",
231 |       "description": "Example of valid, canonical PURLs for this package type.",
232 |       "type": "array",
233 |       "uniqueItems": true,
234 |       "minItems": 1,
235 |       "items": {
236 |         "type": "string",
237 |         "pattern": "^pkg:[a-z][a-z0-9-\\.]+/.*$"
238 |       }
239 |     },
240 |     "note": {
241 |       "title": "Note",
242 |       "description": "Note about this PURL type.",
243 |       "type": "string"
244 |     },
245 |     "reference_urls": {
246 |       "title": "Reference URLs",
247 |       "description": "Optional list of informational reference URLs about this PURL type.",
248 |       "type": "array",
249 |       "uniqueItems": true,
250 |       "items": {
251 |         "type": "string",
252 |         "format": "uri"
253 |       }
254 |     }
255 |   }
256 | }
```

## A.2 PURL Types Index

The schema shown below is available in electronic form at:
https://github.com/package-url/purl-spec/blob/main/schemas/purl-types-index.schema.json

```
 1 | {
 2 |   "$schema": "http://json-schema.org/draft-07/schema#",
 3 |   "$id": "https://purl-spec.org/schemas/purl-type-index.schema-1.0.json",
 4 |   "title": "Package-URL types list.",
 5 |   "description": "A list of the registered Package-URL types.",
 6 |   "type": "array",
 7 |   "additionalItems": false,
 8 |   "items": {
 9 |     "type": "string"
10 |   }
11 | }
```

## A.3 PURL Tests

The schema shown below is available in electronic form at:
https://github.com/package-url/purl-spec/blob/main/schemas/purl-test.schema.json

```
  1 | {
  2 |   "$schema": "http://json-schema.org/draft-07/schema#",
  3 |   "$id": "https://packageurl.org/schemas/purl-test.schema-1.0.json",
  4 |   "title": "PURL test definition",
  5 |   "description": "Schema for Package-URL building and parsing tests with input and expected output.",
  6 |   "type": "object",
  7 |   "additionalProperties": false,
  8 |   "definitions": {
  9 |     "purl_components": {
 10 |       "title": "PURL decoded components",
 11 |       "description": "Individual decoded PURL components to use as a test input or expected output.",
 12 |       "type": "object",
 13 |       "additionalProperties": false,
 14 |       "properties": {
 15 |         "type": {
 16 |           "title": "PURL type",
 17 |           "description": "Package-URL type component.",
 18 |           "default": null,
 19 |           "type": [
 20 |             "string",
 21 |             "null"
 22 |           ]
 23 |         },
 24 |         "namespace": {
 25 |           "title": "PURL namespace",
 26 |           "description": "Package-URL namespace decoded component.",
 27 |           "default": null,
 28 |           "type": [
 29 |             "string",
 30 |             "null"
 31 |           ]
 32 |         },
 33 |         "name": {
 34 |           "title": "PURL name",
 35 |           "description": "Package-URL name decoded component.",
 36 |           "default": null,
 37 |           "type": [
 38 |             "string",
 39 |             "null"
 40 |           ]
 41 |         },
 42 |         "version": {
 43 |           "title": "PURL version",
 44 |           "description": "Package-URL version decoded component.",
 45 |           "default": null,
 46 |           "type": [
 47 |             "string",
 48 |             "null"
 49 |           ]
 50 |         },
 51 |         "qualifiers": {
 52 |           "title": "PURL qualifiers",
 53 |           "description": "Package-URL qualifiers decoded component as an object.",
 54 |           "default": null,
 55 |           "type": [
 56 |             "object",
 57 |             "null"
 58 |           ]
 59 |         },
 60 |         "subpath": {
 61 |           "title": "PURL subpath",
 62 |           "description": "Package-URL subpath decoded component.",
 63 |           "default": null,
 64 |           "type": [
 65 |             "string",
 66 |             "null"
 67 |           ]
 68 |         }
 69 |       }
 70 |     },
 71 |     "purl_test": {
 72 |       "title": "PURL test",
 73 |       "description": "A PURL test with input and expected output.",
 74 |       "type": "object",
 75 |       "required": [
 76 |         "description",
 77 |         "test_group",
 78 |         "test_type",
 79 |         "input"
 80 |       ],
 81 |       "properties": {
 82 |         "description": {
 83 |           "title": "Test description",
 84 |           "description": "A description for this test.",
 85 |           "type": "string"
 86 |         },
 87 |         "test_group": {
 88 |           "title": "Test group",
 89 |           "description": "The group of this test like 'base' or 'advanced'.",
 90 |           "type": "string",
 91 |           "enum": [
 92 |             "base",
 93 |             "advanced"
 94 |           ],
 95 |           "meta:enum": {
 96 |             "base": "Test group for base conformance tests for PURL building and parsing.",
 97 |             "advanced": "Test group for advanced tests to support flexible PURL building and parsing."
 98 |           }
 99 |         },
100 |         "test_type": {
101 |           "title": "Test type",
102 |           "description": "The type of this test like 'build' or 'parse'.",
103 |           "type": "string",
104 |           "enum": [
105 |             "build",
106 |             "parse",
107 |             "roundtrip"
108 |           ],
109 |           "meta:enum": {
110 |             "build": "A PURL building test from decoded components to a canonical PURL string.",
111 |             "parse": "A PURL building test from decoded components to a canonical PURL string.",
112 |             "roundtrip": "A PURL routrip test, parsing then building back a PURL from a canonical string input."
113 |           }
114 |         },
115 |         "expected_failure": {
116 |           "title": "Expected failure",
117 |           "description": "true if this test input is expected to fail to be processed.",
118 |           "type": "boolean",
119 |           "default": false
120 |         },
121 |         "expected_failure_reason": {
122 |           "title": "Expected failure reason",
123 |           "description": "The reason why this test is is expected to fail if expected_failure is true.",
124 |           "default": null,
125 |           "type": [
126 |             "string",
127 |             "null"
128 |           ]
129 |         }
130 |       },
131 |       "allOf": [
132 |         {
133 |           "if": {
134 |             "properties": {
135 |               "test_type": {
136 |                 "const": "parse"
137 |               },
138 |               "expected_failure": {
139 |                 "const": false
140 |               }
141 |             },
142 |             "required": [
143 |               "test_type",
144 |               "expected_failure"
145 |             ]
146 |           },
147 |           "then": {
148 |             "properties": {
149 |               "input": {
150 |                 "title": "Input test PURL",
151 |                 "description": "A PURL string to use as a test input (canonical or not).",
152 |                 "type": "string"
153 |               },
154 |               "expected_output": {
155 |                 "title": "Expected output decoded PURL components",
156 |                 "description": "Test output as an object decoded PURL components, unless expected_failure.",
157 |                 "$ref": "#/definitions/purl_components"
158 |               }
159 |             },
160 |             "required": [
161 |               "input",
162 |               "expected_output"
163 |             ]
164 |           }
165 |         },
166 |         {
167 |           "if": {
168 |             "properties": {
169 |               "test_type": {
170 |                 "const": "build"
171 |               },
172 |               "expected_failure": {
173 |                 "const": false
174 |               }
175 |             },
176 |             "required": [
177 |               "test_type",
178 |               "expected_failure"
179 |             ]
180 |           },
181 |           "then": {
182 |             "properties": {
183 |               "input": {
184 |                 "title": "Expected output decoded PURL components",
185 |                 "description": "Test output as an object decoded PURL components, unless expected_failure.",
186 |                 "$ref": "#/definitions/purl_components"
187 |               },
188 |               "expected_output": {
189 |                 "title": "Expected canonical PURL",
190 |                 "description": "A canonical PURL string to use as a test ouput.",
191 |                 "type": "string"
192 |               }
193 |             },
194 |             "required": [
195 |               "input",
196 |               "expected_output"
197 |             ]
198 |           }
199 |         },
200 |         {
201 |           "if": {
202 |             "properties": {
203 |               "test_type": {
204 |                 "const": "roundtrip"
205 |               }
206 |             },
207 |             "required": [
208 |               "test_type"
209 |             ]
210 |           },
211 |           "then": {
212 |             "properties": {
213 |               "input": {
214 |                 "title": "Input test PURL",
215 |                 "description": "A PURL string to use as a test input (canonical or not).",
216 |                 "type": "string"
217 |               },
218 |               "expected_output": {
219 |                 "title": "Expected canonical PURL",
220 |                 "description": "A canonical PURL string to use as a test ouput.",
221 |                 "type": "string"
222 |               }
223 |             },
224 |             "required": [
225 |               "input",
226 |               "expected_output"
227 |             ]
228 |           }
229 |         },
230 |         {
231 |           "if": {
232 |             "properties": {
233 |               "test_type": {
234 |                 "const": "parse"
235 |               },
236 |               "expected_failure": {
237 |                 "const": true
238 |               }
239 |             },
240 |             "required": [
241 |               "test_type",
242 |               "expected_failure"
243 |             ]
244 |           },
245 |           "then": {
246 |             "properties": {
247 |               "input": {
248 |                 "title": "Input test PURL",
249 |                 "description": "A PURL string to use as a test input (canonical or not).",
250 |                 "type": "string"
251 |               }
252 |             },
253 |             "required": [
254 |               "input",
255 |               "expected_failure_reason"
256 |             ]
257 |           }
258 |         },
259 |         {
260 |           "if": {
261 |             "properties": {
262 |               "test_type": {
263 |                 "const": "build"
264 |               },
265 |               "expected_failure": {
266 |                 "const": true
267 |               }
268 |             },
269 |             "required": [
270 |               "test_type",
271 |               "expected_failure"
272 |             ]
273 |           },
274 |           "then": {
275 |             "properties": {
276 |               "input": {
277 |                 "title": "Expected output decoded PURL components",
278 |                 "description": "Test output as an object decoded PURL components, unless expected_failure.",
279 |                 "$ref": "#/definitions/purl_components"
280 |               }
281 |             },
282 |             "required": [
283 |               "input",
284 |               "expected_failure_reason"
285 |             ]
286 |           }
287 |         }
288 |       ]
289 |     }
290 |   },
291 |   "properties": {
292 |     "$schema": {
293 |       "title": "JSON schema",
294 |       "description": "Contains the URL of the JSON schema for Package-URL tests.",
295 |       "constant": "https://packageurl.org/schemas/purl-test.schema-1.0.json",
296 |       "format": "uri"
297 |     },
298 |     "tests": {
299 |       "title": "Test suite",
300 |       "description": "A list of Package-URL build and parse tests.",
301 |       "additionalItems": false,
302 |       "type": "array",
303 |       "minItems": 1,
304 |       "uniqueItems": true,
305 |       "items": {
306 |         "$ref": "#/definitions/purl_test"
307 |       }
308 |     }
309 |   }
310 | }
```
