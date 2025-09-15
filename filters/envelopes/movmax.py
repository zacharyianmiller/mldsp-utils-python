#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"


""" movmax.py: 

    Two-stack implementation of a moving maximum (peak-hold) filter
    for windowed peak detection. This algorithm compares the maximums
    of each array where the 'front' array manages the maximum value of
    the input window and the 'back' array manages the previous history 
    via a reverse cumulative maximum calculation done only when the input 
    window is filled.

"""

# Python dependencies
import sys
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


def movmax_driver(selection: str):

    # Basic example
    if selection == "1":
        mov_max = MovMax(kernel_size=5)

        x = np.random.rand(100)
        y: list = [0] * len(x)
        for n in range(len(x)):
            y[n] = mov_max.process(x[n])

        # Format x-axis
        plt.plot(x)
        plt.xlabel('Time [samples]')

        # Format y-axis
        plt.plot(y, color='r', linestyle='--')
        plt.ylim([0.0, 1.025])
        plt.ylabel('Normalized value [unipolar]')
        plt.title('Moving Maximum Filter', fontsize=12, fontweight='bold')
        plt.show()

    # Audio example
    elif selection == "2":
        mov_max = MovMax(kernel_size=4096)

        x, fs = sf.read("../../testing/audio/SnareTop.wav")
        x = np.abs(x[0:int(len(x)/2)-4000,1]) / np.max(np.abs(x)) # mono, normalized
        y: list = [0] * x.shape[0]
        for n in range(x.shape[0]):
            y[n] = mov_max.process(x[n])

        # Format x-axis
        plt.plot(x)
        plt.xlabel('Time [samples]')
        ax = plt.gca()
        ticks = ax.get_xticks().tolist()
        ax.set_xticks(ticks)
        ax.set_xticklabels(['0' if x == 0 else '{:}k'.format(int(0.001 * x)) for x in ticks])

        # Format y-axis
        plt.plot(y, color='r', linestyle='--')
        plt.ylim([0.0, 1.025])
        plt.ylabel('Normalized value [unipolar]')
        plt.title('Moving Maximum Filter', fontsize=12, fontweight='bold')
        plt.show()

    else:
        print("Invalid selection.")

if __name__ == "__main__":
    print("Choose example type to display:")
    print("1. Normalized random values")
    print("2. Mono audio signal")
    movmax_driver(input("Selection: "))