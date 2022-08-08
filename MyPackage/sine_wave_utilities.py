from matplotlib import pyplot as plt
import numpy as np


def generate_sine_data(Amplitude=1, Phase=0, Frequency=1, x_min=0, x_max=np.pi*2, n_samples=100):
    """
    generates sine data for the fiven input parameters

    :param Amplitude: amplitude of sine wave
    :type Amplitude: float
    :param Phase: phase of sine wave
    :type Phase: float
    :param Frequency: frequency of sine wave
    :type Frequency: float
    :param x_min: minimum x data
    :type x_min: float
    :param x_max: maximum x data
    :type x_max: float
    :param n_samples: number of samples in x
    :type n_samples: int
    :return: x, y, the x and y values of the generated sine plot

    """
    # create_data
    x = np.linspace(x_min, x_max, n_samples)
    y = (Amplitude * np.sin(x*Frequency)) - Phase

    return x, y


def data_plotter(x, y, x_label='x', y_label='y', title='excellent graph', grid=True):   # pragma: no cover
    """
    just plots the data in x and y as a line plot

    :param x: x data for plotting;
    :type x: 1D list or array
    :param y: y data for plotting
    :type y: 1D list or array
    :param x_label: x axis label
    :type x_label: str, optional
    :param y_label: y axis label
    :type y_label: str, optional
    :param title: plot title
    :type title: str, optional
    :param grid: True plots grid
    :type grid: bool, optional
    """

    # plot figure
    plt.figure()
    plt.plot(x, y)
    if grid:
        plt.grid()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

