#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"

from matplotlib import pyplot as plt

""" moving_average.py: 

    Windowed moving average filter based on a running
    cumulative sum via an integer delay line.

"""


# Python dependencies
import numpy as np
import matplotlib.pyplot as plt


# Custom functions
from effects.delays.int_delay import IntDelay


class MovAvg:
    def __init__(self, kernel_size):
        self.kernel_size = kernel_size
        self.int_delay = IntDelay(kernel_size)
        self.accumulator: float = 0.0
        self.reset()

    def reset(self):
        self.int_delay.reset()
        self.accumulator = 0.0

    def process(self, xn):
        self.accumulator += xn - self.int_delay.process(xn)
        return self.accumulator / self.kernel_size

if __name__ == "__main__":
    # Basic example
    mov_avg = MovAvg(kernel_size=256)
    x = [0] * 256 + [1] * 256 + [0] * 256
    y = np.zeros(len(x))
    for n in range(len(x)):
        y[n] = mov_avg.process(x[n])

    plt.plot(x)
    plt.xlabel('Time [samples]')
    plt.plot(y)
    plt.ylabel('Normalized value (unipolar)')
    plt.title('Moving Average Filter')
    plt.show()