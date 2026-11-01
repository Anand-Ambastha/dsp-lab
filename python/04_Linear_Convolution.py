
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


# Experiment 4: Linear Convolution
# Original implementation from the DSP experiment notebook.

def exp4():
    x = np.array([1, 2, 0, 1])
    h = np.array([1, 5, 7, 3])
    y = np.convolve(x, h)

    n1 = np.arange(-2, 2)
    n2 = np.arange(-1, 3)
    ny = np.arange(-3, 4)

    fig, ax = plt.subplots(3, 1, figsize=(8, 6))
    ax[0].stem(n1, x)
    ax[0].set_title("x[n]")
    ax[1].stem(n2, h)
    ax[1].set_title("h[n]")
    ax[2].stem(ny, y)
    ax[2].set_title("Linear convolution")

    for a in ax:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp4")], (
        f"x[n] = {x}\n"
        f"h[n] = {h}\n"
        f"Linear convolution = {y}\n"
        f"Output index = {ny}"
    )


if __name__ == '__main__':
    exp4()
