#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-16"


""" peak_hold_smoothing.py: Basic integer delay line """


# Python dependencies
import numpy as np
import control as ct
import matplotlib.pyplot as plt
import soundfile as sf

# Custom functions
from filters.envelopes.moving_maximum import MovMax
from filters.smoothing.iir_exp_smooth import IIRExpSmooth


def main():
    x, fs = sf.read('../testing/audio/SnareTop.wav')
    x = x[25000:50000,1] # mono
    eps = 1e-12  # prevent log10(0)
    movmax: MovMax = MovMax(4096)
    iir_smooth: IIRExpSmooth = IIRExpSmooth(fs, 100)

    hold = np.zeros(len(x))
    smoothed = np.zeros(len(x))
    for n in range(len(x)):
        smoothed[n] = movmax.process(ct.mag2db(x[n]+eps))
        # smoothed[n] = iir_smooth.process(movmax.process(ct.mag2db(x[n]+eps)))

    plt.plot(ct.mag2db(x+eps))
    plt.plot(smoothed)
    plt.ylim(-20, 5)
    plt.show()

if __name__ == "__main__":
    main()