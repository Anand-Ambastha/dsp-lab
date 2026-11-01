
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


# Experiment 5: Circular Convolution
# Original implementation from the DSP experiment notebook.

def exp5():
    x = np.array([1, 2, 0, 1])
    h = np.array([1, 5, 7, 3])
    N = max(len(x), len(h))

    y = np.zeros(N)
    for n in range(N):
        for k in range(N):
            y[n] += x[k]*h[(n-k) % N]

    fig, ax = plt.subplots(3, 1, figsize=(8, 6))
    ax[0].stem(np.arange(N), x)
    ax[0].set_title("x[n]")
    ax[1].stem(np.arange(N), h)
    ax[1].set_title("h[n]")
    ax[2].stem(np.arange(N), y)
    ax[2].set_title("Circular convolution")

    for a in ax:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp5")], (
        f"x[n] = {x}\n"
        f"h[n] = {h}\n"
        f"Circular convolution length = {N}\n"
        f"Result = {y}"
    )


if __name__ == '__main__':
    exp5()
