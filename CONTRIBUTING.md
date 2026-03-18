# Contributing

Thank you for your interest in contributing to the PURL Specification. 
You can contribute by joining discussions, reporting bugs, registering a
new PURL **type**, writing documentation or adding/improving test cases.

The **purl-spec** project is responsible for development and maintenance of:
- [ECMA-427](https://ecma-tc54.github.io/ECMA-427/) - This is the Ecma 
standard for Package-URL (PURL); also known as the "Core Specification".
- Other PURL documentation including JSON Schemas, PURL **type** definitions,
test cases, how-to guides and more. 

## Documentation 
PURL documentation is published at:
- [ECMA-427](https://ecma-tc54.github.io/ECMA-427/) - the Core Specification
- https://wwww.packageurl.org/ - this is the production website for the 
project.
- https://package-url.github.io/www.packageurl.org/ - this is the staging
website which may have more recent content than production.

**NB**: Please follow our basic [style guide](https://github.com/package-url/community/blob/main/documentation/style-guide.md) for writing PURL documentation.

## Repository content

This PURL Specification repository is different from many other GitHub 
repositories because the only code is for the repository workflows.
The primary content is documentation in the form of:
- JSON Schema files for the specification
- JSON data files for PURL **type** definitions or test cases
- Markdown files for human-written or generated documentation

A change to any of these files requires a pull request.

## Pull Request Guidelines

Please read the following guidelines carefully before submitting a pull 
request.

- **Attach your PR to an existing issue.** Discuss the reason for a PR in an 
existing issue or create a new one. The Conversation feature for a PR should 
used to discuss the PR details, not the reason for the PR.

- **Keep your PR focused** Keep your PR small and focused. This will optimize
review and implementation.

- **Write your own descriptions, comments, and documentation.** All written
  content in a PR must be authored by a human.

- **Disclose any AI usage.** If any part of your contribution was generated or
  assisted by AI, you must disclose this and specify the tools used and how.

- You must agree to the Developer [Certificate of Origin](http://developercertificate.org/). For commits, it is best to simply add a line 
like this to your commit message, with your name and email::

      Signed-off-by: Jane Doe <developer@example.com>

**A PR that violates these rules will be closed.**

## Development
For most changes, except documentation in human-written markdown files, you 
will want to install a local development environment because you will need to 
run some utilities to:
- Validate JSON schema changes for correctness and format
- Validate that test case data files are schema-valid
- Generate or update generated PURL **type** documentation

To setup an environment to contribute a pull request follow these instructions:

### Setup
Ensure that you have a recent Python version 3 and Make installed.
Configure your environment:

    ```bash
    make conf
    ```

### Usage
To validate that the schemas and data files are correct, run:

```bash
make check
```

To regenerate the Python utility model code from the JSON schemas, then 
regenerate the PURL type documentation from the JSON PURL type definition 
files, run:

```bash
make gencode
make gendocs
```

## Project communications

You can also participate in **purl-spec** project meetings or via Slack. See 
the [Participate](https://www.packageurl.org/docs/participate/meetings) page 
on the website for details.



