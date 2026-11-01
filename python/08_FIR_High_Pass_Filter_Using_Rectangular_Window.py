
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


# Experiment 8: FIR High-Pass Filter Using Rectangular Window
# Original implementation from the DSP experiment notebook.

def exp8():
    rp, rs = 0.05, 0.04
    fp, fs_edge, Fs = 1500, 2000, 9000

    num = -20*np.log10(np.sqrt(rp*rs))-13
    den = 14.6*(fs_edge-fp)/Fs
    order = int(np.ceil(num/den))
    if order % 2:
        order += 1

    b = signal.firwin(
        order+1, fp, window="boxcar",
        pass_zero=False, fs=Fs
    )

    w, H = signal.freqz(b, worN=8192, fs=Fs)
    db = 20*np.log10(np.maximum(np.abs(H), 1e-10))

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(w, db)
    ax.axvline(fp, linestyle="--", label="Passband edge")
    ax.axvline(fs_edge, linestyle="--", label="Stopband edge")
    ax.set_xlim(0, Fs/2)
    ax.set_ylim(-100, 5)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title("FIR High-Pass Filter - Rectangular Window")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    return [save_plot(fig, "exp8")], (
        f"Filter order = {order}\n"
        f"Number of coefficients = {len(b)}\n"
        f"Coefficients = {np.round(b, 6)}"
    )


if __name__ == '__main__':
    exp8()
