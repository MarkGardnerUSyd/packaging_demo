# Building documentation with Sphinx

We can generate really cool looking html documentation from markdown files, rst files, and indeed our code itself using [sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

Create a folder called docsrc, navigate to it in the terminal and type:

```bash
sphinx quick-start
./make html # windows
make html linux
```

answer all the promps however you want or just press enter to leave them blank.

This process will have created a number of folders inside your docsrc folder, and built some basic html at docsrc/build.

## editing documentation structure

Because we are going to want to host our documentation on github, we need the built documentation to end up in a folder at 

1. Copy everything in docsrc/source to docsrc and delete source. 
2. open make.bat and change to ```set SOURCEDIR=source``` ```set SOURCEDIR=.``` This tells sphinx that whatever directory the make.bat file is in is the source directory
3. change ```set BUILDDIR=build``` to ```set BUILDDIR=../docs``` This tells sphinx to output the built documentation to a folder one level from make.bat called docs (which is what we will need for github to host)
4. run ```make``` again! 

## actually writing/ generating the documentation! 

## hosting documentation with github

Every github repository has an associated 'github pages' that you can use to host your html documentation.



> hint! on enterprise github, this is available for all repos. On github.com, it is only available for public repos.

