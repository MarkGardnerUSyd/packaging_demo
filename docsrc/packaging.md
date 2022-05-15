# Packaging and PyPi upload

## setting up the meta data files

The first thing we need to do is set up some files that hold the information about how to build our project, what it's depenencies are, etc. These instructions are based off [this tutorial])(https://packaging.python.org/en/latest/tutorials/packaging-projects/)

First create a file called pyproject.toml and copy the below code into it. This file identifies what system we are using to build and package our code.

```
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
```

Next, make a new file called setup.cfg and copy the below into it

> The setup file can be either a .py file or a .cfg file. I am using cfg as recommended in the official packaging instructions, but I don't really know what the pros and cons are. 

```cfg
[metadata]
name = example-package-YOUR-USERNAME-HERE
version = 0.0.1
author = Example Author
author_email = author@example.com
description = A small example package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/pypa/sampleproject
project_urls =
    Bug Tracker = https://github.com/pypa/sampleproject/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src
```

Obviously, this is a template, and we need to update it to reflect our project. The version of this file inside this repository has already been updated; you can use this as a base for creating your own setup.cfg files.

**important: make sure you change the name of the package to reflect your username. This is to ensure the package has a unique name**

## Building the package

From a terminal, type

```
python -m build
```

If succesful, you will have a new folder called 'dist' which contains the distribution of your code. This is what we can uploadto PyPi.

## difference between install requires and dev-requirements.txt

note that setup.cfg ```install_requires``` tag only defines depenencies of our **package**. Meanwhile, dev-requirements.txt contains all the dependencies that **developers** will need, e.g. pytest, sphinx, etc. In this way, developers can still quickly setup a new project and end users only get the requirements to run the code.



