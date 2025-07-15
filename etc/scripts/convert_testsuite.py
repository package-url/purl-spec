# -*- coding: utf-8 -*-
#
# Copyright (c) the purl authors
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Visit https://github.com/package-url/packageurl-python for support and
# download.

import json
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

from packageurl import PackageURL
from purl_test_dataclass import BuildTest
from purl_test_dataclass import ParseTest
from purl_test_dataclass import PurlComponents
from purl_test_dataclass import RoundtripTest


def convert_test(
    description,
    purl,
    canonical_purl,
    is_invalid,
    type,
    name,
    namespace,
    version,
    qualifiers,
    subpath,
):
    """
    Yield new test objects from the fields of a legacy test
    """

    components = PurlComponents(
        type=type,
        namespace=namespace,
        name=name,
        version=version,
        qualifiers=qualifiers,
        subpath=subpath,
    )

    if is_invalid:
        # yield tests that are expected to fail

        yield ParseTest(
            description=description,
            test_group="base",
            test_type="parse",
            input=purl,
            expected_output=None,
            expected_failure_reason="Should fail to parse a PURL from invalid purl input",
            expected_failure=True,
        )

        yield ParseTest(
            description=description,
            test_group="base",
            test_type="parse",
            input=canonical_purl,
            expected_output=None,
            expected_failure_reason="Should fail to parse a PURL from invalid canonical purl input",
            expected_failure=True,
        )

        yield BuildTest(
            description=description,
            test_group="base",
            test_type="build",
            input=components,
            expected_output=None,
            expected_failure_reason="Should fail to build a PURL from invalid input components",
            expected_failure=True,
        )

    else:
        # yield tests that are expected to pass
        yield RoundtripTest(
            description=f"{description}. Rountrip an input purl to canonical.",
            test_group="advanced",
            test_type="roundtrip",
            input=purl,
            expected_output=canonical_purl,
            expected_failure_reason=None,
            expected_failure=False,
        )

        yield ParseTest(
            description=description,
            test_group="base",
            test_type="parse",
            input=purl,
            expected_output=components,
            expected_failure_reason=None,
            expected_failure=False,
        )

        yield RoundtripTest(
            description=f"{description}. Rountrip a canonical input to canonical output.",
            test_group="base",
            test_type="roundtrip",
            input=canonical_purl,
            expected_output=canonical_purl,
            expected_failure_reason=None,
            expected_failure=False,
        )

        yield BuildTest(
            description=description,
            test_group="base",
            test_type="build",
            input=components,
            expected_output=canonical_purl,
            expected_failure_reason=None,
            expected_failure=False,
        )


def convert_example(purl):
    """
    Yield new test objects from a PURL example.
    """
    parsed = PackageURL.from_string(purl)
    components = PurlComponents(parsed.to_dict())

    yield ParseTest(
        description=f"Parse test for {type!r} PURL",
        test_type="parse",
        test_group="base",
        input=purl,
        expected_output=components,
        expected_failure_reason=None,
        expected_failure=False,
    )

    yield RoundtripTest(
        description=f"Rountrip test for {type!r} PURL",
        test_type="roundtrip",
        test_group="base",
        input=purl,
        expected_output=purl,
        expected_failure_reason=None,
        expected_failure=False,
    )

    yield BuildTest(
        description=f"Build test  for {type!r} PURL",
        test_group="base",
        test_type="build",
        input=components,
        expected_output=purl,
        expected_failure_reason=None,
        expected_failure=False,
    )


def convert_tests(test_dir: Path):
    """Read leagcy test JSON file and write updated test file in new format"""

    for test_file in test_dir.glob("*.json"):
        try:
            tests_data = json.loads(test_file.read_text())
        except Exception as e:
            raise Exception(test_file) from e

        new_tests = []
        for test in tests_data:
            new_tests.extend(convert_test(**test))

        new_tests = [asdict(t) for t in new_tests]

        test_file.write_text(json.dumps(new_tests, indent=2))


def convert_examples(def_dir: Path, test_dir: Path):
    """Read PURL type definition JSON file and write updated test file in new format"""

    # mapping of test data by type
    ex_tests_by_type = defaultdict(list)

    # build tests from examples
    for def_file in def_dir.glob("*-definition.json"):
        try:
            def_data = json.loads(def_file.read_text())
        except Exception as e:
            raise Exception(def_file) from e

        def_type = def_data["type"]
        examples = [e.strip() for e in def_data["examples"]]
        print("Found examples for", def_type, examples)

        for purl in examples:
            ex_tests = convert_example(purl=purl)
            ex_tests_by_type[def_type].extend(asdict(t) for t in ex_tests)

    # extend existing tests with new tests
    tf_by_type = {tf.name.replace("-test.json", ""): tf for tf in test_dir.glob("*-test.json")}

    # iterate over bew tests and save as new or extend preexisting
    for ttype, tests in ex_tests_by_type.items():
        test_file = tf_by_type.get(ttype)
        if test_file:
            try:
                # extend existing with new from examples
                tests_data = json.loads(test_file.read_text())
                tests_data.extend(tests)
            except Exception as e:
                raise Exception(test_file) from e
        elif not test_file:
            # use new as-is
            test_file = test_dir / f"{ttype}-test.json"
            tests_data = tests

        test_file.write_text(json.dumps(tests_data, indent=2))


if __name__ == "__main__":
    import sys

    what = sys.argv[1]

    if what == "convert":
        test_dir = sys.argv[2]
        convert_tests(Path(test_dir))
    elif what == "examples":
        test_dir = sys.argv[2]
        def_dir = sys.argv[3]
        convert_example(Path(test_dir, def_dir))
