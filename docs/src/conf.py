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


def setup(app):
    app.add_css_file("css/custom.css")


project = 'ska-low-mccs-daq-interface'
copyright = "2023, SKAO"
author = "MCCS Team <drew.devereux@skao.int>"
release = "0.0.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

html_context = {
    "favicon_url": "img/favicon_mono.ico",
    "logo_url": "img/logo.png",
    "theme_logo_only": True,
}

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
    ("py:class", "grpc.ServicerContext"),
]