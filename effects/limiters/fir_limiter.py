#! /usr/bin/env python

__author__ = "Zachary Miller"
__copyright__ = "Copyright 2025, Miller Labs DSP"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "zacharyianmiller1@gmail.com"
__date__ = "2025-09-15"


""" fir_limiter.py: Basic integer delay line """


# Python dependencies
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Custom functions
from filters.envelopes.moving_minimum import MovMin
from filters.smoothing.moving_average import MovAvg
from effects.delays.int_delay import IntDelay
from filters.smoothing.fir_exp_rel import FIRExpRelease

class FIRLimiter:
    def __init__(self, fs, limit, attack_ms):
        self.fs = fs
        self.limit = limit
        self.attack_ms = attack_ms
        self.attack_samples: int = 0.001*attack_ms*fs
        self.moving_minimum = MovMin(self.attack_samples)
        self.moving_average = MovAvg(self.attack_samples, 8)
        self.intd = IntDelay(int(self.attack_samples))

    def calculate_gain(self, xn: float):
        max_gain: float = 1.0
        if np.fabs(xn) > self.limit:
            max_gain = self.limit / np.fabs(xn)

        # Invert maximum gain to avoid moving average's ramp from zero
        yn = np.abs(self.moving_minimum.process(max_gain) - 1)
        return -self.moving_average.process(yn) + 1, max_gain

    def process(self, xn) -> float:
        gr, mg = self.calculate_gain(xn)
        return xn*gr

if __name__ == "__main__":
    x, sr = sf.read('../../testing/audio/SnareTop.wav')
    x = x[0:50000,1] # mono
    limiter = FIRLimiter(sr, 0.25, 30)
    gr_env = np.zeros(len(x))
    mg_env = np.zeros(len(x))
    x_ltc = np.zeros(len(x))
    y = np.zeros(len(x))
    for n in range(len(x)):
        gr_env[n], mg_env[n] = limiter.calculate_gain(x[n])
        y[n] = limiter.process(x[n])

    plt.plot(mg_env, c='black')
    plt.plot(gr_env, c='yellow')
    plt.xlim(0, len(x))
    plt.ylim(0.0, 1.0)
    plt.xlabel('Time [samples]')
    plt.ylabel('GR [linear, unipolar]')
    plt.title('FIR Limiter')
    plt.show()