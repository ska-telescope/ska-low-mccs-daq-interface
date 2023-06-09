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
    "favicon": "img/favicon_mono.ico",
    "logo": "img/logo.png",
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
intersphinx_mapping = {'python': ('https://docs.python.org/3.10', None)}

nitpick_ignore = [
]