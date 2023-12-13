# Configuration file for the Sphinx documentation builder.

import lumache as target_app


# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = target_app.__version__
version = target_app.__version__

# release = '0.1'
# version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'breathe',
    'sphinx_multiversion'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


breathe_projects = {
    "Nutshell": "../../doxygen_breathe_example/xml/",
}



latex_elements = {
    # Additional stuff for the LaTeX preamble.
    'preamble': '\\usepackage[utf8]{inputenc}',
    'babel': '\\usepackage[russian]{babel}',
    'cmappkg': '\\usepackage{cmap}',
    # 'fontenc': '\\usepackage[T1,T2A]{fontenc}',
    'utf8extra':'\\DeclareUnicodeCharacter{00A0}{\\nobreakspace}',
}


