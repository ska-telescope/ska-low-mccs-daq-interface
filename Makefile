include .make/base.mk

########################################
# DOCS
########################################
DOCS_SPHINXOPTS = -n -W --keep-going

docs-pre-build:
	poetry config virtualenvs.create false
	poetry install --no-root --only docs

.PHONY: docs-pre-build


########################################
# PYTHON
########################################
include .make/python.mk

PYTHON_LINE_LENGTH = 88

python-post-lint:
	mypy src/ tests/

.PHONY: python-post-lint
