
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


# Experiment 14: Filtering of Audio Frequency Components
# Original implementation from the DSP experiment notebook.

def exp14():
    x, Fs, source = get_audio()

    N = min(2**20, len(x))
    N = 2**int(np.floor(np.log2(N)))
    x = x[:N]

    X = fft(x)
    f_all = fftfreq(N, 1/Fs)

    cutoff = 300
    X_filtered = X.copy()
    X_filtered[np.abs(f_all) < cutoff] = 0

    y = ifft(X_filtered).real

    t = np.arange(N)/Fs
    f = f_all[:N//2]

    fig, ax = plt.subplots(3, 1, figsize=(9, 7))
    ax[0].plot(t, x)
    ax[0].set_title("Original audio signal")

    ax[1].plot(f, np.abs(X[:N//2]), label="Original")
    ax[1].plot(f, np.abs(X_filtered[:N//2]), label="Filtered")
    ax[1].axvline(cutoff, linestyle="--", label="Cutoff")
    ax[1].set_xlim(0, Fs/2)
    ax[1].set_title("Frequency spectrum")
    ax[1].legend()

    ax[2].plot(t, y)
    ax[2].set_title("Filtered audio signal")

    for a in ax:
        a.grid(True)
    fig.tight_layout()

    sf.write(os.path.join(OUT, "filtered_ringtone.wav"), y, Fs)

    return [save_plot(fig, "exp14")], (
        f"Audio source: {source}\n"
        f"Sampling frequency: {Fs} Hz\n"
        f"Samples analysed: {N}\n"
        f"Filter: Frequency-domain high-pass filter\n"
        f"Cutoff frequency: {cutoff} Hz\n"
        f"Filtered audio saved as filtered_ringtone.wav"
    )


if __name__ == '__main__':
    exp14()
