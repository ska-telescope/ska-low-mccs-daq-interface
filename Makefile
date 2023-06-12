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

########################################
# gRPC
########################################
GRPC_PROTOS_FOLDER = ./src/ska_low_mccs_daq_interface/protos
GRPC_OUTPUT_FOLDER = ./src/ska_low_mccs_daq_interface/generated_code
grpc-code:
	python -m grpc_tools.protoc -I $(GRPC_PROTOS_FOLDER) --python_out=$(GRPC_OUTPUT_FOLDER) --mypy_out=$(GRPC_OUTPUT_FOLDER) --grpc_python_out=$(GRPC_OUTPUT_FOLDER) daq.proto
	sed -i -e 's/import daq_pb2/from ska_low_mccs_daq_interface.generated_code import daq_pb2/g' $(GRPC_OUTPUT_FOLDER)/daq_pb2_grpc.py

.PHONY: grpc-code