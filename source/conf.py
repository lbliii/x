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
import os, sys

# if computer is Mac, find the determined repo in the contributor's /Documents/github/determined folder
if sys.platform == 'darwin':
    sys.path.insert(0, '/Users/*/Documents/github/determined')

print("hiiiii!!!")

conf_dir = os.path.abspath(os.path.dirname(__file__))
determined_path = os.path.abspath(os.path.join(conf_dir, '../determined'))
sys.path.insert(0, determined_path)

# print the directory above the conf.py file
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# list the files in the directory above the conf.py file
print(os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))))

print("~~~~~~~~~~~~")
# -- Project information -----------------------------------------------------

project = 'project-x'
copyright = '2023, Determined AI'
author = 'Tara & LB'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc'
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
html_theme = 'sphinx_book_theme'
html_theme_options= {
    "home_page_in_toc": True,
    "toc_title": "Contents",
    "show_toc_level": 4,
    "show_navbar_depth": 1,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']