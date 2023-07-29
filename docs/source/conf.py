# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

from datetime import datetime
from setuptools.config import read_configuration

import django

repo_config = read_configuration("../../setup.cfg")["metadata"]


# Note: You may need to change the path to match
# your project's structure
sys.path.insert(0, os.path.abspath("../../src")) 
sys.path.insert(0, os.path.abspath(".."))  # For discovery of Python modules
sys.path.insert(0, os.path.abspath("."))  # For finding the django_settings.py file

# This tells Django where to find the settings file
os.environ["DJANGO_SETTINGS_MODULE"] = "django_settings"
# This activates Django and makes it possible for Sphinx to
# autodoc your project
django.setup()

project = repo_config["name"]
copyright = f'{datetime.now().year}, {repo_config["author"]}'
author = repo_config["author"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
