
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


# Experiment 2: Verification of Parseval's Theorem
# Original implementation from the DSP experiment notebook.

def exp2():
    x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
    N = len(x)
    X = fft(x)

    lhs = np.sum(np.abs(x)**2)
    rhs = np.sum(np.abs(X)**2)/N

    fig, ax = plt.subplots(1, 2, figsize=(9, 4))
    ax[0].stem(np.arange(N), x)
    ax[0].set_title("Input sequence")
    ax[1].stem(np.arange(N), np.abs(X))
    ax[1].set_title("DFT magnitude")

    for a in ax:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp2")], (
        f"Input: {x}\n"
        f"DFT: {np.round(X, 3)}\n"
        f"Time-domain energy: {lhs:.4f}\n"
        f"Frequency-domain energy: {rhs:.4f}\n"
        f"Parseval verified: {np.isclose(lhs, rhs)}"
    )


if __name__ == '__main__':
    exp2()
