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
from typing import Any, Literal, Optional
from pydantic import BaseModel, ConfigDict, Field


class PackageUrlTestDefinition(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    field_schema: Optional[Any] = Field(
        None,
        alias="$schema",
        description="Contains the URL of the JSON schema for Package-URL tests.",
        title="JSON schema",
    )
    tests: Optional[list[PurlTest]] = Field(
        None,
        description="A list of Package-URL build and parse tests.",
        min_length=1,
        title="Test suite",
    )


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


class PurlTest(BaseModel):
    description: str = Field(
        ..., description="A description for this test.", title="Test description"
    )
    test_group: Literal["base", "advanced"] = Field(
        ..., description="The group of this test like 'base' or 'advanced'.", title="Test group"
    )
    test_type: Literal["build", "parse", "roundtrip"] = Field(
        ..., description="The type of this test like 'build' or 'parse'.", title="Test type"
    )
    expected_failure: Optional[bool] = Field(
        False,
        description="true if this test input is expected to fail to be processed.",
        title="Expected failure",
    )
    expected_failure_reason: Optional[str] = Field(
        None,
        description="The reason why this test is expected to fail if expected_failure is true.",
        title="Expected failure reason",
    )
