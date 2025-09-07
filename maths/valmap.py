#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-25"

""" valmap.py: 

    Maps a number of its own specific bounds to a new set of bounds.
    This function comes with an array pseudo-overload function.

"""

import numpy as np


def valmap(x, x_min, x_max, target_min, target_max, decimal_precision: int = 9) -> float:
    delta_x = x_max - x_min
    delta_target = target_max - target_min

    # Handle error for magnitude-less vectors / arrays
    if delta_x == 0 or delta_target == 0:
        return 0

    scale = delta_target / delta_x
    offset = (-x_min * scale) + target_min
    fin = (x * scale) + offset
    calc_scale: int = np.pow(10, decimal_precision)
    return float(np.round(fin * calc_scale)) / float(calc_scale)


def valmap_norm(x, x_min, x_max) -> float:
    return (x - x_min) / (x_max - x_min)


def valmap_arr(x: np.array, x_min, x_max, target_min, target_max) -> np.array:
    N = x.shape[0]
    tmp = np.zeros(N)

    for n in range(N):
        tmp[n]: np.zeros(N) = valmap(x[n], x_min, x_max, target_min, target_max)

    return tmp