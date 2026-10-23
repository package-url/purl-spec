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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, Literal


class PackageUrlTestDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_schema: Any | None = Field(
        None,
        alias="$schema",
        description="Contains the URL of the JSON schema for Package-URL tests.",
        title="JSON schema",
    )
    tests: list[PurlTest] | None = Field(
        None,
        description="A list of Package-URL build and parse tests.",
        min_length=1,
        title="Test suite",
    )


class PurlComponents(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: str | None = Field(None, description="Package-URL type component.", title="PURL type")
    namespace: str | None = Field(
        None, description="Package-URL namespace decoded component.", title="PURL namespace"
    )
    name: str | None = Field(
        None, description="Package-URL name decoded component.", title="PURL name"
    )
    version: str | None = Field(
        None, description="Package-URL version decoded component.", title="PURL version"
    )
    qualifiers: dict[str, Any] | None = Field(
        None,
        description="Package-URL qualifiers decoded component as an object.",
        title="PURL qualifiers",
    )
    subpath: str | None = Field(
        None, description="Package-URL subpath decoded component.", title="PURL subpath"
    )


class PurlTest(BaseModel):
    description: str = Field(
        ..., description="A description for this test.", title="Test description"
    )
    test_group: Literal["required", "recommended"] = Field(
        ..., description="The conformance group of this test case.", title="Test group"
    )
    test_type: Literal["build", "parse", "validate"] = Field(
        ..., description="The functional type of this test case.", title="Test type"
    )
    expected_failure: bool | None = Field(
        False,
        description="true if this test input is expected to fail to be processed.",
        title="Expected failure",
    )
    expected_message: str | None = Field(
        None,
        description="The reason why a test failed or another message about the test result.",
        title="Expected test message",
    )
    input: Any
