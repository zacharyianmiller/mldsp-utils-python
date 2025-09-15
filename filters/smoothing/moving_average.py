#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"


""" moving_average.py: 

    Windowed moving average filter based on a running
    cumulative sum via an integer delay line.

"""

# Python dependencies
import sys
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

class MovAvg:
    def __init__(self, kernel_size):
        self.kernel_size = kernel_size

    def process(self, xn):
        return xn
