# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import datetime
import sys
sys.path.append('/docs/source')

# -- Project information -----------------------------------------------------

project = 'GEFEST'
copyright = '{}, NSS Lab'.format(datetime.datetime.now().year)
author = 'NSS Lab'

# The full version, including alpha/beta/rc tags
version = '0.0.1'
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'autodocsumm',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_rtd_theme"
# html_logo = "/docs/img/gefest_logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

autodoc_inherit_docstrings = False
# napoleon_google_docstring = True
# napoleon_include_init_with_doc = True
# napoleon_numpy_docstring = True
autoclass_content = 'class'
autodoc_typehints = 'none'
autodoc_member_order = 'bysource'

# --- Work around to make autoclass signatures not (*args, **kwargs) ----------


# class FakeSignature():
#     def __getattribute__(self, *args):
#         raise ValueError


# def f(app, obj, bound_method):
#     if "__new__" in obj.__name__:
#         obj.__signature__ = FakeSignature()


# def setup(app):
#     app.connect('autodoc-before-process-signature', f)
