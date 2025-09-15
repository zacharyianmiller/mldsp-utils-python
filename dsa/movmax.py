#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"

import sys

""" movmax.py: 

"""

# Python dependencies
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

class MovMax:
    def __init__(self, kernel_size):
        self.kernel_size = kernel_size
        self.front_max = sys.float_info.min
        self.back: list = [sys.float_info.min] * kernel_size
        self.front: list = []

    def process(self, xn):
        # Push front (incoming data) max
        self.front_max = np.fmax(self.front_max, xn)
        self.front.append(xn)

        # Pop back list
        if len(self.back) == 0:
            back_max = sys.float_info.min
            while len(self.front) != 0:
                # Reverse cumulative max, set back max
                back_max = np.fmax(back_max, self.front.pop())
                self.back.append(back_max)

            # Reset front max
            self.front_max = sys.float_info.min

        # Compare maxes of front and back stacks
        return np.fmax(self.front_max, self.back.pop())


def movmax_driver():
    mov_max = MovMax(kernel_size=3)

    # Simple example
    # x = [0, 1, 2, 3, 2, 1, 0, 0, 0]
    # y: list = [0] * len(x)
    # for n in range(len(x)):
    #     y[n] = mov_max.process(x[n])

    # Audio example
    x, fs = sf.read("../testing/audio/SnareTop.wav")
    x = np.abs(x[20000:22500,1])
    y = np.zeros(x.shape[0])
    for n in range(x.shape[0]):
        y[n] = mov_max.process(x[n])


    plt.plot(x)
    plt.plot(y, color='r', linestyle='--')
    plt.show()

if __name__ == "__main__":
    movmax_driver()