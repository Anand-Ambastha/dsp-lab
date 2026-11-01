
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


# Experiment 1: DFT and IDFT
# Original implementation from the DSP experiment notebook.

def exp1():
    x = np.array([1, 3, -1, -2], dtype=complex)
    N = len(x)

    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j*2*np.pi*k*n/N)

    X2 = np.array([1, 2-5j, -1, 2+5j])
    x2 = np.zeros(N, dtype=complex)

    for n in range(N):
        for k in range(N):
            x2[n] += X2[k] * np.exp(1j*2*np.pi*k*n/N)
        x2[n] /= N

    fig, ax = plt.subplots(2, 2, figsize=(9, 5))
    ax[0, 0].stem(np.arange(N), x.real)
    ax[0, 0].set_title("Input sequence")
    ax[0, 1].stem(np.arange(N), np.abs(X))
    ax[0, 1].set_title("DFT magnitude")
    ax[1, 0].stem(np.arange(N), np.abs(X2))
    ax[1, 0].set_title("IDFT input magnitude")
    ax[1, 1].stem(np.arange(N), x2.real)
    ax[1, 1].set_title("IDFT output")

    for a in ax.flat:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp1")], (
        f"Input sequence: {x}\n"
        f"DFT: {np.round(X, 4)}\n"
        f"IDFT input: {X2}\n"
        f"IDFT output: {np.round(x2, 4)}"
    )


if __name__ == '__main__':
    exp1()
