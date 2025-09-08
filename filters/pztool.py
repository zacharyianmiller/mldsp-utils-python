#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-07"

from maths.roots_as_complex import roots_as_complex

""" pztool.py: 

    A unit circle pole-zero plot for discrete filter design and implementation.

        - b: Feedback coefficients
            Found in the numerator and represents the filter's zeros
        - a: Feedforward coefficients
            Found in the denominator and represents the filter's poles

"""

# Python dependencies
import numpy as np
import matplotlib.pyplot as plt

# Custom functions
import maths.roots_as_complex


def pztool(b: np.array,
          a: np.array) -> int:

    # Find roots of numerator and denominator
    filter_zeros: np = np.roots(b)
    filter_poles = np.roots(a)

    # Account for FIR poles
    if filter_poles.size is 0:
        isFIR: bool = True
        filter_poles = np.zeros(b.shape[0] - 1, dtype=complex)

    # Plot base unit circle at origin
    theta = np.linspace(0, 2 * np.pi, 100)
    plt.subplots(figsize=(8, 8))
    plt.title('Pole-Zero Plot', fontsize=16, fontweight='bold')

    r = 1.0  # circle radius
    plt.plot(r * np.cos(theta), r * np.sin(theta), color='blue', linewidth=1, linestyle='dotted')
    lim_bounds = [-r - 0.1, r + 0.1]
    plt.xlabel('Real axis (Re)')
    plt.ylabel('Imaginary axis (Im)')
    plt.xlim(lim_bounds)
    plt.ylim(lim_bounds)

    for z in filter_zeros:
        plt.plot(z.real, z.imag, 'o', mfc='none', color='blue')

    for p in filter_poles:
        plt.plot(p.real, p.imag, 'x', color='blue')

    plt.show()

    return 0

if __name__ == "__main__":
    # IIR lowpass filter
    # b_arr = np.array([0.0976, 0.1952, 0.0976])
    # a_arr = np.array([1, -0.9429, 0.3334])

    # FIR lowpass filter
    b_arr = np.array([0.5, 0.5])
    a_arr = np.array([1])

    pztool(b_arr, a_arr)