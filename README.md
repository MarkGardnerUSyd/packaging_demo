# Packaging and releasing python code on pypi
![](docsrc/__resources/coverage.svg)

Author: Brendan Whelan

This repository is intended to demonstrate the key tasks involved in publicly releasing python code as a member 
of Image X. The code itself just plots a sine wave.

Key topics include:

- Choosing a license
- Setting up packaging tools
- Optional: set up a test framework
- Optional: set up and host html documentation

## Setup/Build/Install

To complete this tutorial you will need:

- An account on [github.com](https://github.com/) (this is different from our enterprise github)
- An account on [test pypi](https://test.pypi.org/) - and you will need to remember your account details!
- A terminal in your OS. On windows, I think pycharm is the easiest option. 
- From there, clone this directory into a new environment and do
```
pip install -r dev-requirements.txt
```

## Usage

A detailed tutorial is provided [here](https://acrf-image-x-institute.github.io/packaging_demo/)

- *docs* contains html documentation
- *docsrc* markdown/rst source documentation
- *tests* test cases
- *MyPackage* source code







