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
from pathlib import Path


def remove_duplicates(test_dir: Path):
    """Remove duplicates"""

    for test_file in test_dir.glob("*.json"):
        try:
            test_data = json.loads(test_file.read_text())
        except Exception as e:
            raise Exception(test_file) from e

        new_tests = []

        for test in test_data["tests"]:
            if test in new_tests:
                continue
            else:
                new_tests.append(test)

        test_data["tests"] = new_tests
        test_file.write_text(json.dumps(test_data, indent=2) + "\n")


if __name__ == "__main__":
    import sys

    test_dir = sys.argv[1]
    remove_duplicates(Path(test_dir))
