# SPDX-License-Identifier: MIT
# Copyright (c) the purl authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Visit https://github.com/package-url/purl-spec and https://packageurl.org for support


from __future__ import annotations

from typing import Any
from typing import Literal
from typing import Optional

from pydantic import AnyUrl
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import RootModel


class Example(RootModel[str]):
    root: str = Field(..., pattern="^pkg:[a-z][a-z0-9-\\.]+/.*$")


class PackageUrlTypeDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_schema: Optional[Any] = Field(
        None,
        alias="$schema",
        description="Contains the URL of the JSON schema for Package-URL type definition.",
        title="JSON schema",
    )
    field_id: str = Field(
        ...,
        alias="$id",
        description="The unique identifier URI for this PURL type definition.",
        pattern="^https:\\/\\/packageurl\\.org/types/[a-z0-9-]+-definition\\.json$",
        title="PURL type definition id",
    )
    type: str = Field(
        ...,
        description="The type string for this Package-URL type.",
        examples=["maven", "npm", "pypi"],
        pattern="^[a-z][a-z0-9-\\.]+$",
        title="PURL type",
    )
    type_name: str = Field(
        ...,
        description="The name for this PURL type.",
        examples=["Apache Maven", "Python Package"],
        title="Type name",
    )
    description: str = Field(
        ..., description="The description of this PURL type.", title="Description"
    )
    repository: Repository = Field(
        ..., description="Package repository usage for this PURL type.", title="Repository"
    )
    namespace_definition: NamespaceDefinition = Field(
        ...,
        description="Definition of the namespace component for this PURL type.",
        title="Namespace definition",
    )
    name_definition: PurlComponentDefinition = Field(
        ...,
        description="Definition of the name component for this PURL type.",
        title="Name definition",
    )
    version_definition: Optional[PurlComponentDefinition] = Field(
        None,
        description="Definition of the version component for this PURL type.",
        title="Version definition",
    )
    qualifiers_definition: Optional[list[QualifiersDefinitionItem]] = Field(
        None,
        description="Definition for the qualifiers specific to this PURL type.",
        title="Qualifiers definition",
    )
    subpath_definition: Optional[PurlComponentDefinition] = Field(
        None,
        description="Definition for the subpath for this PURL type.",
        title="Subpath definition",
    )
    examples: list[Example] = Field(
        ...,
        description="Example of valid, canonical PURLs for this package type.",
        min_length=1,
        title="PURL examples",
    )
    note: Optional[str] = Field(None, description="Note about this PURL type.", title="Note")
    reference_urls: Optional[list[AnyUrl]] = Field(
        None,
        description="Optional list of informational reference URLs about this PURL type.",
        title="Reference URLs",
    )


class PurlComponentDefinition(BaseModel):
    permitted_characters: Optional[str] = Field(
        None,
        description=(
            "Regular expression (ECMA-262 dialect) defining the 'Permitted characters' for this"
            " component of this Package-URL type. If provided, this must be a subset of the"
            " 'Permitted characters' defined in the PURL specification."
        ),
        title="Permitted characters in this PURL component",
    )
    case_sensitive: Optional[bool] = Field(
        True,
        description=(
            "true if this PURL component is case sensitive. If false, the canonical form must be"
            " lowercased."
        ),
        title="Case sensitive",
    )
    normalization_rules: Optional[list[str]] = Field(
        None,
        description=(
            "List of rules to normalize this component for this PURL type. These are plain text,"
            " unstructured rules as some require programming and cannot be enforced only with a"
            " schema. Tools are expected to apply these rules programmatically."
        ),
        title="Normalization rules",
    )
    native_name: Optional[str] = Field(
        None,
        description=(
            "The native name of this PURL component in the package ecosystem. For instance, the"
            " 'namespace' for the 'maven' type is 'groupId', and 'scope' for the 'npm' PURL type."
        ),
        title="Native name",
    )
    note: Optional[str] = Field(None, description="Extra note text.", title="Note")


class QualifiersDefinitionItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    key: str = Field(..., description="The key for the qualifier.", title="Qualifier key")
    requirement: Optional[Requirement] = None
    description: str = Field(
        ..., description="The description of this qualifier.", title="Description"
    )
    default_value: Optional[str] = Field(
        None,
        description="The optional default value of this qualifier if not provided.",
        title="Default value",
    )
    native_name: Optional[str] = Field(
        None, description="The equivalent native name for this qualifier key.", title="Native name"
    )


class Repository(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    use_repository: bool = Field(
        ...,
        description="true if this PURL type use a public package repository.",
        title="Use repository",
    )
    default_repository_url: Optional[AnyUrl] = Field(
        None,
        description="The default public repository URL for this PURL type",
        title="Default repository URL",
    )
    note: Optional[str] = Field(None, description="Extra note text.", title="Note")


class Requirement(RootModel[Literal["required", "optional", "prohibited"]]):
    root: Literal["required", "optional", "prohibited"] = Field(
        ...,
        description="States if this PURL component is required, optional, or prohibited.",
        title="Component requirement",
    )


class NamespaceDefinition(PurlComponentDefinition):
    requirement: Requirement
