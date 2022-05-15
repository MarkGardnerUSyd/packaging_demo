# Packaging and releasing python code on pypi

1. Create a new folder somewhere called "DemoPythonProject"
2. Open this folder as a new project in your chosen IDE

## Environment set up

Ideally for any new python project, you would start by creating a fresh virtual environment.

However, the way that you create new environments depends on a lot of different factors so it is difficult for me to give specific instructions. 

## .gitignore

It's better to add a .gitignore to your repository sooner rather than later. [Here's](https://github.com/github/gitignore/blob/main/Python.gitignore) a useful template.

## Package creation

Create a new folder called ```MyPackage```

This folder is where we are going to put all our source code. This is what will eventually be built and uploaded to PyPi. The remaining directories we will be creating are purely for support - testing, examples, and documentation.

As some demo code, we are going to use a 'sine_plotter' function. 

1. Create a new python file inside ```MyPackage``` called ```PlotSineWave.py``` and copy the below code into it:

```python
from matplotlib import pyplot as plt
import numpy as np


def sine_wave_plotter(Amplitude=1, Phase=0, Frequency=1, x_min=0, x_max=np.pi*2, n_samples=100):
    """
    this function plots a sine wave with the variables defined below.

    :param Amplitude: Amplitude of sine wave
    :param Phase: phase of sine wave
    :param Frequency: Frequency of sine wave
    :param x_min: start of x data
    :param x_max: end of x data
    :param n_samples: number of samples in x data
    :return: None
    """

    # create_data
    x = np.linspace(x_min, x_max, n_samples)
    y = (Amplitude * np.sin(x*Frequency))

    # plot figure
    plt.figure()
    plt.plot(x, y)
    plt.grid()
    plt.xlabel('x [AU]')
    plt.ylabel('y [AU]')
    plt.show()


```

2. Create a new file called ```__init__.py```' and copy the below code into it

```python
"""
This library allows a user to plot a sine wave. It's fully sick.
"""
__version__ = '0.0.0'
```

> Always have an ```__init__.py``` file in the root of a package. It can be empty if you want, but it should always be there.

##  Set up examples 

If you're bothering to release your code publically, you are probably hoping someone will use it. In that case, it is integral to have some simple of examples of using your code. Create a new folder inside DemoPythonProject called ```examples```. Inside this folder create a file called ```demonstrate_sine_wave_plotter.py``` and copy the below code into it:

```python
from pathlib import Path
import sys

'''
For testing/ example purposes it's safest to manually append the path variable to ensure our 
package will always be found. This isn't necessary once we actually install the package 
because installation in python essentially means "copying the package to a place where it can be found"
'''
this_file_loc = Path(__file__)
sys.path.insert(0, str(this_file_loc.parent.parent))

'''
Now we can guarantee that the package will be found we can import it:
'''
import MyPackage

'''
the help and version for the package come from the __init__.py file:
'''
print(f'packge version = {MyPackage.__version__}. Package info {help(MyPackage)}')

MyPackage.sine_wave_utilities.sine_wave_plotter()

# since we are only using one function from this package a better way to import would be
from MyPackage.sine_wave_utilities import sine_wave_plotter
# or
from MyPackge import PlotSineWave as PSW
```



> hint: when creating examples and documentation, ask yourself 'what are some typical problems people have that I think this code can solve' and provide examples of how someone can use the code to solve such problems

## Set up some tests

It is best practice to set up a few tests of your package. Although testing is probably a topic that deserves a dedicated coding club, in this case it's pretty simple since our package is so small!

Inside DemoPythonPackage, create a folder called testing. Add the following scripts:

```:
from pathlib import Path
import sys
import numpy as np
'''
For testing/ example purposes it's safest to manually append the path variable to ensure our 
package will always be found. This isn't necessary once we actually install the package 
because installation in python essentially means "copying the package to a place where it can be found"
'''
this_file_loc = Path(__file__)
sys.path.insert(0, str(this_file_loc.parent.parent))
# note: insert(0) means that the path is above is the FIRST place that python will look for imports
# sys.path.append means that the path above is the LAST place
from MyPackage import sine_wave_utilities as swu

def test_amplitude():
    x, y = swu.generate_sine_data(Amplitude=10)
    assert y.max() > 9.9  # can't guarantee max=10 because we have finite samples
    assert y.min() < -9.9

def test_range():
    x, y = swu.generate_sine_data(x_max=10, x_min=-8)
    assert x.max() == 10
    assert x.min() == -8

def test_n_samples():
    x, y = swu.generate_sine_data(n_samples=192)
    assert y.shape[0] == 192

def test_phase():
    x_0, y_0 = swu.generate_sine_data(Phase=0)
    x_1, y_1 = swu.generate_sine_data(Phase=1)
    # if phase works, at a minimum we should see that these two data sets are different...
    assert not np.equal(y_0, y_1)
```

To execute these tests, we just have to run [pytest](https://docs.pytest.org/en/7.1.x/) from the root directory. Pytest is smart enough to find our tests by itself.

```bash
# from command line:
pytest
```



> 

When you run these tests, **you should get a failure!** This is because I did not actually implement the phase variable properly. To fix this, go to MyPackage / demonstrate_sine_plotter.py and make the following change:

```python
# change
y = (Amplitude * np.sin(x*Frequency))
# to
y = (Amplitude * np.sin(x*Frequency)) - Phase
```

now if you execute the tests again, they should all pass/

## assessing test cover

A key aspect of your testing framework is how many lines of your package actually get executed during testing. There is an easy way to check this, using the package [coverage](https://coverage.readthedocs.io/en/6.3.3/)

```bash
# from command line:
coverage run -m pytest
coverage report
```

This reveals that we only have 47% coverage on our sine_wave_utilities module:

```bash
Name                                Stmts   Miss  Cover
-------------------------------------------------------
MyPackage\__init__.py                   1      0   100%
MyPackage\sine_wave_utilities.py       15      8    47%
tests\test_sine_wave_utilities.py      21      0   100%
-------------------------------------------------------
TOTAL                                  37      8    78%

```

Why is this so low!? The answer is that we haven't written any tests at all for the ```data_plotter``` method.

Now at this point, we can do a few things:

1. Write some more tests. This is tricky for methods that generate a function for two reasons; generating plots from the command line often blocks further execution of scripts, and it is hard to test if a plot is 'right' or not.
2. Just accept our bad coverage and move on
3. tell coverage we intentionally left that method out of our test framework by putting ```# pragma: no cover``` next to the method definition. 

I am going to take the third option, after which our coverage report looks like this:

```bash
Name                                Stmts   Miss  Cover
-------------------------------------------------------
MyPackage\__init__.py                   1      0   100%
MyPackage\sine_wave_utilities.py        6      0   100%
tests\test_sine_wave_utilities.py      21      0   100%
-------------------------------------------------------
TOTAL                                  28      0   100%

```

 Boo yah!

## make a badge for test coverage

The inclusion or absence of tests, as well as the extent of test coverage is one of the things that developers will look to when considering whether to use your package. If the tests are there, it's generally an indication of a reasonably high quality code base. Therefore, it can be handy  to generate a badge that you can put in the readme. 

> hint: you may have to update the output path below if you don't have a folder yet called docsrc/__resources

```bash
 coverage-badge -f -o docsrc/__resources/coverage.svg
```

![](docsrc\__resources\coverage.svg)

nice! 

## Documentation

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

## Building documentation with Sphinx

We can generate really cool looking html documentation from markdown files, rst files, and indeed our code itself using [sphinx](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

Create a folder called docsrc, navigate to it in the terminal and type:

```bash
sphinx quick-start
./make html # windows
make html linux
```

answer all the promps however you want or just press enter to leave them blank.

This process will have created a number of folders inside your docsrc folder, and built some basic html at docsrc/build.

### editing documentation structure

Because we are going to want to host our documentation on github, we need the built documentation to end up in a folder at 

1. Copy everything in docsrc/source to docsrc and delete source. 
2. open make.bat and change to ```set SOURCEDIR=source``` ```set SOURCEDIR=.``` This tells sphinx that whatever directory the make.bat file is in is the source directory
3. change ```set BUILDDIR=build``` to ```set BUILDDIR=../docs``` This tells sphinx to output the built documentation to a folder one level from make.bat called docs (which is what we will need for github to host)
4. run ```make``` again! 

## actually writing/ generating the documentation! 

## hosting documentation with github

Every github repository has an associated 'github pages' that you can use to host your html documentation.



> hint! on enterprise github, this is available for all repos. On github.com, it is only available for public repos.



