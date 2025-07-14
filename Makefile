# SPDX-License-Identifier: MIT
# Copyright (c) the purl authors
# Visit https://github.com/package-url/purl-spec and https://packageurl.org for support

PYTHON_EXE?=python3
VENV_LOCATION=venv
ACTIVATE?=. ${VENV_LOCATION}/bin/activate;

CODEGEN?=datamodel-codegen \
    --target-python-version 3.10 \
    --use-double-quotes \
    --use-exact-imports \
    --use-standard-collections \
    --wrap-string-literal \
    --enum-field-as-literal all \
    --formatters ruff-format \
    --field-constraints \
    --disable-timestamp \
    --keep-model-order \
    --custom-file-header-path LICENSE \
    --input-file-type jsonschema \
    --output-model-type pydantic_v2.BaseModel

virtualenv:
	@echo "-> Bootstrap the virtualenv with PYTHON_EXE=${PYTHON_EXE}"
	${PYTHON_EXE} -m venv ${VENV_LOCATION}

conf: virtualenv
	@echo "-> Install dependencies"
	@${ACTIVATE} pip install -r requirements.txt

format:
	@echo "-> Run Ruff format"
	@${ACTIVATE} ruff check --select I --fix
	@${ACTIVATE} ruff format
	@echo "-> Run Ruff linter"
	@${ACTIVATE} ruff check --fix

checkjson:
	@echo "-> Validate JSON schemas"
	@${ACTIVATE} check-jsonschema --check-metaschema --verbose schemas/*.json
	@echo "-> Validate JSON data files against the schemas"
	@${ACTIVATE} check-jsonschema --schemafile schemas/purl-types-index.schema.json --verbose types/index.json
	@${ACTIVATE} check-jsonschema --schemafile schemas/purl-type-definition.schema.json --verbose types/*-definition.json
#	@${ACTIVATE} check-jsonschema --schemafile schemas/purl-test.schema.json --verbose types/*-test.json *-test.json

check: checkjson
	@echo "-> Run Ruff linter validation (pycodestyle, bandit, isort, and more)"
	@${ACTIVATE} ruff check
	@echo "-> Run Ruff format validation"
	@${ACTIVATE} ruff format --check

clean:
	@echo "-> Clean the Python env"
	rm -rf .venv/
	find . -type f -name '*.py[co]' -delete

generate:
	@echo "-> Generate Python code from schemas"
	@${ACTIVATE} ${CODEGEN} \
	    --input schemas/purl-types-index.schema.json \
	    --output etc/scripts/purl_types_index.py
	@${ACTIVATE} ${CODEGEN} \
	    --input schemas/purl-type-definition.schema.json \
	    --output etc/scripts/purl_type_definition.py
	@${ACTIVATE} ${CODEGEN} \
	    --input schemas/purl-test.schema.json \
	    --output etc/scripts/purl_test.py
	@echo "-> Run Black format for generated code"
	@${ACTIVATE} black -l 100 --preview --enable-unstable-feature string_processing etc/scripts/*.py

docs:
	@${ACTIVATE} python etc/scripts/generate_index_and_docs.py


.PHONY: virtualenv conf valid checkjson check clean generate docs
