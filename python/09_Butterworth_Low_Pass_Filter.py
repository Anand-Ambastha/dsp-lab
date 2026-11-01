
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


# Experiment 9: Butterworth Low-Pass Filter
# Original implementation from the DSP experiment notebook.

def exp9():
    Ap, As = 1, 40
    Fpass, Fstop, Fs = 100, 150, 1000

    Wp = Fpass/(Fs/2)
    Ws = Fstop/(Fs/2)

    order, Wn = signal.buttord(Wp, Ws, Ap, As)
    b, a = signal.butter(order, Wn, btype="low")

    w, H = signal.freqz(b, a, worN=8192, fs=Fs)
    db = 20*np.log10(np.maximum(np.abs(H), 1e-10))

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(w, db)
    ax.axvline(Fpass, linestyle="--", label="Passband edge")
    ax.axvline(Fstop, linestyle="--", label="Stopband edge")
    ax.set_xlim(0, Fs/2)
    ax.set_ylim(-100, 5)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title("Butterworth Low-Pass Filter")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    return [save_plot(fig, "exp9")], (
        f"Filter order = {order}\n"
        f"Critical frequency = {Wn:.6f}\n"
        f"Numerator coefficients = {np.round(b, 6)}\n"
        f"Denominator coefficients = {np.round(a, 6)}"
    )


if __name__ == '__main__':
    exp9()
