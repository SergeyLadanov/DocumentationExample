## Template for the Read the Docs tutorial


This GitHub template includes fictional Python library
with some basic Sphinx docs.

Read the tutorial here:

https://docs.readthedocs.io/en/stable/tutorial/

### Install requirements:
```
pip install -r requirements.txt
pip install -r docs/requirements.txt
pip install -e .
```


### Install texlive and cyrilic for pdf generation in linux:

```
sudo apt-get install texlive-lang-cyrillic -y
```

### Domains for doxygen documentation (using breathe)

https://breathe.readthedocs.io/en/latest/domains.html


### Build docs

Simple:

```
make --directory docs
```

Multiversion build:

```
sphinx-multiversion docs/source build/html
```
