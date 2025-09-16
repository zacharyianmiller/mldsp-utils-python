#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-15"


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
    def __init__(self, kernel_size: int, num_cascades: int):
        self.kernel_size: int = kernel_size
        self.num_cascades = num_cascades
        self.int_delay = [IntDelay(kernel_size) for _ in range(self.num_cascades)]
        self.accumulator = np.zeros(self.num_cascades)
        self.reset()

    def reset(self):
        [d.clear() for d in self.int_delay]
        self.accumulator = np.zeros(self.num_cascades)

    def process(self, xn):
        yn: float = 0.0
        y1: float = xn
        for i in range(self.num_cascades):
            self.accumulator[i] += y1 - self.int_delay[i].process(y1)
            yn = self.accumulator[i] / self.kernel_size
            y1 = yn # cascade feedback

        return yn

if __name__ == "__main__":
    # Basic example
    mov_avg = MovAvg(kernel_size=64, num_cascades=4)
    x = [0] * 256 + [1] * 256 + [0] * 256
    y = np.zeros(len(x))
    for n in range(len(x)):
        y[n] = mov_avg.process(x[n])

    plt.plot(x)
    plt.xlabel('Time [samples]')
    plt.plot(y)
    plt.ylabel('Normalized value (unipolar)')
    plt.title('Cascaded Moving Average Filter')
    plt.show()