# SPDX-License-Identifier: MIT
# Copyright (c) the purl authors
# Visit https://github.com/package-url/purl-spec and https://packageurl.org for support

PYTHON_EXE?=python3
VENV_LOCATION=venv
ACTIVATE?=. ${VENV_LOCATION}/bin/activate;

CODEGEN?=datamodel-codegen \
    --target-python-version 3.10 \
    --use-double-quotes \
    --enum-field-as-literal all \
    --use-schema-description \
    --field-constraints \
    --disable-timestamp \
    --custom-file-header-path LICENSE \
    --input-file-type jsonschema \
    --output-model-type dataclasses.dataclass \

virtualenv:
	@echo "-> Bootstrap the virtualenv with PYTHON_EXE=${PYTHON_EXE}"
	${PYTHON_EXE} -m venv ${VENV_LOCATION}

conf: virtualenv
	@echo "-> Install dependencies"
	@${ACTIVATE} pip install -r requirements.txt

format:
	@echo "-> Run Ruff format"
	@${ACTIVATE} ruff format
	@echo "-> Run Ruff linter"
	@${ACTIVATE} ruff check --fix

check:
	@echo "-> Run Ruff linter validation (pycodestyle, bandit, isort, and more)"
	@${ACTIVATE} ruff check
	@echo "-> Run Ruff format validation"
	@${ACTIVATE} ruff format --check
	@echo "-> Validate JSON schemas"
	@${ACTIVATE} check-jsonschema --check-metaschema --verbose schemas/*.json
	@echo "-> Validate JSON data files against the schemas"
	@${ACTIVATE} check-jsonschema --schemafile schemas/purl-types-index.schema.json --verbose types/index.json
	@${ACTIVATE} check-jsonschema --schemafile schemas/purl-type-definition.schema.json --verbose types/*-definition.json
	@${ACTIVATE} check-jsonschema --schemafile schemas/purl-test.schema.json --verbose types/*-test.json *-test.json

clean:
	@echo "-> Clean the Python env"
	rm -rf .venv/
	find . -type f -name '*.py[co]' -delete

generate:
	@${ACTIVATE} ${CODEGEN} \
	    --input schemas/purl-types-index.schema.json \
	    --output etc/scripts/purl_types_index.py
	@${ACTIVATE} ${CODEGEN} \
	    --input schemas/purl-type-definition.schema.json \
	    --output etc/scripts/purl_type_definition.py
	@${ACTIVATE} ${CODEGEN} \
	    --input schemas/purl-test.schema.json \
	    --output etc/scripts/purl_test.py

docs:
	@${ACTIVATE} python etc/scripts/generate_index_and_docs.py


.PHONY: virtualenv conf valid check clean generate docs
