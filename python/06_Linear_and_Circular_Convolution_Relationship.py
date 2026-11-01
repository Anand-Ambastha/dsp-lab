
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


# Experiment 6: Linear and Circular Convolution Relationship
# Original implementation from the DSP experiment notebook.

def exp6():
    x = np.array([1, 2, 0, 1])
    h = np.array([1, 5, 7, 3])

    linear = np.convolve(x, h)
    N = max(len(x), len(h))

    folded = np.zeros(N)
    for i, value in enumerate(linear):
        folded[i % N] += value

    M = len(x) + len(h) - 1
    xp = np.pad(x, (0, M-len(x)))
    hp = np.pad(h, (0, M-len(h)))

    circ = np.zeros(M)
    for n in range(M):
        for k in range(M):
            circ[n] += xp[k]*hp[(n-k) % M]

    fig, ax = plt.subplots(3, 1, figsize=(8, 6))
    ax[0].stem(np.arange(len(linear)), linear)
    ax[0].set_title("Linear convolution")
    ax[1].stem(np.arange(N), folded)
    ax[1].set_title("Circular convolution by folding")
    ax[2].stem(np.arange(M), circ)
    ax[2].set_title("Zero-padded circular convolution")

    for a in ax:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp6")], (
        f"Linear convolution = {linear}\n"
        f"Folded circular convolution = {folded}\n"
        f"Zero-padded circular convolution = {circ}\n"
        f"Zero-padded result equals linear convolution: {np.allclose(linear, circ)}"
    )


if __name__ == '__main__':
    exp6()
