# Packaging and releasing python code on pypi

1. Create a new folder somewhere called "DemoPythonProject"
2. Open this folder as a new project in your chosen IDE

## Environment set up

Ideally for any new python project, you would start by creating a fresh virtual environment.

However, the way that you create new environments depends on a lot of different factors so it is difficult for me to give specific instructions. 



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

## .gitignore

It's better to add a .gitignore to your repository sooner rather than later. [Here's](https://github.com/github/gitignore/blob/main/Python.gitignore) a useful template.

## License







