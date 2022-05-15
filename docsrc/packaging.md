# Packaging and PyPi upload



These instructions are based off [this tutorial])(https://packaging.python.org/en/latest/tutorials/packaging-projects/)

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

Obviously, this is a template, and we need to update it to reflect our project.

- name: your name
- version: ```attr: MyPackage.__version__ ```
- author_email >> your email
  - This takes the version from the ```__init__``` file in  MyPackage
- description >> write a short description e.g. "this is to demonstrate python packaging"
- long_description - already pointing towards the readme so we don't have to do anything
- url: can point either to the github, or, if you've set it up your html documentation
- Bug Tracker: point to your issue page
- License: 



## difference between install requires and dev-requirements.txt

note that setup.cfg ```install_requires``` tag only defines depenencies of our **package**. Meanwhile, dev-requirements.txt contains all the dependencies that developers will need, e.g. pytest, sphinx, etc. In this way, developers can still quickly setup a new project but we aren't cluttering users environements up with useless packages. 



