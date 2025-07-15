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

from dataclasses import dataclass
from typing import Any
from typing import Literal
from typing import Optional
from typing import Union


@dataclass
class PurlComponents:
    type: Optional[str] = None
    namespace: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    qualifiers: Optional[dict[str, Any]] = None
    subpath: Optional[str] = None


Description = str

TestGroup = Literal["base", "advanced"]

ExpectedFailure = bool

ExpectedFailureReason = str


@dataclass
class ParseTest:
    description: Description
    test_group: TestGroup
    test_type: str = "parse"
    input: str = None
    expected_output: Optional[PurlComponents] = None
    expected_failure: Optional[ExpectedFailure] = False
    expected_failure_reason: Optional[ExpectedFailureReason] = None


@dataclass
class RoundtripTest:
    description: Description
    test_group: TestGroup
    test_type: str = "roundtrip"
    input: str = None
    expected_output: Optional[str] = None
    expected_failure: Optional[ExpectedFailure] = False
    expected_failure_reason: Optional[ExpectedFailureReason] = None


@dataclass
class BuildTest:
    description: Description
    test_group: TestGroup
    test_type: str = "build"
    input: PurlComponents = None
    expected_output: Optional[str] = None
    expected_failure: Optional[ExpectedFailure] = False
    expected_failure_reason: Optional[ExpectedFailureReason] = None


@dataclass
class PurlTestDefinition:
    field_schema: Optional[Any] = None
    tests: Optional[list[Union[BuildTest, ParseTest]]] = None
