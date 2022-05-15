from matplotlib import pyplot as plt
import numpy as np


def generate_sine_data(Amplitude=1, Phase=0, Frequency=1, x_min=0, x_max=np.pi*2, n_samples=100):
    """

    :param Amplitude: amplitude of sine wave
    :param Phase: phase of sine wave
    :param Frequency: frequency of sine wave
    :param x_min: minimum x data
    :param x_max: maximum x data
    :param n_samples: number of samples in x
    :return:
    """
    # create_data
    x = np.linspace(x_min, x_max, n_samples)
    y = (Amplitude * np.sin(x*Frequency)) - Phase

    return x, y


def __data_plotter(x, y, x_label='x', y_label='y', title='excellent graph', grid=True):  # pragma: no cover
    """
    :param x:
    :param y:
    :param x_label:
    :param y_label:
    :param title:
    :param grid:
    :return:
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

