#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"

""" fir_exp_rel.py: 

    FIR (finite impulse response) smoothing filter for release
    envelopes modeling exponential decay.

"""

# Python dependencies
import numpy as np

class FIRExponentialRelease:
    def __init__(self, release_samples):
        self.release_slew = 1 / (release_samples + 1)
        self.yn = 1.0

    def step(self, xn: float) -> float:
        self.yn += (xn - self.yn) * self.release_slew
        self.yn = np.fmin(self.yn, xn)
        return self.yn