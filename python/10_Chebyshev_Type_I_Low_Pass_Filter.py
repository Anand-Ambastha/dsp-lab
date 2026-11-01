
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


# Experiment 10: Chebyshev Type-I Low-Pass Filter
# Original implementation from the DSP experiment notebook.

def exp10():
    Ap, As = 1, 40
    Wpass, Wstop = 0.2, 0.707

    order, Wn = signal.cheb1ord(Wpass, Wstop, Ap, As)
    b, a = signal.cheby1(order, Ap, Wn, btype="low")

    w, H = signal.freqz(b, a, worN=8192)
    db = 20*np.log10(np.maximum(np.abs(H), 1e-10))

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(w/np.pi, db)
    ax.axvline(Wpass, linestyle="--", label="Passband edge")
    ax.axvline(Wstop, linestyle="--", label="Stopband edge")
    ax.set_xlim(0, 1)
    ax.set_ylim(-100, 5)
    ax.set_xlabel("Normalized frequency (×π rad/sample)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title("Chebyshev Type-I Low-Pass Filter")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    return [save_plot(fig, "exp10")], (
        f"Filter order = {order}\n"
        f"Critical frequency = {Wn:.6f}\n"
        f"Numerator coefficients = {np.round(b, 6)}\n"
        f"Denominator coefficients = {np.round(a, 6)}\n"
        "Assumption: Wpass=0.2 and Wstop=0.707."
    )


if __name__ == '__main__':
    exp10()
