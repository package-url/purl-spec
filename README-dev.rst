Development setup and instructions
=====================================

We use some code:

- to validate the JSON schemas for correctness and format them, and
- to validate that the test suite data files are schema-valid.

To setup an environment to contribute to the Package-URL spec and standard, follow these
instructions::

Setup
-------

1. Ensure that you have a recent Python version 3 and Make installed.
2. Configure your environment::

    make conf

Usage
-------

To validate that the schemas and data files are correct, run::

    make check


To regenerate the Python utility model code from the JSON schemas, then regenerate the
PURL type documentation from the JSON PURL type definition files, run::

    make generate
    make docs

