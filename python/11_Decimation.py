
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


# Experiment 11: Decimation
# Original implementation from the DSP experiment notebook.

def exp11():
    t = np.arange(0, 1.01, 0.01)
    x = np.sin(2*np.pi*5*t)
    D = 3

    y = signal.decimate(x, D)
    td = t[::D][:len(y)]

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(t, x, label="Original signal")
    ax.stem(td, y, linefmt="C1-", markerfmt="C1o",
            basefmt=" ", label="Decimated signal")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Decimation")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    return [save_plot(fig, "exp11")], (
        f"Original samples = {len(x)}\n"
        f"Decimation factor = {D}\n"
        f"Decimated samples = {len(y)}\n"
        f"Original sampling frequency = 100 Hz\n"
        f"New sampling frequency = {100/D:.4f} Hz\n"
        f"Decimated sequence = {np.round(y, 4)}"
    )


if __name__ == '__main__':
    exp11()
