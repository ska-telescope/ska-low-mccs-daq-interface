"""Configuration file for Sphinx."""
import os
import sys

# WORKAROUND: https://github.com/sphinx-doc/sphinx/issues/9243
import sphinx.builders.html
import sphinx.builders.latex
import sphinx.builders.texinfo
import sphinx.builders.text
import sphinx.ext.autodoc

sys.path.insert(0, os.path.abspath("../../src"))


project = 'ska-low-mccs-daq-interface'
copyright = "2023, SKAO"
author = "MCCS Team <drew.devereux@skao.int>"
release = '0.1.0'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]

# templates_path = []
exclude_patterns = []

html_theme = "ska_ser_sphinx_theme"
# html_static_path = []

html_context = {}

#################################
# autodoc config
#################################
autodoc_mock_imports = [
]

#################################
# intersphinx config
#################################
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.10", None),
    "ska-control-model": ("https://developer.skao.int/projects/ska-control-model/en/0.3.1/", None),
}

nitpicky = True

nitpick_ignore = [
    ("py:class", "daq_pb2.ConfigurationResponse"),
    ("py:class", "daq_pb2.commandResponse"),
    ("py:class", "daq_pb2.configDaqRequest"),
    ("py:class", "daq_pb2.daqStatusRequest"),
    ("py:class", "daq_pb2.daqStatusResponse"),
    ("py:class", "daq_pb2.getConfigRequest"),
    ("py:class", "daq_pb2.startDaqRequest"),
    ("py:class", "daq_pb2.startDaqResponse"),
    ("py:class", "daq_pb2.stopDaqRequest"),
    ("py:class", "daq_pb2.stopDaqResponse"),
    ("py:class", "daq_pb2.bandpassMonitorStartRequest"),
    ("py:class", "daq_pb2.bandpassMonitorStartResponse"),
    ("py:class", "grpc.ServicerContext"),
]
