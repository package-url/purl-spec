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
from typing import Any, Literal, Optional, Union
from pydantic import BaseModel, ConfigDict, Field, RootModel


class BuildTest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Description
    test_group: TestGroup
    test_type: Literal["build"]
    input: PurlComponents = Field(
        ...,
        description="An object of decoded PURL components to use as a test input.",
        title="Input test PURL components",
    )
    expected_output: Optional[str] = Field(
        None,
        description="Test output as a canonical PURL string, unless expected_failure.",
        title="Expected output canonical PURL string",
    )
    expected_failure: Optional[ExpectedFailure] = False
    expected_failure_reason: Optional[ExpectedFailureReason] = None


class Description(RootModel[str]):
    root: str = Field(
        ..., description="An optional description for this test.", title="Test description"
    )


class ExpectedFailure(RootModel[bool]):
    root: bool = Field(
        ...,
        description="true if this test input is expected to fail to be processed.",
        title="Expected failure",
    )


class ExpectedFailureReason(RootModel[str]):
    root: str = Field(
        ...,
        description="The reason why this is is expected to fail if expected_failure is true.",
        title="Expected failure reason",
    )


class ParseTest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Description
    test_group: TestGroup
    test_type: Literal["parse"]
    input: str = Field(
        ...,
        description="A PURL string to use as a test input (canonical or not).",
        title="Input test PURL",
    )
    expected_output: Optional[PurlComponents] = Field(
        None,
        description="Test output as an object decoded PURL components, unless expected_failure.",
        title="Expected output decoded PURL components",
    )
    expected_failure: Optional[ExpectedFailure] = False
    expected_failure_reason: Optional[ExpectedFailureReason] = None


class PurlComponents(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Optional[str] = Field(None, description="Package-URL type component.", title="PURL type")
    namespace: Optional[str] = Field(
        None, description="Package-URL namespace decoded component.", title="PURL namespace"
    )
    name: Optional[str] = Field(
        None, description="Package-URL name decoded component.", title="PURL name"
    )
    version: Optional[str] = Field(
        None, description="Package-URL version decoded component.", title="PURL version"
    )
    qualifiers: Optional[dict[str, Any]] = Field(
        None,
        description="Package-URL qualifiers decoded component as an object.",
        title="PURL qualifiers",
    )
    subpath: Optional[str] = Field(
        None, description="Package-URL subpath decoded component.", title="PURL subpath"
    )


class PurlTestDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_schema: Optional[Any] = Field(
        None,
        alias="$schema",
        description="Contains the URL of the JSON schema for Package-URL tests.",
        title="JSON schema",
    )
    tests: Optional[list[Union[BuildTest, ParseTest]]] = Field(
        None,
        description="A list of Package-URL build and parse tests.",
        min_length=1,
        title="Test suite",
    )


class TestGroup(RootModel[Literal["base", "advanced"]]):
    root: Literal["base", "advanced"] = Field(
        ..., description="The group of this test like 'base' or 'advanced'.", title="Test group"
    )
