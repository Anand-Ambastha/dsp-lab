
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


# Experiment 3: Circular Time Shifting and Time Reversal
# Original implementation from the DSP experiment notebook.

def exp3():
    x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
    N = len(x)
    n = np.arange(N)

    shifted = np.roll(x, 5)
    reversed_x = x[(-n) % N]

    Xs = fft(shifted)
    Xr = fft(reversed_x)

    fig, ax = plt.subplots(2, 2, figsize=(9, 5))
    ax[0, 0].stem(n, shifted)
    ax[0, 0].set_title("Circular time shift")
    ax[0, 1].stem(n, np.abs(Xs))
    ax[0, 1].set_title("Shifted DFT magnitude")
    ax[1, 0].stem(n, reversed_x)
    ax[1, 0].set_title("Circular time reversal")
    ax[1, 1].stem(n, np.abs(Xr))
    ax[1, 1].set_title("Reversed DFT magnitude")

    for a in ax.flat:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp3")], (
        f"Original sequence: {x}\n"
        f"Shifted sequence: {shifted}\n"
        f"Reversed sequence: {reversed_x}\n"
        f"DFT of shifted sequence: {np.round(Xs, 3)}\n"
        f"DFT of reversed sequence: {np.round(Xr, 3)}"
    )


if __name__ == '__main__':
    exp3()
