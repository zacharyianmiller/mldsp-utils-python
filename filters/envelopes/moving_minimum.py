#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-15"

from filters.envelopes.moving_maximum import MovMax


""" moving_minimum.py: Extension of the moving maximum algorithm. """


class MovMin:
    def __init__(self, kernel_size):
        self.kernel_size = kernel_size
        self.moving_maximum = MovMax(kernel_size)

    def process(self, xn):
        return -self.moving_maximum.process(-xn)