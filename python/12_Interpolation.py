
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.fft import fft, ifft, fftfreq
from scipy.io import wavfile
import soundfile as sf

OUT = os.path.join(os.path.dirname(__file__), "..", "output")
INPUT = os.path.join(os.path.dirname(__file__), "..", "input")

os.makedirs(OUT, exist_ok=True)


# Experiment 12: Interpolation
# Original implementation from the DSP experiment notebook.

def exp12():
    t = np.arange(0, 1.01, 0.01)
    x = np.sin(2*np.pi*5*t)
    L = 3

    decimated = signal.decimate(x, L)
    interpolated = signal.resample_poly(decimated, L, 1)

    td = np.arange(len(decimated))*0.03
    ti = np.arange(len(interpolated))*0.01

    fig, ax = plt.subplots(3, 1, figsize=(9, 6))
    ax[0].plot(t, x)
    ax[0].set_title("Original signal")
    ax[1].stem(td, decimated)
    ax[1].set_title("Decimated signal")
    ax[2].plot(ti, interpolated)
    ax[2].set_title("Interpolated signal")

    for a in ax:
        a.grid(True)
        a.set_xlabel("Time (s)")
    fig.tight_layout()

    return [save_plot(fig, "exp12")], (
        f"Original samples = {len(x)}\n"
        f"Decimated samples = {len(decimated)}\n"
        f"Interpolated samples = {len(interpolated)}\n"
        f"Interpolation factor = {L}\n"
        f"Interpolated sequence = {np.round(interpolated, 4)}"
    )


if __name__ == '__main__':
    exp12()
