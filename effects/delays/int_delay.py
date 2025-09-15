#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"


""" int_delay.py: Basic integer delay line """


# Python dependencies
import numpy as np
import matplotlib.pyplot as plt

class IntDelay:
    def __init__(self, delay_samples: int):
        self.delay_samples = delay_samples
        self.buffer: list = [0] * delay_samples
        self.w_idx = 0

    def clear(self):
        self.buffer = [0] * self.delay_samples
        self.w_idx = 0

    def get_delay_samples(self):
        return self.delay_samples

    def process(self, xn):
        # Read buffer
        r_idx: int = self.w_idx % self.delay_samples
        yn: float = self.buffer[r_idx]

        # Write buffer
        self.buffer[self.w_idx] = xn
        self.w_idx = (self.w_idx + 1) % self.delay_samples

        return yn

if __name__ == "__main__":
    # Basic example
    int_delay = IntDelay(delay_samples=1000)

    fs = 48000
    ts = np.linspace(0, 1, num=fs)
    x = np.sin(2*np.pi*ts) # 1 Hz
    x_pad = np.pad(x, pad_width=(0, int_delay.get_delay_samples()), mode='constant', constant_values=0)

    y = np.zeros(len(x_pad) + int_delay.get_delay_samples())
    for n in range(len(x_pad)):
        y[n] = int_delay.process(x_pad[n])

    plt.plot(x_pad)
    plt.plot(y)
    plt.show()