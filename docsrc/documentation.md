# Add documentation

There are probably three main levels of documentation for your code.

1. Readme.md: This is non negotiable!  Although it is acceptable in simple cases to essentially put all the documentation in the readme, in general it is better practice for the readme to be 'short and sharp' and provide detailed documentation elsewhere. See [here](https://github.sydney.edu.au/Image-X/Template) for a good template.
2. More detailed examples. This can be in the form of further markdown files, or you can use sphinx
3. Comments and docstrings in your code! These can also be incorporated into your general documentation using sphinx.

## Create README.md

Inside DemoPythonProject, create a file called ```README.md``` and copy the below into it:

````markdown
# DemoPythonProject

**Author:** *{{ Your Name }}*

*Give a brief summary of the purpose of the code and what it does.*

## Setup/Build/Install

For a properly package python package that is released on PyPi, the answer would be:
```
pip install DemoPythonProject
```

## Usage

See [our documentation](link)

## Directory Structure

- **DemoPythonProject** Source code
- **examples** examples of how to use
- **docsrc** source documentation
- **docs** html documentation generated with sphinx
````

## Set up SPHINX

add the following lines to Makefile:

```
github:
	@make html
	@cp -a _build/html/. ../docs
```

add the following to make.bat, just before the %SPHINXBUILD% statement:

```
if "%1" == "github" (
    %SPHINXBUILD% -M html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS%
    robocopy %BUILDDIR%/html ../docs /E > nul
    echo.Generated files copied to ../docs
    goto end
)
```



