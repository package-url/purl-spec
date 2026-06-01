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

import json
from pathlib import Path


def format_json(path: Path):
    """
    Format in place and recursively all the files with a .json extension at ``path``.
    """
    for json_file in path.rglob("**/*.json"):
        if not json_file.is_file():
            continue
        try:
            unformatted = json.loads(json_file.read_text())
            # note the trailing LF
            formatted = json.dumps(unformatted, indent=2) + "\n"
            json_file.write_text(formatted)
        except Exception as e:
            print(f"Failed to format JSON file: {json_file!r}: {e!r}")


if __name__ == "__main__":
    import sys

    path = sys.argv[1]
    format_json(Path(path))
