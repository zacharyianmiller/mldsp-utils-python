#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"

""" freqz.py: 

    A Bode plot (frequency and phase response) representation of a 
    discrete-time filter (both IIR and FIR) given some filter coefficient
    arrays.
            
        - b: Feedback coefficients
            Found in the numerator and represents the filter's zeros
        - a: Feedforward coefficients
            Found in the denominator and represents the filter's poles
        - n: Frequency response resolution via length of input frequencies
            Defaults to a 1024-point frequency array
        
"""


# Python dependencies
import numpy as np
import matplotlib.pyplot as plt
from maths.gcd import gcd_arr

# Custom functions
from maths.gcd import gcd_arr
from maths.valmap import valmap_norm


def freqz(b: np.array,
          a: np.array,
          n: int = 1024,
          isPhaseRadians = False):

    # Factor out transfer function gains
    K_num = gcd_arr(b)
    K_den = gcd_arr(a)

    # Solve for poles and zeros (where z=0)
    zeros = np.roots(b)
    poles = np.roots(a)

    w = np.linspace(0, np.pi, n)
    ejw = np.exp(1j*w) # Euler's formula

    Hz = 1.0
    for z in zeros:
        Hz *= (ejw - z)

    for p in poles:
        Hz /= (ejw - p)

    # Scale axes
    w_norm = w / np.pi  # normalized pi rad/sample
    Hz *= K_num / K_den  # factored gains

    # Adjust phase
    theta = np.atan(Hz.imag / Hz.real)
    if not isPhaseRadians:
        theta *= (180 / np.pi)

    # Magnitude response plot
    plt.subplot(2, 1, 1)
    Hz_abs = np.sqrt(Hz.real**2 + Hz.imag**2)
    plt.plot(w_norm, 20*np.log10(np.abs(Hz)))

    plt.xlim([0, 1])
    plt.xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    plt.xlabel(r'Normalized Frequency ($\times \pi$ rad/sample)')
    plt.ylim([-60, 5])
    plt.ylabel('Magnitude [dB]')

    plt.subplots_adjust(hspace=0.6)
    plt.grid(True, linestyle='dashed', color='lightgrey')
    plt.title('Magnitude', fontweight='bold')

    # Phase response plot
    plt.subplot(2, 1, 2)
    plt.plot(w_norm, np.unwrap(theta))

    plt.xlim([0, 1])
    plt.xticks([0.0, 0.25, 0.5, 0.75, 1.0])
    plt.xlabel(r'Normalized Frequency ($\times \pi$ rad/sample)')
    plt.ylabel('Phase [radians]' if isPhaseRadians else 'Phase [degrees]')

    # Fit bounds of phase response
    lower_bound = theta[0:1].item()

    # Account for phase wrap at 180 degrees
    plt.grid(True, linestyle='dashed', color='lightgrey')
    plt.title('Phase', fontweight='bold')
    plt.show()

    # Print filter characteristics
    print('Filter plot successful.')
    print('b: {}'.format(b_arr))
    print('a: {}'.format(a_arr))

if __name__ == "__main__":
    # IIR lowpass filter
    # b_arr = np.array([0.0976, 0.1952, 0.0976])
    # a_arr = np.array([1, -0.9429, 0.3334])

    # FIR lowpass filter
    b_arr = np.array([0.5, 0.5])
    a_arr = np.array([1])

    freqz(b_arr, a_arr, 1024)