.. Cool_Project documentation master file, created by
   sphinx-quickstart on Sun May 15 13:05:05 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python packaging and release tutorial
=====================================

This tutorial takes you through all the steps you should put in place to release a python project on PyPi so
it can be pip installed. Basically, this tutorial will teach you how to recreate
this repository from scratch (including this documentation, how meta!)

There are four main things to consider before releasing your code (apart from obviously the code itself!)

#. Adding a license
#. some example scripts
#. test cases
#. documentation
#. packaging and release.

Now, full disclosure. Once your code is ready and you have added a license, you can skip straight ahead to
4 without considering any of the other steps. However, assuming that the reason you are releasing you code is that you hope that people will actually use it, I **highly** recomend you include all of these. This tutorial will show you to to quickly set up all these facets.

Prerequisites
-------------

- An account on `github.com <https://github.com/>`_ (this is different from our enterprise github)
- An account on `test pypi <https://test.pypi.org/>`_ - and you will need to remember your account details!
- A terminal in your OS. On windows, I think pycharm is the easiest option.
- From there, clone this directory into a new environment and do

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   /set_up_environment.md
   /package_setup.md
   /add_supporting_files.md
   /examples.md
   /testing.md
   /documentation.md
   /packaging.md
   /uploading.md
   /code_docs.md

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
