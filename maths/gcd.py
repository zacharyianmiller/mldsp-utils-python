#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"

""" gcd.py: 

    Recursive function to find greatest common denominator (GCD)
    of an array of floats. This implementation is based on the 
    Euclidean algorithm.

"""


# Python dependencies
import numpy as np


def gcd(x1: float, x2: float) -> float:

    a = np.abs(x1)
    b = np.abs(x2)

    while x2 > 0.000001:
        remainder = np.mod(x1, x2)
        x1 = x2
        x2 = remainder

    return x1


def gcd_arr(arr: np.array):

    N = len(arr)
    # When array is 2+ values
    if len(arr) > 1:
        running_gcd = 0.0

        idx: int = 0
        running_gcd = gcd(arr[idx], arr[idx + 1])
        while idx < len(arr) - 1:
            if idx > 0:
                running_gcd = gcd(running_gcd, arr[idx])

            idx += 1

        return running_gcd

    # When array only has 1 value
    elif len(arr) == 1:
        return arr[0]

    # When array is empty
    else:
        assert False, 'Cannot compute GCD of empty array.'