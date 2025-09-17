#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-16"

""" iir_exp_smooth.py: 

    IIR (infinite impulse response) lowpass smoothing filter designed
    to handle simultaneous attack and release envelopes.

"""

# Python dependencies
import numpy as np
import sys

class IIRExpSmooth:
    def __init__(self, fs, ms):
        self.fs = fs
        self.alpha = np.exp(-2*np.pi*(1/fs)/(ms*0.001))
        self.y1: float = -100 # single-sample feedback

    def process(self, xn: float) -> float:
            xn = xn + self.alpha*(np.abs(self.y1 - xn))
            self.y1 = xn
            return xn