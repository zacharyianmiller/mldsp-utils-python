#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-06"


"""     
    
    roots_as_complex.py: 
            
    When no complex values are present, this function 
    tacks on 0j to each array item.

"""


import numpy as np


def roots_as_complex(arr: np.array) -> np.array:
    # If complex values are present, compute roots like normal...
    if np.iscomplex(arr).any:
        return np.roots(arr)

    # Otherwise concatenate '0j' to our roots
    temp_roots: np.array = np.roots(arr)
    complex_roots: np.array = np.zeros(temp_roots.shape[0])
    for n in range(temp_roots.shape[0]):
        complex_roots[n] = complex(temp_roots[n], 0)

    return complex_roots