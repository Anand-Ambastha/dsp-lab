
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


# Experiment 13: Extraction and Plotting of Audio Frequency Components
# Original implementation from the DSP experiment notebook.

def exp13():
    x, Fs, source = get_audio()

    N = min(2**20, len(x))
    N = 2**int(np.floor(np.log2(N)))
    x = x[:N]

    X = fft(x)
    reconstructed = ifft(X).real

    f = fftfreq(N, 1/Fs)[:N//2]
    magnitude = 2/N*np.abs(X[:N//2])
    t = np.arange(N)/Fs

    fig, ax = plt.subplots(3, 1, figsize=(9, 7))
    ax[0].plot(t, x)
    ax[0].set_title("Original audio signal")
    ax[1].plot(f, magnitude)
    ax[1].set_title("FFT magnitude spectrum")
    ax[1].set_xlim(0, Fs/2)
    ax[2].plot(t, reconstructed)
    ax[2].set_title("Reconstructed signal using IFFT")

    for a in ax:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp13")], (
        f"Audio source: {source}\n"
        f"Sampling frequency: {Fs} Hz\n"
        f"Samples analysed: {N}\n"
        f"Duration: {N/Fs:.4f} seconds\n"
        f"Maximum reconstruction error: {np.max(np.abs(x-reconstructed)):.10f}"
    )


if __name__ == '__main__':
    exp13()
