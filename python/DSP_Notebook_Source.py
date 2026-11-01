# NOTEBOOK CELL 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, windows
import math

# Clear previous plots
plt.close('all')

# Input parameters
rp = float(input("Enter the passband ripple: "))
rs = float(input("Enter the stopband ripple: "))
fp = float(input("Enter the passband frequency: "))
fs = float(input("Enter the stopband frequency: "))
f = float(input("Enter the sampling frequency: "))

# Normalized frequencies
wp = 2 * fp / f
ws = 2 * fs / f

# Calculate filter order
num = -20 * np.log10(np.sqrt(rp * rs)) - 13
dem = 14.6 * (fs - fp) / f

n = math.ceil(num / dem)

n1 = n + 1

# Ensure even filter order
if n % 2 != 0:
    n = n - 1

# Rectangular window
y = windows.boxcar(n1)

# Design Low-Pass FIR filter
b = firwin(n + 1, fp, window='boxcar', fs=f)

# Frequency response
h, o = freqz(b, 1, worN=256)

m = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot frequency response
plt.figure(figsize=(8, 5))
plt.plot(o / np.pi, m)

plt.ylabel('Gain in dB')
plt.xlabel('Normalised Frequency')
plt.title('Low-Pass FIR Filter using Rectangular Window')
plt.grid(True)

plt.tight_layout()
plt.show()

print("Filter Order:", n)
print("Filter Coefficients:\n", b)

# NOTEBOOK CELL 2

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz, windows
import math

# Clear previous plots
plt.close('all')

# Input parameters
rp = float(input("Enter the passband ripple: "))
rs = float(input("Enter the stopband ripple: "))
fp = float(input("Enter the passband frequency: "))
fs = float(input("Enter the stopband frequency: "))
f = float(input("Enter the sampling frequency: "))

# Normalized frequencies
wp = 2 * fp / f
ws = 2 * fs / f

# Calculate filter order
num = -20 * np.log10(np.sqrt(rp * rs)) - 13
dem = 14.6 * (fs - fp) / f

n = math.ceil(num / dem)

n1 = n + 1

# Ensure even filter order
if n % 2 != 0:
    n = n - 1

# Rectangular window
y = windows.boxcar(n1)

# Design High-Pass FIR filter
b = firwin(n + 1, fp, window='boxcar',
           pass_zero=False, fs=f)

# Frequency response
h, o = freqz(b, 1, worN=256)

m = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot frequency response
plt.figure(figsize=(8, 5))
plt.plot(o / np.pi, m)

plt.ylabel('Gain in dB')
plt.xlabel('Normalised Frequency')
plt.title('High-Pass FIR Filter using Rectangular Window')
plt.grid(True)

plt.tight_layout()
plt.show()

print("Filter Order:", n)
print("Filter Coefficients:\n", b)

# NOTEBOOK CELL 3

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
import math

# Input Parameters
rp = 0.05
rs = 0.04
fp = 1200
fs = 2000
f = 9000

print("OBJECTIVE 7: LOW PASS FIR FILTER")
print("--------------------------------")
print("Passband Ripple:", rp)
print("Stopband Ripple:", rs)
print("Passband Frequency:", fp, "Hz")
print("Stopband Frequency:", fs, "Hz")
print("Sampling Frequency:", f, "Hz")

# Normalized frequencies
wp = 2 * fp / f
ws = 2 * fs / f

# Calculate filter order
num = -20 * np.log10(np.sqrt(rp * rs)) - 13
dem = 14.6 * (fs - fp) / f

n = math.ceil(num / dem)

# Make filter order even
if n % 2 != 0:
    n -= 1

print("\nCalculated Filter Order:", n)

# Design Low Pass FIR Filter using Rectangular Window
b = firwin(n + 1, fp, window='boxcar', fs=f)

print("\nFilter Coefficients:")
print(b)

# Calculate frequency response
h, w = freqz(b, worN=4096, fs=f)

m = 20 * np.log10(np.maximum(np.abs(h), 1e-8))

# Plot frequency response
plt.figure(figsize=(11, 6))

plt.plot(w, m, linewidth=1.8, label='LPF Response')

plt.axvline(fp, color='green', linestyle='--',
            label='Passband Edge (1200 Hz)')

plt.axvline(fs, color='red', linestyle='--',
            label='Stopband Edge (2000 Hz)')

plt.title('Low-Pass FIR Filter using Rectangular Window')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')

plt.xlim(0, f/2)
plt.ylim(-100, 5)

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# NOTEBOOK CELL 4

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Input parameters
rp = 0.05
rs = 0.04
fp = 1200
fs = 2000
f = 9000

# Calculate filter order
num = -20 * np.log10(np.sqrt(rp * rs)) - 13
dem = 14.6 * (fs - fp) / f

n = int(np.ceil(num / dem))

if n % 2 != 0:
    n += 1

print("Filter Order:", n)

# Low Pass FIR Filter
b = firwin(n + 1, fp, window='boxcar', fs=f)

# Frequency response
w, h = freqz(b, worN=8192, fs=f)

# Magnitude response
m = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(w, m, 'b', linewidth=2)

plt.title("Low Pass FIR Filter - Rectangular Window")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.xlim(0, f/2)
plt.ylim(-100, 10)

plt.xticks(np.arange(0, 4501, 500))
plt.grid(True, linestyle='--')

plt.axvline(fp, color='green', linestyle='--')
plt.axvline(fs, color='red', linestyle='--')

plt.show()

# NOTEBOOK CELL 5

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Input parameters
rp = 0.05
rs = 0.04
fp = 1500
fs = 2000
f = 9000

# Calculate filter order
num = -20 * np.log10(np.sqrt(rp * rs)) - 13
dem = 14.6 * (fs - fp) / f

n = int(np.ceil(num / dem))

if n % 2 != 0:
    n += 1

print("Filter Order:", n)

# High Pass FIR Filter
b = firwin(n + 1, fp, window='boxcar',
           pass_zero=False, fs=f)

# Frequency response
w, h = freqz(b, worN=8192, fs=f)

# Magnitude response
m = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(w, m, 'b', linewidth=2)

plt.title("High Pass FIR Filter - Rectangular Window")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.xlim(0, f/2)
plt.ylim(-100, 10)

plt.xticks(np.arange(0, 4501, 500))
plt.grid(True, linestyle='--')

plt.axvline(fp, color='green', linestyle='--')
plt.axvline(fs, color='red', linestyle='--')

plt.show()

# NOTEBOOK CELL 6

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import buttord, butter, freqz

# Input specifications
Ap = 1
As = 40
Fpass = 100
Fstop = 150
Fs = 1000

# Normalized frequencies
Wpass = Fpass / (Fs / 2)
Wstop = Fstop / (Fs / 2)

# Calculate Butterworth filter order
n, Wn = buttord(Wpass, Wstop, Ap, As)

# Design Low Pass Butterworth Filter
b, a = butter(n, Wn, btype='low')

print("Butterworth Filter Order:", n)
print("Numerator Coefficients:")
print(b)
print("Denominator Coefficients:")
print(a)

# Frequency response
w, h = freqz(b, a, worN=4096, fs=Fs)

magnitude = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot frequency response
plt.figure(figsize=(10, 6))
plt.plot(w, magnitude, linewidth=2)

plt.axvline(Fpass, color='green', linestyle='--',
            label='Passband Edge')
plt.axvline(Fstop, color='red', linestyle='--',
            label='Stopband Edge')

plt.title('LP IIR Butterworth Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')

plt.xlim(0, Fs/2)
plt.ylim(-100, 5)
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()

# NOTEBOOK CELL 7

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheb1ord, cheby1, freqz

# Input specifications
Ap = 1
As = 40
Wpass = 0.2
Wstop = 0.707

# Calculate Chebyshev Type-I filter order
n, Wn = cheb1ord(Wpass, Wstop, Ap, As)

# Design Low Pass Chebyshev Type-I Filter
b, a = cheby1(n, Ap, Wn, btype='low')

print("Chebyshev Type-I Filter Order:", n)
print("Numerator Coefficients:")
print(b)
print("Denominator Coefficients:")
print(a)

# Frequency response
w, h = freqz(b, a, worN=4096)

magnitude = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot frequency response
plt.figure(figsize=(10, 6))

plt.plot(w / np.pi, magnitude, linewidth=2)

plt.axvline(Wpass, color='green', linestyle='--',
            label='Passband Edge')
plt.axvline(Wstop, color='red', linestyle='--',
            label='Stopband Edge')

plt.title('LP IIR Chebyshev Type-I Filter')
plt.xlabel('Normalized Frequency (× π rad/sample)')
plt.ylabel('Magnitude (dB)')

plt.xlim(0, 1)
plt.ylim(-100, 5)

plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()

# NOTEBOOK CELL 8

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate

# Generate input signal
t = np.arange(0, 1.01, 0.01)
x = np.sin(2 * np.pi * 5 * t)

# Decimation factor
D = 3

# Perform decimation
y = decimate(x, D)

print("Original Signal Length:", len(x))
print("Decimated Signal Length:", len(y))

# Plot signals
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.stem(np.arange(len(x)), x)
plt.title('Original Input Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(np.arange(len(y)), y)
plt.title('Decimated Output Signal (D = 3)')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 9

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate, resample_poly

# Generate input signal
t = np.arange(0, 1.01, 0.01)
x = np.sin(2 * np.pi * 5 * t)

# Interpolation factor
L = 3

# First decimate the signal
y = decimate(x, L)

# Interpolate the decimated signal
y1 = resample_poly(y, L, 1)

print("Original Signal Length:", len(x))
print("Decimated Signal Length:", len(y))
print("Interpolated Signal Length:", len(y1))

# Plot signals
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(np.arange(len(x)), x)
plt.title('Original Input Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(np.arange(len(y)), y)
plt.title('Decimated Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(np.arange(len(y1)), y1)
plt.title('Interpolated Output Signal (L = 3)')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 10

import numpy as np
import matplotlib.pyplot as plt

# Input sequence
xn = np.array([1, 3, -1, -2], dtype=complex)

N = len(xn)
Xk = np.zeros(N, dtype=complex)

# Calculate DFT
for k in range(N):
    for n in range(N):
        Xk[k] += xn[n] * np.exp(-1j * 2*np.pi*n*k/N)

print("DFT of given sequence:")
print(Xk)

n = np.arange(N)

plt.figure(figsize=(9, 8))

plt.subplot(3, 1, 1)
plt.stem(n, xn.real)
plt.title("Input Sequence")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, np.abs(Xk))
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, np.angle(Xk))
plt.title("Phase Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Phase (Radians)")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 11

import numpy as np
import matplotlib.pyplot as plt

# Input sequence
xn = np.array([1, 3, -1, -2], dtype=complex)

N = len(xn)
Xk = np.zeros(N, dtype=complex)

# Calculate DFT
for k in range(N):
    for n in range(N):
        Xk[k] += xn[n] * np.exp(-1j * 2*np.pi*n*k/N)

print("DFT of given sequence:")
print(Xk)

n = np.arange(N)

plt.figure(figsize=(9, 8))

plt.subplot(3, 1, 1)
plt.stem(n, xn.real)
plt.title("Input Sequence")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, np.abs(Xk))
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, np.angle(Xk))
plt.title("Phase Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Phase (Radians)")
plt.grid(True)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Input DFT sequence
Xk = np.array([1, 2-5j, -1, 2+5j])

N = len(Xk)
xn = np.zeros(N, dtype=complex)

# Calculate IDFT
for n in range(N):
    for k in range(N):
        xn[n] += Xk[k] * np.exp(1j*2*np.pi*n*k/N)

xn = xn / N

print("IDFT of given sequence:")
print(np.round(xn.real, 4))

n = np.arange(N)

plt.figure(figsize=(9, 8))

plt.subplot(3, 1, 1)
plt.stem(n, np.abs(Xk))
plt.title("Input DFT Sequence")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, xn.real)
plt.title("IDFT Magnitude / Reconstructed Sequence")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, np.angle(xn))
plt.title("Phase Spectrum")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 12

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])

N = len(x)
n = np.arange(N)

X = np.fft.fft(x)

# Parseval's theorem
LHS = np.sum(np.abs(x)**2)
RHS = np.sum(np.abs(X)**2) / N

print("LHS =", LHS)
print("RHS =", RHS)

print("Parseval's Theorem Verified:", np.isclose(LHS, RHS))

plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.stem(n, np.abs(x))
plt.title("Magnitude of Input")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, np.abs(X))
plt.title("Magnitude of DFT")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.bar(["LHS"], [LHS])
plt.title("Energy in Time Domain")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.bar(["RHS"], [RHS])
plt.title("Energy in Frequency Domain")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 13

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])

N = len(x)
n = np.arange(N)

# Circular shift
y = np.roll(x, 5)

XF = np.fft.fft(x)
YF = np.fft.fft(y)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.stem(n, np.abs(XF))
plt.title("Magnitude of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, np.abs(YF))
plt.title("Magnitude of Shifted DFT")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.stem(n, np.angle(XF))
plt.title("Phase of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.stem(n, np.angle(YF))
plt.title("Phase of Shifted DFT")
plt.grid(True)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])

N = len(x)
n = np.arange(N)

# Time reversal
y = x[::-1]

XF = np.fft.fft(x)
YF = np.fft.fft(y)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.stem(n, np.abs(XF))
plt.title("Magnitude of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, np.abs(YF))
plt.title("Magnitude of Reversed DFT")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.stem(n, np.angle(XF))
plt.title("Phase of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.stem(n, np.angle(YF))
plt.title("Phase of Reversed DFT")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 14

import numpy as np
import matplotlib.pyplot as plt

# Input sequence
xn = np.array([1, 3, -1, -2], dtype=complex)

N = len(xn)
Xk = np.zeros(N, dtype=complex)

# Calculate DFT
for k in range(N):
    for n in range(N):
        Xk[k] += xn[n] * np.exp(-1j * 2*np.pi*n*k/N)

print("DFT of given sequence:")
print(Xk)

n = np.arange(N)

plt.figure(figsize=(9, 8))

plt.subplot(3, 1, 1)
plt.stem(n, xn.real)
plt.title("Input Sequence")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, np.abs(Xk))
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, np.angle(Xk))
plt.title("Phase Spectrum")
plt.xlabel("Frequency Index")
plt.ylabel("Phase (Radians)")
plt.grid(True)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Input DFT sequence
Xk = np.array([1, 2-5j, -1, 2+5j])

N = len(Xk)
xn = np.zeros(N, dtype=complex)

# Calculate IDFT
for n in range(N):
    for k in range(N):
        xn[n] += Xk[k] * np.exp(1j*2*np.pi*n*k/N)

xn = xn / N

print("IDFT of given sequence:")
print(np.round(xn.real, 4))

n = np.arange(N)

plt.figure(figsize=(9, 8))

plt.subplot(3, 1, 1)
plt.stem(n, np.abs(Xk))
plt.title("Input DFT Sequence")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, xn.real)
plt.title("IDFT Magnitude / Reconstructed Sequence")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, np.angle(xn))
plt.title("Phase Spectrum")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 15

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])

N = len(x)
n = np.arange(N)

X = np.fft.fft(x)

# Parseval's theorem
LHS = np.sum(np.abs(x)**2)
RHS = np.sum(np.abs(X)**2) / N

print("LHS =", LHS)
print("RHS =", RHS)

print("Parseval's Theorem Verified:", np.isclose(LHS, RHS))

plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.stem(n, np.abs(x))
plt.title("Magnitude of Input")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, np.abs(X))
plt.title("Magnitude of DFT")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.bar(["LHS"], [LHS])
plt.title("Energy in Time Domain")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.bar(["RHS"], [RHS])
plt.title("Energy in Frequency Domain")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 16

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])

N = len(x)
n = np.arange(N)

# Circular shift
y = np.roll(x, 5)

XF = np.fft.fft(x)
YF = np.fft.fft(y)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.stem(n, np.abs(XF))
plt.title("Magnitude of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, np.abs(YF))
plt.title("Magnitude of Shifted DFT")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.stem(n, np.angle(XF))
plt.title("Phase of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.stem(n, np.angle(YF))
plt.title("Phase of Shifted DFT")
plt.grid(True)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])

N = len(x)
n = np.arange(N)

# Time reversal
y = x[::-1]

XF = np.fft.fft(x)
YF = np.fft.fft(y)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.stem(n, np.abs(XF))
plt.title("Magnitude of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, np.abs(YF))
plt.title("Magnitude of Reversed DFT")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.stem(n, np.angle(XF))
plt.title("Phase of Original DFT")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.stem(n, np.angle(YF))
plt.title("Phase of Reversed DFT")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 17

import numpy as np
import matplotlib.pyplot as plt

# Input sequences
xn = np.array([1, 2, 0, 1])
hn = np.array([1, 5, 7, 3])

# Time indices
n1 = np.arange(-2, 2)
n2 = np.arange(-1, 3)

# Linear convolution
y = np.convolve(xn, hn)

ny = np.arange(n1[0] + n2[0],
               n1[-1] + n2[-1] + 1)

print("Linear Convolution:")
print(y)

plt.figure(figsize=(9, 8))

plt.subplot(3, 1, 1)
plt.stem(n1, xn)
plt.title("First Input Sequence")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n2, hn)
plt.title("Second Input Sequence")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(ny, y)
plt.title("Linear Convolution Output")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 18

import numpy as np
import matplotlib.pyplot as plt

# Input sequences
xn = np.array([1, 2, 0, 1])
hn = np.array([1, 5, 7, 3])

N = max(len(xn), len(hn))

# Zero padding
xn = np.pad(xn, (0, N-len(xn)))
hn = np.pad(hn, (0, N-len(hn)))

y = np.zeros(N)

# Circular convolution
for i in range(N):
    for j in range(N):
        k = (i-j) % N
        y[i] += xn[j] * hn[k]

print("Circular Convolution:")
print(y)

n = np.arange(N)

plt.figure(figsize=(9, 8))

plt.subplot(3, 1, 1)
plt.stem(n, xn)
plt.title("First Input Sequence")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, hn)
plt.title("Second Input Sequence")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, y)
plt.title("Circular Convolution Output")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 19

import numpy as np
import matplotlib.pyplot as plt

xn = np.array([1, 2, 0, 1])
hn = np.array([1, 5, 7, 3])

N = max(len(xn), len(hn))

# Linear convolution
linear = np.convolve(xn, hn)

# Convert linear convolution to circular convolution
circular = np.zeros(N)

for i in range(N):
    circular[i] = sum(
        linear[j]
        for j in range(len(linear))
        if j % N == i
    )

print("Circular Convolution using Linear Convolution:")
print(circular)

plt.figure(figsize=(9, 7))

plt.subplot(3, 1, 1)
plt.stem(xn)
plt.title("First Input Sequence")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(hn)
plt.title("Second Input Sequence")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(circular)
plt.title("Circular Convolution Output")
plt.grid(True)

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

xn = np.array([1, 2, 0, 1])
hn = np.array([1, 5, 7, 3])

# Required circular convolution length
N = len(xn) + len(hn) - 1

# Zero padding
x = np.pad(xn, (0, N-len(xn)))
h = np.pad(hn, (0, N-len(hn)))

# Circular convolution
y = np.zeros(N)

for n in range(N):
    for m in range(N):
        k = (n-m) % N
        y[n] += x[m] * h[k]

print("Linear Convolution using Circular Convolution:")
print(y)

plt.figure(figsize=(9, 7))

plt.subplot(3, 1, 1)
plt.stem(x)
plt.title("Zero Padded First Sequence")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(h)
plt.title("Zero Padded Second Sequence")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(y)
plt.title("Linear Convolution Output")
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 20

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Input parameters
rp = 0.05
rs = 0.04
fp = 1200
fs = 2000
f = 9000

# Calculate filter order
num = -20 * np.log10(np.sqrt(rp * rs)) - 13
dem = 14.6 * (fs - fp) / f

n = int(np.ceil(num / dem))

if n % 2 != 0:
    n += 1

print("Filter Order:", n)

# Low Pass FIR Filter
b = firwin(n + 1, fp, window='boxcar', fs=f)

# Frequency response
w, h = freqz(b, worN=8192, fs=f)

# Magnitude response
m = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(w, m, 'b', linewidth=2)

plt.title("Low Pass FIR Filter - Rectangular Window")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.xlim(0, f/2)
plt.ylim(-100, 10)

plt.xticks(np.arange(0, 4501, 500))
plt.grid(True, linestyle='--')

plt.axvline(fp, color='green', linestyle='--')
plt.axvline(fs, color='red', linestyle='--')

plt.show()

# NOTEBOOK CELL 21

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Input parameters
rp = 0.05
rs = 0.04
fp = 1500
fs = 2000
f = 9000

# Calculate filter order
num = -20 * np.log10(np.sqrt(rp * rs)) - 13
dem = 14.6 * (fs - fp) / f

n = int(np.ceil(num / dem))

if n % 2 != 0:
    n += 1

print("Filter Order:", n)

# High Pass FIR Filter
b = firwin(n + 1, fp, window='boxcar',
           pass_zero=False, fs=f)

# Frequency response
w, h = freqz(b, worN=8192, fs=f)

# Magnitude response
m = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(w, m, 'b', linewidth=2)

plt.title("High Pass FIR Filter - Rectangular Window")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")

plt.xlim(0, f/2)
plt.ylim(-100, 10)

plt.xticks(np.arange(0, 4501, 500))
plt.grid(True, linestyle='--')

plt.axvline(fp, color='green', linestyle='--')
plt.axvline(fs, color='red', linestyle='--')

plt.show()

# NOTEBOOK CELL 22

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import buttord, butter, freqz

# Input specifications
Ap = 1
As = 40
Fpass = 100
Fstop = 150
Fs = 1000

# Normalized frequencies
Wpass = Fpass / (Fs / 2)
Wstop = Fstop / (Fs / 2)

# Calculate Butterworth filter order
n, Wn = buttord(Wpass, Wstop, Ap, As)

# Design Low Pass Butterworth Filter
b, a = butter(n, Wn, btype='low')

print("Butterworth Filter Order:", n)
print("Numerator Coefficients:")
print(b)
print("Denominator Coefficients:")
print(a)

# Frequency response
w, h = freqz(b, a, worN=4096, fs=Fs)

magnitude = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot frequency response
plt.figure(figsize=(10, 6))
plt.plot(w, magnitude, linewidth=2)

plt.axvline(Fpass, color='green', linestyle='--',
            label='Passband Edge')
plt.axvline(Fstop, color='red', linestyle='--',
            label='Stopband Edge')

plt.title('LP IIR Butterworth Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')

plt.xlim(0, Fs/2)
plt.ylim(-100, 5)
plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()

# NOTEBOOK CELL 23

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheb1ord, cheby1, freqz

# Input specifications
Ap = 1
As = 40
Wpass = 0.2
Wstop = 0.707

# Calculate Chebyshev Type-I filter order
n, Wn = cheb1ord(Wpass, Wstop, Ap, As)

# Design Low Pass Chebyshev Type-I Filter
b, a = cheby1(n, Ap, Wn, btype='low')

print("Chebyshev Type-I Filter Order:", n)
print("Numerator Coefficients:")
print(b)
print("Denominator Coefficients:")
print(a)

# Frequency response
w, h = freqz(b, a, worN=4096)

magnitude = 20 * np.log10(np.maximum(np.abs(h), 1e-10))

# Plot frequency response
plt.figure(figsize=(10, 6))

plt.plot(w / np.pi, magnitude, linewidth=2)

plt.axvline(Wpass, color='green', linestyle='--',
            label='Passband Edge')
plt.axvline(Wstop, color='red', linestyle='--',
            label='Stopband Edge')

plt.title('LP IIR Chebyshev Type-I Filter')
plt.xlabel('Normalized Frequency (× π rad/sample)')
plt.ylabel('Magnitude (dB)')

plt.xlim(0, 1)
plt.ylim(-100, 5)

plt.grid(True, linestyle=':')
plt.legend()
plt.tight_layout()
plt.show()

# NOTEBOOK CELL 24

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate

# Generate input signal
t = np.arange(0, 1.01, 0.01)
x = np.sin(2 * np.pi * 5 * t)

# Decimation factor
D = 3

# Perform decimation
y = decimate(x, D)

print("Original Signal Length:", len(x))
print("Decimated Signal Length:", len(y))

# Plot signals
plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.stem(np.arange(len(x)), x)
plt.title('Original Input Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(np.arange(len(y)), y)
plt.title('Decimated Output Signal (D = 3)')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 25

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate, resample_poly

# Generate input signal
t = np.arange(0, 1.01, 0.01)
x = np.sin(2 * np.pi * 5 * t)

# Interpolation factor
L = 3

# First decimate the signal
y = decimate(x, L)

# Interpolate the decimated signal
y1 = resample_poly(y, L, 1)

print("Original Signal Length:", len(x))
print("Decimated Signal Length:", len(y))
print("Interpolated Signal Length:", len(y1))

# Plot signals
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(np.arange(len(x)), x)
plt.title('Original Input Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(np.arange(len(y)), y)
plt.title('Decimated Signal')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(np.arange(len(y1)), y1)
plt.title('Interpolated Output Signal (L = 3)')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 26

get_ipython().system('pip -q install numpy scipy matplotlib soundfile reportlab')

import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import soundfile as sf

from scipy.fft import fft, ifft, fftfreq
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Preformatted, Image
)
from google.colab import files

# AUDIO FILE
print("Upload ringtone.mp3, or skip to use a generated test signal.")
uploaded = files.upload()

audio_file = next(
    (name for name in uploaded
     if name.lower().endswith((".mp3", ".wav", ".flac", ".ogg"))),
    None
)

OUT = "/content/dsp_graphs"
os.makedirs(OUT, exist_ok=True)

experiments = []

def add_experiment(number, title, aim, matlab, function):
    experiments.append({
        "number": number,
        "title": title,
        "aim": aim,
        "matlab": matlab,
        "function": function
    })

def save_plot(fig, name):
    path = os.path.join(OUT, name + ".png")
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path

# ============================================================
# EXPERIMENT 1: DFT AND IDFT
# ============================================================

def exp1():
    x = np.array([1, 3, -1, -2], dtype=complex)
    N = len(x)

    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j*2*np.pi*k*n/N)

    X2 = np.array([1, 2-5j, -1, 2+5j])
    x2 = np.zeros(N, dtype=complex)

    for n in range(N):
        for k in range(N):
            x2[n] += X2[k] * np.exp(1j*2*np.pi*k*n/N)
        x2[n] /= N

    fig, ax = plt.subplots(2, 2, figsize=(9, 5))
    ax[0, 0].stem(np.arange(N), x.real)
    ax[0, 0].set_title("Input sequence")
    ax[0, 1].stem(np.arange(N), np.abs(X))
    ax[0, 1].set_title("DFT magnitude")
    ax[1, 0].stem(np.arange(N), np.abs(X2))
    ax[1, 0].set_title("IDFT input magnitude")
    ax[1, 1].stem(np.arange(N), x2.real)
    ax[1, 1].set_title("IDFT output")

    for a in ax.flat:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp1")], (
        f"Input sequence: {x}\n"
        f"DFT: {np.round(X, 4)}\n"
        f"IDFT input: {X2}\n"
        f"IDFT output: {np.round(x2, 4)}"
    )

matlab1 = r"""
clc; clear all; close all;

x = [1 3 -1 -2];
N = length(x);

for k = 0:N-1
    X(k+1) = 0;
    for n = 0:N-1
        X(k+1) = X(k+1) + x(n+1)*exp(-1i*2*pi*k*n/N);
    end
end

disp('DFT:');
disp(X);

X = [1 2-5i -1 2+5i];

for n = 0:N-1
    x(n+1) = 0;
    for k = 0:N-1
        x(n+1) = x(n+1) + X(k+1)*exp(1i*2*pi*k*n/N);
    end
    x(n+1) = x(n+1)/N;
end

disp('IDFT:');
disp(x);
"""

add_experiment(
    1, "DFT and IDFT",
    "To calculate the Discrete Fourier Transform and Inverse Discrete Fourier Transform of given sequences.",
    matlab1, exp1
)

# ============================================================
# EXPERIMENT 2: PARSEVAL'S THEOREM
# ============================================================

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

matlab2 = r"""
clc; clear all; close all;

x = [0 2 4 6 8 10 12 14 16];
N = length(x);

X = fft(x);

LHS = sum(abs(x).^2);
RHS = sum(abs(X).^2)/N;

disp('Time domain energy:');
disp(LHS);

disp('Frequency domain energy:');
disp(RHS);

if abs(LHS-RHS) < 1e-10
    disp('Parseval theorem verified');
end
"""

add_experiment(
    2, "Verification of Parseval's Theorem",
    "To verify Parseval's theorem by comparing the time-domain and frequency-domain energy of a sequence.",
    matlab2, exp2
)

# ============================================================
# EXPERIMENT 3: CIRCULAR SHIFT AND TIME REVERSAL
# ============================================================

def exp3():
    x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
    N = len(x)
    n = np.arange(N)

    shifted = np.roll(x, 5)
    reversed_x = x[(-n) % N]

    Xs = fft(shifted)
    Xr = fft(reversed_x)

    fig, ax = plt.subplots(2, 2, figsize=(9, 5))
    ax[0, 0].stem(n, shifted)
    ax[0, 0].set_title("Circular time shift")
    ax[0, 1].stem(n, np.abs(Xs))
    ax[0, 1].set_title("Shifted DFT magnitude")
    ax[1, 0].stem(n, reversed_x)
    ax[1, 0].set_title("Circular time reversal")
    ax[1, 1].stem(n, np.abs(Xr))
    ax[1, 1].set_title("Reversed DFT magnitude")

    for a in ax.flat:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp3")], (
        f"Original sequence: {x}\n"
        f"Shifted sequence: {shifted}\n"
        f"Reversed sequence: {reversed_x}\n"
        f"DFT of shifted sequence: {np.round(Xs, 3)}\n"
        f"DFT of reversed sequence: {np.round(Xr, 3)}"
    )

matlab3 = r"""
clc; clear all; close all;

x = [0 2 4 6 8 10 12 14 16];
N = length(x);

% Circular time shifting
y = circshift(x, [0 5]);
X = fft(y);

figure;
subplot(2,1,1);
stem(abs(X));
title('Magnitude of DFT after circular shift');

subplot(2,1,2);
stem(angle(X));
title('Phase of DFT after circular shift');

% Circular time reversal
y = x([1 N:-1:2]);
X = fft(y);

figure;
subplot(2,1,1);
stem(abs(X));
title('Magnitude of DFT after time reversal');

subplot(2,1,2);
stem(angle(X));
title('Phase of DFT after time reversal');
"""

add_experiment(
    3, "Circular Time Shifting and Time Reversal",
    "To study circular time shifting and time reversal of a discrete-time sequence and their effects on the DFT.",
    matlab3, exp3
)

# ============================================================
# EXPERIMENT 4: LINEAR CONVOLUTION
# ============================================================

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

matlab4 = r"""
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

n1 = -2:1;
n2 = -1:2;

y = conv(x,h);
n = -3:3;

subplot(3,1,1);
stem(n1,x);
title('Input x[n]');

subplot(3,1,2);
stem(n2,h);
title('Impulse response h[n]');

subplot(3,1,3);
stem(n,y);
title('Linear convolution');
"""

add_experiment(
    4, "Linear Convolution",
    "To calculate the linear convolution of two discrete-time sequences.",
    matlab4, exp4
)

# ============================================================
# EXPERIMENT 5: CIRCULAR CONVOLUTION
# ============================================================

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

matlab5 = r"""
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

N1 = length(x);
N2 = length(h);
N = max(N1,N2);

x = [x zeros(1,N-N1)];
h = [h zeros(1,N-N2)];

for n = 0:N-1
    y(n+1) = 0;
    for k = 0:N-1
        y(n+1) = y(n+1) + x(k+1)*h(mod(n-k,N)+1);
    end
end

disp('Circular convolution:');
disp(y);
stem(y);
"""

add_experiment(
    5, "Circular Convolution",
    "To calculate the circular convolution of two finite-length discrete-time sequences.",
    matlab5, exp5
)

# ============================================================
# EXPERIMENT 6: LINEAR AND CIRCULAR CONVOLUTION RELATION
# ============================================================

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

matlab6 = r"""
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

% Linear convolution
y = conv(x,h);

% Circular convolution by folding
N = max(length(x),length(h));
yc = zeros(1,N);

for k = 1:length(y)
    index = mod(k-1,N)+1;
    yc(index) = yc(index)+y(k);
end

% Linear convolution using circular convolution
M = length(x)+length(h)-1;
x1 = [x zeros(1,M-length(x))];
h1 = [h zeros(1,M-length(h))];

for n = 0:M-1
    z(n+1) = 0;
    for k = 0:M-1
        z(n+1) = z(n+1)+x1(k+1)*h1(mod(n-k,M)+1);
    end
end

disp('Linear convolution:');
disp(y);
disp('Circular convolution by folding:');
disp(yc);
disp('Zero-padded circular convolution:');
disp(z);
"""

add_experiment(
    6, "Linear and Circular Convolution Relationship",
    "To obtain circular convolution by folding linear convolution and to obtain linear convolution using zero-padded circular convolution.",
    matlab6, exp6
)

# ============================================================
# EXPERIMENT 7: FIR LOW-PASS FILTER
# ============================================================

def exp7():
    rp, rs = 0.05, 0.04
    fp, fs_edge, Fs = 1200, 2000, 9000

    num = -20*np.log10(np.sqrt(rp*rs))-13
    den = 14.6*(fs_edge-fp)/Fs
    order = int(np.ceil(num/den))
    if order % 2:
        order += 1

    b = signal.firwin(order+1, fp, window="boxcar", fs=Fs)
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
    ax.set_title("FIR Low-Pass Filter - Rectangular Window")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    return [save_plot(fig, "exp7")], (
        f"Filter order = {order}\n"
        f"Number of coefficients = {len(b)}\n"
        f"Coefficients = {np.round(b, 6)}"
    )

matlab7 = r"""
clc; clear all; close all;

rp = 0.05;
rs = 0.04;
fp = 1200;
fs = 2000;
f = 9000;

num = -20*log10(sqrt(rp*rs))-13;
dem = 14.6*(fs-fp)/f;
n = ceil(num/dem);

if mod(n,2) ~= 0
    n = n+1;
end

wp = 2*fp/f;
y = rectwin(n+1);
b = fir1(n,wp,y);

freqz(b,1,8192,f);
title('FIR Low Pass Filter using Rectangular Window');
"""

add_experiment(
    7, "FIR Low-Pass Filter Using Rectangular Window",
    "To design an FIR low-pass filter using a rectangular window and plot its frequency response.",
    matlab7, exp7
)

# ============================================================
# EXPERIMENT 8: FIR HIGH-PASS FILTER
# ============================================================

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

matlab8 = r"""
clc; clear all; close all;

rp = 0.05;
rs = 0.04;
fp = 1500;
fs = 2000;
f = 9000;

num = -20*log10(sqrt(rp*rs))-13;
dem = 14.6*(fs-fp)/f;
n = ceil(num/dem);

if mod(n,2) ~= 0
    n = n+1;
end

wp = 2*fp/f;
y = rectwin(n+1);
b = fir1(n,wp,'high',y);

freqz(b,1,8192,f);
title('FIR High Pass Filter using Rectangular Window');
"""

add_experiment(
    8, "FIR High-Pass Filter Using Rectangular Window",
    "To design an FIR high-pass filter using a rectangular window and plot its frequency response.",
    matlab8, exp8
)

# ============================================================
# EXPERIMENT 9: BUTTERWORTH LOW-PASS FILTER
# ============================================================

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

matlab9 = r"""
clc; clear all; close all;

Ap = 1;
Ast = 40;
Fpass = 100;
Fstop = 150;
Fs = 1000;

Wpass = 2*Fpass/Fs;
Wstop = 2*Fstop/Fs;

[n,Wn] = buttord(Wpass,Wstop,Ap,Ast);
[b,a] = butter(n,Wn,'low');

freqz(b,a,8192,Fs);
title('Butterworth Low Pass Filter');
"""

add_experiment(
    9, "Butterworth Low-Pass Filter",
    "To design a digital Butterworth low-pass filter according to the given passband and stopband specifications.",
    matlab9, exp9
)

# ============================================================
# EXPERIMENT 10: CHEBYSHEV TYPE-I LOW-PASS FILTER
# ============================================================

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

matlab10 = r"""
clc; clear all; close all;

delta1 = 1;
delta2 = 40;

% Assumed corrected low-pass frequency ordering
wp = 0.2;
ws = 0.707;

[n,Wn] = cheb1ord(wp,ws,delta1,delta2);
[b,a] = cheby1(n,delta1,Wn,'low');

freqz(b,a,8192);
title('Chebyshev Type-I Low Pass Filter');
"""

add_experiment(
    10, "Chebyshev Type-I Low-Pass Filter",
    "To design a digital Chebyshev Type-I low-pass filter and plot its frequency response.",
    matlab10, exp10
)

# ============================================================
# EXPERIMENT 11: DECIMATION
# ============================================================

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

matlab11 = r"""
clc; clear all; close all;

t = 0:0.01:1;
D = 3;

x = sin(2*pi*5*t);
y = decimate(x,D);

subplot(2,1,1);
plot(t,x);
title('Original Signal');

subplot(2,1,2);
stem(y);
title('Decimated Signal');
"""

add_experiment(
    11, "Decimation",
    "To reduce the sampling rate of a discrete-time signal by a factor of three.",
    matlab11, exp11
)

# ============================================================
# EXPERIMENT 12: INTERPOLATION
# ============================================================

def exp12():
    t = np.arange(0, 1.01, 0.01)
    x = np.sin(2*np.pi*5*t)
    L = 3

    decimated = signal.decimate(x, L)
    interpolated = signal.resample_poly(decimated, L, 1)

    td = np.arange(len(decimated))*0.03
    ti = np.arange(len(interpolated))*0.01

    fig, ax = plt.subplots(3, 1, figsize=(9, 6))
    ax[0].plot(t, x)
    ax[0].set_title("Original signal")
    ax[1].stem(td, decimated)
    ax[1].set_title("Decimated signal")
    ax[2].plot(ti, interpolated)
    ax[2].set_title("Interpolated signal")

    for a in ax:
        a.grid(True)
        a.set_xlabel("Time (s)")
    fig.tight_layout()

    return [save_plot(fig, "exp12")], (
        f"Original samples = {len(x)}\n"
        f"Decimated samples = {len(decimated)}\n"
        f"Interpolated samples = {len(interpolated)}\n"
        f"Interpolation factor = {L}\n"
        f"Interpolated sequence = {np.round(interpolated, 4)}"
    )

matlab12 = r"""
clc; clear all; close all;

t = 0:0.01:1;
d = 3;

x = sin(2*pi*5*t);

y = decimate(x,d);
y1 = interp(y,d);

subplot(3,1,1);
plot(x);
title('Original Signal');

subplot(3,1,2);
stem(y);
title('Decimated Signal');

subplot(3,1,3);
plot(y1);
title('Interpolated Signal');
"""

add_experiment(
    12, "Interpolation",
    "To increase the sampling rate of a decimated signal using interpolation.",
    matlab12, exp12
)

# ============================================================
# AUDIO INPUT
# ============================================================

def get_audio():
    if audio_file:
        x, Fs = sf.read(audio_file)
        if x.ndim > 1:
            x = np.mean(x, axis=1)
        return x.astype(float), Fs, audio_file

    Fs = 8000
    t = np.arange(0, 3, 1/Fs)
    x = (
        0.5*np.sin(2*np.pi*440*t)
        + 0.3*np.sin(2*np.pi*880*t)
        + 0.2*np.sin(2*np.pi*1500*t)
    )
    return x, Fs, "Generated test audio"

# ============================================================
# EXPERIMENT 13: AUDIO FFT AND IFFT
# ============================================================

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

matlab13 = r"""
clc; clear all; close all;

[s,fs] = audioread('ringtone.mp3');

N = 20;
s = s(2:1:2^N+1);

FFT_org_abs = fft(s);

subplot(3,1,1);
plot(s);
title('Original Audio Signal');

subplot(3,1,2);
stem(abs(FFT_org_abs));
title('Magnitude of FFT');

IFFT_org = ifft(FFT_org_abs);

subplot(3,1,3);
plot(IFFT_org);
title('Reconstructed Audio Signal');
"""

add_experiment(
    13, "Extraction and Plotting of Audio Frequency Components",
    "To calculate the FFT of an audio signal, plot its frequency components and reconstruct it using IFFT.",
    matlab13, exp13
)

# ============================================================
# EXPERIMENT 14: AUDIO FREQUENCY FILTERING
# ============================================================

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

matlab14 = r"""
clc; clear all; close all;

[s,fs] = audioread('ringtone.mp3');

N = 20;
s = s(2:1:2^N+1);

FFT_org_abs = abs(fftshift(fft(s)));
nvec = -2^(N-1):2^(N-1)-1;

FFT_Filtered = fftshift(fft(s));

% Remove frequency components around zero
FFT_Filtered(abs(nvec) < 2^(N-6)) = 0;

% The original MATLAB indexing for the next
% range is invalid/reversed and needs correction.

filtered_signal = ifft(ifftshift(FFT_Filtered));

subplot(3,1,1);
plot(s);
title('Original Audio');

subplot(3,1,2);
plot(abs(FFT_Filtered));
title('Filtered Spectrum');

subplot(3,1,3);
plot(real(filtered_signal));
title('Filtered Audio');
"""

add_experiment(
    14, "Filtering of Audio Frequency Components",
    "To remove selected frequency components from an audio signal using frequency-domain filtering.",
    matlab14, exp14
)

# ============================================================
# PDF GENERATION
# ============================================================

styles = getSampleStyleSheet()

heading = ParagraphStyle(
    "ExperimentHeading",
    parent=styles["Heading1"],
    fontSize=13,
    leading=16,
    textColor=colors.darkblue,
    spaceAfter=8
)

section = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontSize=10,
    leading=13,
    spaceBefore=6,
    spaceAfter=4
)

body = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontSize=9,
    leading=12,
    spaceAfter=5
)

code_style = ParagraphStyle(
    "Code",
    fontName="Courier",
    fontSize=6.2,
    leading=7.5
)

output_style = ParagraphStyle(
    "Output",
    fontName="Courier",
    fontSize=7,
    leading=9
)

story = []

for item in experiments:

    story.append(Paragraph(
        f"EXPERIMENT {item['number']}: {item['title']}",
        heading
    ))

    story.append(Paragraph("Aim", section))
    story.append(Paragraph(item["aim"], body))

    story.append(Paragraph("MATLAB Code", section))
    story.append(Preformatted(item["matlab"].strip(), code_style))

    story.append(Paragraph("Generated Output", section))

    try:
        graph_paths, result = item["function"]()

        story.append(Preformatted(str(result), output_style))

        for path in graph_paths:
            if os.path.exists(path):
                story.append(Spacer(1, 3*mm))
                img = Image(path)
                img._restrictSize(175*mm, 105*mm)
                story.append(img)
                story.append(Spacer(1, 3*mm))

    except Exception as error:
        story.append(Paragraph(
            f"Output generation error: {str(error)}",
            body
        ))

    story.append(PageBreak())

def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(
        A4[0]/2, 8*mm, f"Page {doc.page}"
    )
    canvas.restoreState()

PDF_PATH = "/content/DSP_Lab_Manual.pdf"

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A4,
    rightMargin=13*mm,
    leftMargin=13*mm,
    topMargin=12*mm,
    bottomMargin=15*mm
)

doc.build(
    story,
    onFirstPage=page_number,
    onLaterPages=page_number
)

print("PDF created:", PDF_PATH)
print("Experiments included:", len(experiments))

files.download(PDF_PATH)

# NOTEBOOK CELL 27

get_ipython().system('pip -q install numpy scipy matplotlib soundfile reportlab')

import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import soundfile as sf

from scipy.fft import fft, ifft, fftfreq
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Preformatted, Image
)
from google.colab import files

# AUDIO FILE
print("Upload ringtone.mp3, or skip to use a generated test signal.")
uploaded = files.upload()

audio_file = next(
    (name for name in uploaded
     if name.lower().endswith((".mp3", ".wav", ".flac", ".ogg"))),
    None
)

OUT = "/content/dsp_graphs"
os.makedirs(OUT, exist_ok=True)

experiments = []

def add_experiment(number, title, aim, matlab, function):
    experiments.append({
        "number": number,
        "title": title,
        "aim": aim,
        "matlab": matlab,
        "function": function
    })

def save_plot(fig, name):
    path = os.path.join(OUT, name + ".png")
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path

# ============================================================
# EXPERIMENT 1: DFT AND IDFT
# ============================================================

def exp1():
    x = np.array([1, 3, -1, -2], dtype=complex)
    N = len(x)

    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j*2*np.pi*k*n/N)

    X2 = np.array([1, 2-5j, -1, 2+5j])
    x2 = np.zeros(N, dtype=complex)

    for n in range(N):
        for k in range(N):
            x2[n] += X2[k] * np.exp(1j*2*np.pi*k*n/N)
        x2[n] /= N

    fig, ax = plt.subplots(2, 2, figsize=(9, 5))
    ax[0, 0].stem(np.arange(N), x.real)
    ax[0, 0].set_title("Input sequence")
    ax[0, 1].stem(np.arange(N), np.abs(X))
    ax[0, 1].set_title("DFT magnitude")
    ax[1, 0].stem(np.arange(N), np.abs(X2))
    ax[1, 0].set_title("IDFT input magnitude")
    ax[1, 1].stem(np.arange(N), x2.real)
    ax[1, 1].set_title("IDFT output")

    for a in ax.flat:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp1")], (
        f"Input sequence: {x}\n"
        f"DFT: {np.round(X, 4)}\n"
        f"IDFT input: {X2}\n"
        f"IDFT output: {np.round(x2, 4)}"
    )

matlab1 = r"""
clc; clear all; close all;

x = [1 3 -1 -2];
N = length(x);

for k = 0:N-1
    X(k+1) = 0;
    for n = 0:N-1
        X(k+1) = X(k+1) + x(n+1)*exp(-1i*2*pi*k*n/N);
    end
end

disp('DFT:');
disp(X);

X = [1 2-5i -1 2+5i];

for n = 0:N-1
    x(n+1) = 0;
    for k = 0:N-1
        x(n+1) = x(n+1) + X(k+1)*exp(1i*2*pi*k*n/N);
    end
    x(n+1) = x(n+1)/N;
end

disp('IDFT:');
disp(x);
"""

add_experiment(
    1, "DFT and IDFT",
    "To calculate the Discrete Fourier Transform and Inverse Discrete Fourier Transform of given sequences.",
    matlab1, exp1
)

# ============================================================
# EXPERIMENT 2: PARSEVAL'S THEOREM
# ============================================================

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

matlab2 = r"""
clc; clear all; close all;

x = [0 2 4 6 8 10 12 14 16];
N = length(x);

X = fft(x);

LHS = sum(abs(x).^2);
RHS = sum(abs(X).^2)/N;

disp('Time domain energy:');
disp(LHS);

disp('Frequency domain energy:');
disp(RHS);

if abs(LHS-RHS) < 1e-10
    disp('Parseval theorem verified');
end
"""

add_experiment(
    2, "Verification of Parseval's Theorem",
    "To verify Parseval's theorem by comparing the time-domain and frequency-domain energy of a sequence.",
    matlab2, exp2
)

# ============================================================
# EXPERIMENT 3: CIRCULAR SHIFT AND TIME REVERSAL
# ============================================================

def exp3():
    x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
    N = len(x)
    n = np.arange(N)

    shifted = np.roll(x, 5)
    reversed_x = x[(-n) % N]

    Xs = fft(shifted)
    Xr = fft(reversed_x)

    fig, ax = plt.subplots(2, 2, figsize=(9, 5))
    ax[0, 0].stem(n, shifted)
    ax[0, 0].set_title("Circular time shift")
    ax[0, 1].stem(n, np.abs(Xs))
    ax[0, 1].set_title("Shifted DFT magnitude")
    ax[1, 0].stem(n, reversed_x)
    ax[1, 0].set_title("Circular time reversal")
    ax[1, 1].stem(n, np.abs(Xr))
    ax[1, 1].set_title("Reversed DFT magnitude")

    for a in ax.flat:
        a.grid(True)
    fig.tight_layout()

    return [save_plot(fig, "exp3")], (
        f"Original sequence: {x}\n"
        f"Shifted sequence: {shifted}\n"
        f"Reversed sequence: {reversed_x}\n"
        f"DFT of shifted sequence: {np.round(Xs, 3)}\n"
        f"DFT of reversed sequence: {np.round(Xr, 3)}"
    )

matlab3 = r"""
clc; clear all; close all;

x = [0 2 4 6 8 10 12 14 16];
N = length(x);

% Circular time shifting
y = circshift(x, [0 5]);
X = fft(y);

figure;
subplot(2,1,1);
stem(abs(X));
title('Magnitude of DFT after circular shift');

subplot(2,1,2);
stem(angle(X));
title('Phase of DFT after circular shift');

% Circular time reversal
y = x([1 N:-1:2]);
X = fft(y);

figure;
subplot(2,1,1);
stem(abs(X));
title('Magnitude of DFT after time reversal');

subplot(2,1,2);
stem(angle(X));
title('Phase of DFT after time reversal');
"""

add_experiment(
    3, "Circular Time Shifting and Time Reversal",
    "To study circular time shifting and time reversal of a discrete-time sequence and their effects on the DFT.",
    matlab3, exp3
)

# ============================================================
# EXPERIMENT 4: LINEAR CONVOLUTION
# ============================================================

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

matlab4 = r"""
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

n1 = -2:1;
n2 = -1:2;

y = conv(x,h);
n = -3:3;

subplot(3,1,1);
stem(n1,x);
title('Input x[n]');

subplot(3,1,2);
stem(n2,h);
title('Impulse response h[n]');

subplot(3,1,3);
stem(n,y);
title('Linear convolution');
"""

add_experiment(
    4, "Linear Convolution",
    "To calculate the linear convolution of two discrete-time sequences.",
    matlab4, exp4
)

# ============================================================
# EXPERIMENT 5: CIRCULAR CONVOLUTION
# ============================================================

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

matlab5 = r"""
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

N1 = length(x);
N2 = length(h);
N = max(N1,N2);

x = [x zeros(1,N-N1)];
h = [h zeros(1,N-N2)];

for n = 0:N-1
    y(n+1) = 0;
    for k = 0:N-1
        y(n+1) = y(n+1) + x(k+1)*h(mod(n-k,N)+1);
    end
end

disp('Circular convolution:');
disp(y);
stem(y);
"""

add_experiment(
    5, "Circular Convolution",
    "To calculate the circular convolution of two finite-length discrete-time sequences.",
    matlab5, exp5
)

# ============================================================
# EXPERIMENT 6: LINEAR AND CIRCULAR CONVOLUTION RELATION
# ============================================================

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

matlab6 = r"""
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

% Linear convolution
y = conv(x,h);

% Circular convolution by folding
N = max(length(x),length(h));
yc = zeros(1,N);

for k = 1:length(y)
    index = mod(k-1,N)+1;
    yc(index) = yc(index)+y(k);
end

% Linear convolution using circular convolution
M = length(x)+length(h)-1;
x1 = [x zeros(1,M-length(x))];
h1 = [h zeros(1,M-length(h))];

for n = 0:M-1
    z(n+1) = 0;
    for k = 0:M-1
        z(n+1) = z(n+1)+x1(k+1)*h1(mod(n-k,M)+1);
    end
end

disp('Linear convolution:');
disp(y);
disp('Circular convolution by folding:');
disp(yc);
disp('Zero-padded circular convolution:');
disp(z);
"""

add_experiment(
    6, "Linear and Circular Convolution Relationship",
    "To obtain circular convolution by folding linear convolution and to obtain linear convolution using zero-padded circular convolution.",
    matlab6, exp6
)

# ============================================================
# EXPERIMENT 7: FIR LOW-PASS FILTER
# ============================================================

def exp7():
    rp, rs = 0.05, 0.04
    fp, fs_edge, Fs = 1200, 2000, 9000

    num = -20*np.log10(np.sqrt(rp*rs))-13
    den = 14.6*(fs_edge-fp)/Fs
    order = int(np.ceil(num/den))
    if order % 2:
        order += 1

    b = signal.firwin(order+1, fp, window="boxcar", fs=Fs)
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
    ax.set_title("FIR Low-Pass Filter - Rectangular Window")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    return [save_plot(fig, "exp7")], (
        f"Filter order = {order}\n"
        f"Number of coefficients = {len(b)}\n"
        f"Coefficients = {np.round(b, 6)}"
    )

matlab7 = r"""
clc; clear all; close all;

rp = 0.05;
rs = 0.04;
fp = 1200;
fs = 2000;
f = 9000;

num = -20*log10(sqrt(rp*rs))-13;
dem = 14.6*(fs-fp)/f;
n = ceil(num/dem);

if mod(n,2) ~= 0
    n = n+1;
end

wp = 2*fp/f;
y = rectwin(n+1);
b = fir1(n,wp,y);

freqz(b,1,8192,f);
title('FIR Low Pass Filter using Rectangular Window');
"""

add_experiment(
    7, "FIR Low-Pass Filter Using Rectangular Window",
    "To design an FIR low-pass filter using a rectangular window and plot its frequency response.",
    matlab7, exp7
)

# ============================================================
# EXPERIMENT 8: FIR HIGH-PASS FILTER
# ============================================================

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

matlab8 = r"""
clc; clear all; close all;

rp = 0.05;
rs = 0.04;
fp = 1500;
fs = 2000;
f = 9000;

num = -20*log10(sqrt(rp*rs))-13;
dem = 14.6*(fs-fp)/f;
n = ceil(num/dem);

if mod(n,2) ~= 0
    n = n+1;
end

wp = 2*fp/f;
y = rectwin(n+1);
b = fir1(n,wp,'high',y);

freqz(b,1,8192,f);
title('FIR High Pass Filter using Rectangular Window');
"""

add_experiment(
    8, "FIR High-Pass Filter Using Rectangular Window",
    "To design an FIR high-pass filter using a rectangular window and plot its frequency response.",
    matlab8, exp8
)

# ============================================================
# EXPERIMENT 9: BUTTERWORTH LOW-PASS FILTER
# ============================================================

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

matlab9 = r"""
clc; clear all; close all;

Ap = 1;
Ast = 40;
Fpass = 100;
Fstop = 150;
Fs = 1000;

Wpass = 2*Fpass/Fs;
Wstop = 2*Fstop/Fs;

[n,Wn] = buttord(Wpass,Wstop,Ap,Ast);
[b,a] = butter(n,Wn,'low');

freqz(b,a,8192,Fs);
title('Butterworth Low Pass Filter');
"""

add_experiment(
    9, "Butterworth Low-Pass Filter",
    "To design a digital Butterworth low-pass filter according to the given passband and stopband specifications.",
    matlab9, exp9
)

# ============================================================
# EXPERIMENT 10: CHEBYSHEV TYPE-I LOW-PASS FILTER
# ============================================================

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

matlab10 = r"""
clc; clear all; close all;

delta1 = 1;
delta2 = 40;

% Assumed corrected low-pass frequency ordering
wp = 0.2;
ws = 0.707;

[n,Wn] = cheb1ord(wp,ws,delta1,delta2);
[b,a] = cheby1(n,delta1,Wn,'low');

freqz(b,a,8192);
title('Chebyshev Type-I Low Pass Filter');
"""

add_experiment(
    10, "Chebyshev Type-I Low-Pass Filter",
    "To design a digital Chebyshev Type-I low-pass filter and plot its frequency response.",
    matlab10, exp10
)

# ============================================================
# EXPERIMENT 11: DECIMATION
# ============================================================

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

matlab11 = r"""
clc; clear all; close all;

t = 0:0.01:1;
D = 3;

x = sin(2*pi*5*t);
y = decimate(x,D);

subplot(2,1,1);
plot(t,x);
title('Original Signal');

subplot(2,1,2);
stem(y);
title('Decimated Signal');
"""

add_experiment(
    11, "Decimation",
    "To reduce the sampling rate of a discrete-time signal by a factor of three.",
    matlab11, exp11
)

# ============================================================
# EXPERIMENT 12: INTERPOLATION
# ============================================================

def exp12():
    t = np.arange(0, 1.01, 0.01)
    x = np.sin(2*np.pi*5*t)
    L = 3

    decimated = signal.decimate(x, L)
    interpolated = signal.resample_poly(decimated, L, 1)

    td = np.arange(len(decimated))*0.03
    ti = np.arange(len(interpolated))*0.01

    fig, ax = plt.subplots(3, 1, figsize=(9, 6))
    ax[0].plot(t, x)
    ax[0].set_title("Original signal")
    ax[1].stem(td, decimated)
    ax[1].set_title("Decimated signal")
    ax[2].plot(ti, interpolated)
    ax[2].set_title("Interpolated signal")

    for a in ax:
        a.grid(True)
        a.set_xlabel("Time (s)")
    fig.tight_layout()

    return [save_plot(fig, "exp12")], (
        f"Original samples = {len(x)}\n"
        f"Decimated samples = {len(decimated)}\n"
        f"Interpolated samples = {len(interpolated)}\n"
        f"Interpolation factor = {L}\n"
        f"Interpolated sequence = {np.round(interpolated, 4)}"
    )

matlab12 = r"""
clc; clear all; close all;

t = 0:0.01:1;
d = 3;

x = sin(2*pi*5*t);

y = decimate(x,d);
y1 = interp(y,d);

subplot(3,1,1);
plot(x);
title('Original Signal');

subplot(3,1,2);
stem(y);
title('Decimated Signal');

subplot(3,1,3);
plot(y1);
title('Interpolated Signal');
"""

add_experiment(
    12, "Interpolation",
    "To increase the sampling rate of a decimated signal using interpolation.",
    matlab12, exp12
)

# ============================================================
# AUDIO INPUT
# ============================================================

def get_audio():
    if audio_file:
        x, Fs = sf.read(audio_file)
        if x.ndim > 1:
            x = np.mean(x, axis=1)
        return x.astype(float), Fs, audio_file

    Fs = 8000
    t = np.arange(0, 3, 1/Fs)
    x = (
        0.5*np.sin(2*np.pi*440*t)
        + 0.3*np.sin(2*np.pi*880*t)
        + 0.2*np.sin(2*np.pi*1500*t)
    )
    return x, Fs, "Generated test audio"

# ============================================================
# EXPERIMENT 13: AUDIO FFT AND IFFT
# ============================================================

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

matlab13 = r"""
clc; clear all; close all;

[s,fs] = audioread('ringtone.mp3');

N = 20;
s = s(2:1:2^N+1);

FFT_org_abs = fft(s);

subplot(3,1,1);
plot(s);
title('Original Audio Signal');

subplot(3,1,2);
stem(abs(FFT_org_abs));
title('Magnitude of FFT');

IFFT_org = ifft(FFT_org_abs);

subplot(3,1,3);
plot(IFFT_org);
title('Reconstructed Audio Signal');
"""

add_experiment(
    13, "Extraction and Plotting of Audio Frequency Components",
    "To calculate the FFT of an audio signal, plot its frequency components and reconstruct it using IFFT.",
    matlab13, exp13
)

# ============================================================
# EXPERIMENT 14: AUDIO FREQUENCY FILTERING
# ============================================================

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

matlab14 = r"""
clc; clear all; close all;

[s,fs] = audioread('ringtone.mp3');

N = 20;
s = s(2:1:2^N+1);

FFT_org_abs = abs(fftshift(fft(s)));
nvec = -2^(N-1):2^(N-1)-1;

FFT_Filtered = fftshift(fft(s));

% Remove frequency components around zero
FFT_Filtered(abs(nvec) < 2^(N-6)) = 0;

% The original MATLAB indexing for the next
% range is invalid/reversed and needs correction.

filtered_signal = ifft(ifftshift(FFT_Filtered));

subplot(3,1,1);
plot(s);
title('Original Audio');

subplot(3,1,2);
plot(abs(FFT_Filtered));
title('Filtered Spectrum');

subplot(3,1,3);
plot(real(filtered_signal));
title('Filtered Audio');
"""

add_experiment(
    14, "Filtering of Audio Frequency Components",
    "To remove selected frequency components from an audio signal using frequency-domain filtering.",
    matlab14, exp14
)

# ============================================================
# PDF GENERATION
# ============================================================

styles = getSampleStyleSheet()

heading = ParagraphStyle(
    "ExperimentHeading",
    parent=styles["Heading1"],
    fontSize=13,
    leading=16,
    textColor=colors.darkblue,
    spaceAfter=8
)

section = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontSize=10,
    leading=13,
    spaceBefore=6,
    spaceAfter=4
)

body = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontSize=9,
    leading=12,
    spaceAfter=5
)

code_style = ParagraphStyle(
    "Code",
    fontName="Courier",
    fontSize=6.2,
    leading=7.5
)

output_style = ParagraphStyle(
    "Output",
    fontName="Courier",
    fontSize=7,
    leading=9
)

story = []

for item in experiments:

    story.append(Paragraph(
        f"EXPERIMENT {item['number']}: {item['title']}",
        heading
    ))

    story.append(Paragraph("Aim", section))
    story.append(Paragraph(item["aim"], body))

    story.append(Paragraph("MATLAB Code", section))
    story.append(Preformatted(item["matlab"].strip(), code_style))

    story.append(Paragraph("Generated Output", section))

    try:
        graph_paths, result = item["function"]()

        story.append(Preformatted(str(result), output_style))

        for path in graph_paths:
            if os.path.exists(path):
                story.append(Spacer(1, 3*mm))
                img = Image(path)
                img._restrictSize(175*mm, 105*mm)
                story.append(img)
                story.append(Spacer(1, 3*mm))

    except Exception as error:
        story.append(Paragraph(
            f"Output generation error: {str(error)}",
            body
        ))

    story.append(PageBreak())

def page_number(canvas, doc):
    canvas.saveState()

    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(13*mm, A4[1] - 9*mm, "ANAND AMBASTHA")

    canvas.setStrokeColor(colors.grey)
    canvas.line(
        13*mm, A4[1] - 12*mm,
        A4[0] - 13*mm, A4[1] - 12*mm
    )

    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(
        A4[0]/2, 8*mm, f"Page {doc.page}"
    )

    canvas.restoreState()

PDF_PATH = "/content/DSP_Lab_Manual.pdf"

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A4,
    rightMargin=13*mm,
    leftMargin=13*mm,
    topMargin=12*mm,
    bottomMargin=15*mm
)

doc.build(
    story,
    onFirstPage=page_number,
    onLaterPages=page_number
)

print("PDF created:", PDF_PATH)
print("Experiments included:", len(experiments))

files.download(PDF_PATH)

# NOTEBOOK CELL 28

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Read audio file
audio, Fs = sf.read('ringtone.mp3')

# Convert stereo to mono
if audio.ndim == 2:
    audio = np.mean(audio, axis=1)

# Select power-of-two samples
N = min(20, int(np.floor(np.log2(len(audio)))))

if N < 1:
    raise ValueError("Audio file is too short.")

s = audio[:2**N]
L = len(s)

print("Sampling Frequency:", Fs, "Hz")
print("Number of Samples:", L)

# FFT of original audio
FFT_original = np.fft.fftshift(np.fft.fft(s))
FFT_original_abs = np.abs(FFT_original)

# Frequency axis
freq = np.fft.fftshift(np.fft.fftfreq(L, d=1/Fs))

# Create frequency mask
FFT_filtered = FFT_original.copy()

# Remove low-frequency components
cutoff = 300
FFT_filtered[np.abs(freq) < cutoff] = 0

# Calculate filtered spectrum
FFT_filtered_abs = np.abs(FFT_filtered)

# Inverse FFT
filtered_signal = np.fft.ifft(
    np.fft.ifftshift(FFT_filtered)
).real

# Time axis
time = np.arange(L) / Fs

# Plot results
plt.figure(figsize=(11, 9))

plt.subplot(3, 1, 1)
plt.plot(time, s)
plt.title('Original Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(freq, FFT_original_abs)
plt.title('Original Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(freq, FFT_filtered_abs, color='red')
plt.title('Filtered Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Plot reconstructed filtered audio
plt.figure(figsize=(10, 4))
plt.plot(time, filtered_signal)
plt.title('Reconstructed Filtered Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

# Save filtered audio
sf.write('filtered_ringtone.wav', filtered_signal, Fs)

print("Filtered audio saved as filtered_ringtone.wav")

# NOTEBOOK CELL 29

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Read audio file
audio, Fs = sf.read('ringtone.mp3')

# Convert stereo to mono
if audio.ndim == 2:
    audio = np.mean(audio, axis=1)

# Select power-of-two samples
N = min(20, int(np.floor(np.log2(len(audio)))))

if N < 1:
    raise ValueError("Audio file is too short.")

s = audio[:2**N]
L = len(s)

print("Sampling Frequency:", Fs, "Hz")
print("Number of Samples:", L)

# FFT of original audio
FFT_original = np.fft.fftshift(np.fft.fft(s))
FFT_original_abs = np.abs(FFT_original)

# Frequency axis
freq = np.fft.fftshift(np.fft.fftfreq(L, d=1/Fs))

# Create frequency mask
FFT_filtered = FFT_original.copy()

# Remove low-frequency components
cutoff = 300
FFT_filtered[np.abs(freq) < cutoff] = 0

# Calculate filtered spectrum
FFT_filtered_abs = np.abs(FFT_filtered)

# Inverse FFT
filtered_signal = np.fft.ifft(
    np.fft.ifftshift(FFT_filtered)
).real

# Time axis
time = np.arange(L) / Fs

# Plot results
plt.figure(figsize=(11, 9))

plt.subplot(3, 1, 1)
plt.plot(time, s)
plt.title('Original Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(freq, FFT_original_abs)
plt.title('Original Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(freq, FFT_filtered_abs, color='red')
plt.title('Filtered Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Plot reconstructed filtered audio
plt.figure(figsize=(10, 4))
plt.plot(time, filtered_signal)
plt.title('Reconstructed Filtered Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

# Save filtered audio
sf.write('filtered_ringtone.wav', filtered_signal, Fs)

print("Filtered audio saved as filtered_ringtone.wav")

# NOTEBOOK CELL 30

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Read audio file
audio, Fs = sf.read('/content/job_masuk.mp3')

# Convert stereo to mono
if audio.ndim == 2:
    audio = np.mean(audio, axis=1)

# Select power-of-two samples
N = min(20, int(np.floor(np.log2(len(audio)))))

if N < 1:
    raise ValueError("Audio file is too short.")

s = audio[:2**N]
L = len(s)

print("Sampling Frequency:", Fs, "Hz")
print("Number of Samples:", L)

# FFT of original audio
FFT_original = np.fft.fftshift(np.fft.fft(s))
FFT_original_abs = np.abs(FFT_original)

# Frequency axis
freq = np.fft.fftshift(np.fft.fftfreq(L, d=1/Fs))

# Create frequency mask
FFT_filtered = FFT_original.copy()

# Remove low-frequency components
cutoff = 300
FFT_filtered[np.abs(freq) < cutoff] = 0

# Calculate filtered spectrum
FFT_filtered_abs = np.abs(FFT_filtered)

# Inverse FFT
filtered_signal = np.fft.ifft(
    np.fft.ifftshift(FFT_filtered)
).real

# Time axis
time = np.arange(L) / Fs

# Plot results
plt.figure(figsize=(11, 9))

plt.subplot(3, 1, 1)
plt.plot(time, s)
plt.title('Original Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(freq, FFT_original_abs)
plt.title('Original Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(freq, FFT_filtered_abs, color='red')
plt.title('Filtered Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Plot reconstructed filtered audio
plt.figure(figsize=(10, 4))
plt.plot(time, filtered_signal)
plt.title('Reconstructed Filtered Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.show()

# Save filtered audio
sf.write('filtered_ringtone.wav', filtered_signal, Fs)

print("Filtered audio saved as filtered_ringtone.wav")

# NOTEBOOK CELL 31

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample_poly
from pathlib import Path
from scipy.io.wavfile import read
import soundfile as sf

# Read audio file
audio, Fs = sf.read('ringtone.mp3')

# Convert stereo audio to mono
if audio.ndim == 2:
    audio = np.mean(audio, axis=1)

# Select a power-of-two number of samples
N = min(20, int(np.floor(np.log2(len(audio)))))

if N < 1:
    raise ValueError("Audio file is too short.")

s = audio[:2**N]
L = len(s)

print("Sampling Frequency:", Fs, "Hz")
print("Number of Samples:", L)
print("Duration:", L / Fs, "seconds")

# Calculate FFT
FFT_org = np.fft.fft(s)
FFT_abs = np.abs(FFT_org)

# Calculate frequency axis
freq = np.fft.fftfreq(L, d=1/Fs)

# Single-sided frequency spectrum
half = L // 2
freq_half = freq[:half]
FFT_half = (2 / L) * FFT_abs[:half]

# Inverse FFT
IFFT_org = np.fft.ifft(FFT_org).real

# Time axis
time = np.arange(L) / Fs

# Plot results
plt.figure(figsize=(11, 9))

plt.subplot(3, 1, 1)
plt.plot(time, s)
plt.title('Original Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(freq_half, FFT_half)
plt.title('Frequency Components of Audio Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, IFFT_org)
plt.title('Reconstructed Audio Signal using IFFT')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 32

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample_poly
from pathlib import Path
from scipy.io.wavfile import read
import soundfile as sf

# Read audio file
audio, Fs = sf.read('/content/job_masuk.mp3')

# Convert stereo audio to mono
if audio.ndim == 2:
    audio = np.mean(audio, axis=1)

# Select a power-of-two number of samples
N = min(20, int(np.floor(np.log2(len(audio)))))

if N < 1:
    raise ValueError("Audio file is too short.")

s = audio[:2**N]
L = len(s)

print("Sampling Frequency:", Fs, "Hz")
print("Number of Samples:", L)
print("Duration:", L / Fs, "seconds")

# Calculate FFT
FFT_org = np.fft.fft(s)
FFT_abs = np.abs(FFT_org)

# Calculate frequency axis
freq = np.fft.fftfreq(L, d=1/Fs)

# Single-sided frequency spectrum
half = L // 2
freq_half = freq[:half]
FFT_half = (2 / L) * FFT_abs[:half]

# Inverse FFT
IFFT_org = np.fft.ifft(FFT_org).real

# Time axis
time = np.arange(L) / Fs

# Plot results
plt.figure(figsize=(11, 9))

plt.subplot(3, 1, 1)
plt.plot(time, s)
plt.title('Original Audio Signal')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(freq_half, FFT_half)
plt.title('Frequency Components of Audio Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(time, IFFT_org)
plt.title('Reconstructed Audio Signal using IFFT')
plt.xlabel('Time (Seconds)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# NOTEBOOK CELL 33

import os
import shutil
import zipfile
from pathlib import Path
from google.colab import files

# ============================================================
# 1. PROJECT CONFIGURATION
# ============================================================

PROJECT_NAME = "DSP_MATLAB_Lab_Experiments"

BASE_DIR = Path("/content") / PROJECT_NAME
ZIP_PATH = Path("/content") / f"{PROJECT_NAME}.zip"

PDF_FILE = Path("/content/DSP_Lab_Report.pdf")
AUDIO_FILE = Path("/content/ringtone.mp3")

# Check that experiment source dictionaries exist
if "python_codes" not in globals():
    raise NameError(
        "python_codes dictionary is missing. "
        "Define it with the Python source code for each experiment."
    )

if "matlab_codes" not in globals():
    raise NameError(
        "matlab_codes dictionary is missing. "
        "Define it with the original MATLAB source code for each experiment."
    )

# ============================================================
# 2. CREATE DIRECTORY STRUCTURE
# ============================================================

folders = [
    "python",
    "matlab",
    "input",
    "output"
]

for folder in folders:
    (BASE_DIR / folder).mkdir(parents=True, exist_ok=True)

# ============================================================
# 3. SAVE PYTHON SCRIPTS
# ============================================================

for filename, code in python_codes.items():

    if not filename.endswith(".py"):
        filename += ".py"

    file_path = BASE_DIR / "python" / filename

    file_path.write_text(str(code), encoding="utf-8")

# ============================================================
# 4. SAVE MATLAB SCRIPTS
# ============================================================

for filename, code in matlab_codes.items():

    if not filename.endswith(".m"):
        filename += ".m"

    file_path = BASE_DIR / "matlab" / filename

    file_path.write_text(str(code), encoding="utf-8")

# ============================================================
# 5. COPY GENERATED PDF REPORT
# ============================================================

if not PDF_FILE.exists():
    raise FileNotFoundError(
        f"PDF report not found: {PDF_FILE}"
    )

shutil.copy2(
    PDF_FILE,
    BASE_DIR / "DSP_Lab_Report.pdf"
)

# ============================================================
# 6. COPY INPUT RINGTONE
# ============================================================

if AUDIO_FILE.exists():

    shutil.copy2(
        AUDIO_FILE,
        BASE_DIR / "input" / "ringtone.mp3"
    )

else:
    print("WARNING: ringtone.mp3 not found.")
    print("Audio experiments may require this input file.")

# ============================================================
# 7. CREATE DETAILED README
# ============================================================

readme = r"""
# Digital Signal Processing Laboratory Experiments

### Course Code: ECC-351

**Author:** Anand Ambastha

**Subject:** Digital Signal Processing

---

## 1. Overview

This repository contains Digital Signal Processing (DSP)
laboratory experiments implemented using MATLAB and Python.

The project covers fundamental DSP concepts, including
discrete Fourier transforms, convolution, digital filter
design, sampling-rate conversion, and audio signal processing.

Each experiment is organized with its corresponding MATLAB
implementation (`.m`) and Python implementation (`.py`).

The Python implementations generate numerical results and
graphical visualizations. These outputs are compiled into
a PDF laboratory report.

### Project objectives

- Implement fundamental DSP algorithms.
- Understand time-domain and frequency-domain operations.
- Study linear and circular convolution.
- Design and analyse digital filters.
- Understand decimation and interpolation.
- Apply Fourier analysis to audio signals.
- Compare MATLAB and Python implementations.
- Maintain reproducible experiment code and results.

---

## 2. Official Laboratory Manual

**Course:** Digital Signal Processing (ECC-351)

The experiments are based on the official short laboratory
manual.

**Manual:** [ECC-351 Digital Signal Processing Short Manual](https://drive.google.com/file/d/1uFd0gr7VJyATEy6-HB5SVoVQ7ajcHPJp/view)

---

## 3. Repository Structure

```text
DSP_MATLAB_Lab_Experiments/
│
├── python/
│   ├── 01_DFT_IDFT.py
│   ├── 02_Parseval.py
│   ├── 03_Time_Shifting_Reversal.py
│   ├── 04_Linear_Convolution.py
│   ├── 05_Circular_Convolution.py
│   ├── 06_Convolution_Methods.py
│   ├── 07_FIR_Lowpass.py
│   ├── 08_FIR_Highpass.py
│   ├── 09_Butterworth_Lowpass.py
│   ├── 10_Chebyshev_Lowpass.py
│   ├── 11_Decimation.py
│   ├── 12_Interpolation.py
│   ├── 13_Audio_FFT_IFFT.py
│   └── 14_Audio_Filtering.py
│
├── matlab/
│   ├── 01_DFT_IDFT.m
│   ├── 02_Parseval.m
│   ├── 03_Time_Shifting_Reversal.m
│   ├── 04_Linear_Convolution.m
│   ├── 05_Circular_Convolution.m
│   ├── 06_Convolution_Methods.m
│   ├── 07_FIR_Lowpass.m
│   ├── 08_FIR_Highpass.m
│   ├── 09_Butterworth_Lowpass.m
│   ├── 10_Chebyshev_Lowpass.m
│   ├── 11_Decimation.m
│   ├── 12_Interpolation.m
│   ├── 13_Audio_FFT_IFFT.m
│   └── 14_Audio_Filtering.m
│
├── input/
│   └── ringtone.mp3
│
├── output/
│
├── DSP_Lab_Report.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

The actual files included depend on the experiment scripts
provided during packaging.

---

## 4. Experiments

### Experiment 1: DFT and IDFT

Implementation of the Discrete Fourier Transform and
Inverse Discrete Fourier Transform using their mathematical
definitions.

Operations:
- Calculate DFT coefficients.
- Calculate IDFT.
- Reconstruct the original sequence.
- Examine complex frequency-domain values.

Input sequences:
- DFT: [1, 3, -1, -2]
- IDFT: [1, 2-5j, -1, 2+5j]

### Experiment 2: Parseval's Theorem

Verification of Parseval's theorem by comparing the
signal energy in the time and frequency domains.

Input:
[0, 2, 4, 6, 8, 10, 12, 14, 16]

### Experiment 3: Circular Time Shifting and Time Reversal

Study of circular time shifting by five samples and
time reversal of a discrete-time sequence.

### Experiment 4: Linear Convolution

Implementation of linear convolution between:

- x = [1, 2, 0, 1]
- h = [1, 5, 7, 3]

### Experiment 5: Circular Convolution

Implementation of circular convolution using the
same input sequences and an appropriate transform length.

### Experiment 6: Linear and Circular Convolution

Study of the relationship between linear and circular
convolution using folding and zero padding.

Required zero-padded length:

N = N1 + N2 - 1

For the given sequences, N = 7.

### Experiment 7: FIR Low-Pass Filter

Design of an FIR low-pass filter using the rectangular
window method.

Specifications:
- Passband ripple: 0.05
- Stopband ripple: 0.04
- Passband frequency: 1200 Hz
- Stopband frequency: 2000 Hz
- Sampling frequency: 9000 Hz

### Experiment 8: FIR High-Pass Filter

Design of an FIR high-pass filter using the rectangular
window method.

Specifications:
- Passband ripple: 0.05
- Stopband ripple: 0.04
- Passband frequency: 1500 Hz
- Stopband frequency: 2000 Hz
- Sampling frequency: 9000 Hz

### Experiment 9: Butterworth Low-Pass Filter

Design and analysis of a Butterworth low-pass filter.

Specifications:
- Passband attenuation: 1 dB
- Stopband attenuation: 40 dB
- Passband frequency: 100 Hz
- Stopband frequency: 150 Hz
- Sampling frequency: 1000 Hz

### Experiment 10: Chebyshev Type-I Low-Pass Filter

Design and analysis of a Chebyshev Type-I low-pass filter.

The supplied MATLAB material contains reversed passband
and stopband frequency values. The Python implementation
uses the assumed ordering Wpass = 0.2 and Wstop = 0.707.
This assumption should be verified against the original
laboratory instructions.

### Experiment 11: Decimation

Study of sampling-rate reduction using a decimation factor
of three.

Input signal:

x(t) = sin(2π × 5 × t)

Time interval: 0 to 1 second.

Sampling interval: 0.01 second.

### Experiment 12: Interpolation

Study of interpolation and sampling-rate conversion.

The supplied procedure performs decimation by three
followed by interpolation by three.

### Experiment 13: Audio FFT and IFFT

Analysis of an audio signal using FFT and IFFT.

Operations:
- Read the input audio.
- Extract the required samples.
- Calculate FFT.
- Plot the time-domain signal.
- Plot the frequency spectrum.
- Perform IFFT reconstruction.

Input file: `input/ringtone.mp3`

### Experiment 14: Audio Frequency-Domain Filtering

Frequency-domain filtering of an audio signal.

Operations:
- Read the audio signal.
- Transform it into the frequency domain.
- Apply frequency-domain filtering.
- Reconstruct the filtered signal.
- Compare original and filtered signals.

The supplied MATLAB indexing and the assumed Python
filter cutoff should be checked before treating the two
implementations as exactly equivalent.

---

## 5. Technologies and Libraries

### MATLAB

Used for the original experiment implementations and
signal-processing computations.

### Python

Used for numerical computation, signal processing,
visualization, and PDF report generation.

### Python libraries

| Library | Purpose |
|---|---|
| NumPy | Numerical computation |
| SciPy | Signal processing and filter design |
| Matplotlib | Graphs and visualization |
| SoundFile | Audio file processing |
| ReportLab | PDF generation |

---

## 6. Installation

### Requirements

- Python 3.9 or later recommended.
- MATLAB for executing MATLAB scripts.
- Required Python dependencies.
- Input audio file for audio experiments.

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project:

```bash
cd DSP_MATLAB_Lab_Experiments
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 7. Running Python Experiments

Each experiment has an independent Python script.

Example:

```bash
python python/01_DFT_IDFT.py
```

Another example:

```bash
python python/09_Butterworth_Lowpass.py
```

Run the required script from the project root directory
so that relative input and output paths resolve correctly.

---

## 8. Running MATLAB Experiments

Open MATLAB and navigate to the repository directory.

Execute the required script.

Example:

```matlab
run('matlab/01_DFT_IDFT.m')
```

For audio experiments, ensure the input audio file
is available at the expected path.

---

## 9. Input Data

The audio-processing experiments require an input
audio file.

Expected location:

```text
input/ringtone.mp3
```

The same audio file should be used for both MATLAB
and Python implementations when comparing results.

If another audio file is used, update the corresponding
file paths in the scripts.

---

## 10. Generated Outputs

The Python implementations may generate:

- Numerical results.
- Time-domain signal plots.
- Frequency-domain plots.
- Filter magnitude-response plots.
- Reconstructed signal plots.
- Audio filtering comparisons.

The compiled report is:

`DSP_Lab_Report.pdf`

### PDF report format

Each experiment contains:

1. Aim
2. Original MATLAB Code
3. Generated Python Output

Each experiment starts on a new page. The report also
includes the author header and page numbering.

---

## 11. MATLAB and Python Comparison

The repository provides both MATLAB and Python
implementations to facilitate comparison.

Important considerations:

- Array indexing conventions.
- FFT normalization.
- Zero-padding and transform lengths.
- Filter-design conventions.
- Sampling frequencies and frequency units.
- Audio input and output handling.
- Floating-point numerical precision.

Equivalent implementations should be verified using
numerical results, not only visual similarity of plots.

---

## 12. Reproducibility and Limitations

For reproducible results:

1. Use identical input sequences.
2. Maintain identical sampling frequencies.
3. Use consistent transform lengths.
4. Verify filter specifications.
5. Use the same audio input.
6. Check numerical results before comparing graphs.
7. Document any assumptions or deviations from the manual.

Some filter and audio-processing specifications require
verification against the original manual. Numerical
differences may occur due to library conventions and
floating-point precision.

---

## 13. Author

**ANAND AMBASTHA**

Digital Signal Processing Laboratory

Course Code: ECC-351

---

*This repository is intended for academic and educational
purposes.*
"""

(BASE_DIR / "README.md").write_text(
    readme.strip() + "\n",
    encoding="utf-8"
)

# ============================================================
# 8. CREATE REQUIREMENTS.TXT
# ============================================================

requirements = """numpy
scipy
matplotlib
soundfile
reportlab
"""

(BASE_DIR / "requirements.txt").write_text(
    requirements,
    encoding="utf-8"
)

# ============================================================
# 9. CREATE .GITIGNORE
# ============================================================

gitignore = """__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store
"""

(BASE_DIR / ".gitignore").write_text(
    gitignore,
    encoding="utf-8"
)

# ============================================================
# 10. VERIFY PROJECT CONTENTS
# ============================================================

python_files = list((BASE_DIR / "python").glob("*.py"))
matlab_files = list((BASE_DIR / "matlab").glob("*.m"))

print("=" * 60)
print("PROJECT VERIFICATION")
print("=" * 60)

print("Python scripts:", len(python_files))
print("MATLAB scripts:", len(matlab_files))
print("PDF report:", (BASE_DIR / "DSP_Lab_Report.pdf").exists())
print("Audio file:", (BASE_DIR / "input" / "ringtone.mp3").exists())

if not python_files:
    raise ValueError("No Python scripts were saved.")

if not matlab_files:
    raise ValueError("No MATLAB scripts were saved.")

print("\nPYTHON FILES")
for f in sorted(python_files):
    print(" -", f.name)

print("\nMATLAB FILES")
for f in sorted(matlab_files):
    print(" -", f.name)

# ============================================================
# 11. CREATE ZIP FILE
# ============================================================

if ZIP_PATH.exists():
    ZIP_PATH.unlink()

with zipfile.ZipFile(
    ZIP_PATH,
    "w",
    compression=zipfile.ZIP_DEFLATED
) as zipf:

    for file_path in BASE_DIR.rglob("*"):

        if file_path.is_file():

            archive_path = file_path.relative_to(BASE_DIR.parent)

            zipf.write(
                file_path,
                archive_path
            )

# ============================================================
# 12. VERIFY ZIP CONTENTS
# ============================================================

with zipfile.ZipFile(ZIP_PATH, "r") as zipf:

    zip_contents = zipf.namelist()

    print("\nZIP CONTENTS")
    for item in zip_contents:
        print(" -", item)

    print("\nTotal files in ZIP:", len(zip_contents))

print("\n" + "=" * 60)
print("PROJECT PACKAGED SUCCESSFULLY")
print("=" * 60)

print("Project directory:", BASE_DIR)
print("ZIP location:", ZIP_PATH)
print("ZIP size: {:.2f} MB".format(ZIP_PATH.stat().st_size / (1024 * 1024)))

# ============================================================
# 13. DOWNLOAD ZIP
# ============================================================

files.download(str(ZIP_PATH))

# NOTEBOOK CELL 34

import os
import shutil
import zipfile
import inspect
import textwrap
from pathlib import Path
from google.colab import files

# ============================================================
# 1. CONFIGURATION
# ============================================================

PROJECT_NAME = "DSP_MATLAB_Lab_Experiments"

BASE_DIR = Path("/content") / PROJECT_NAME
ZIP_PATH = Path("/content") / f"{PROJECT_NAME}.zip"

PDF_FILE = Path("/content/DSP_Lab_Manual.pdf")
AUDIO_FILE = Path("/content/ringtone.mp3")

# Check original experiment definitions
if "experiments" not in globals():
    raise NameError(
        "The experiments list is missing. "
        "Run your original DSP experiment/PDF-generation cell first."
    )

# ============================================================
# 2. CREATE FOLDERS
# ============================================================

for folder in ["python", "matlab", "input", "output"]:
    (BASE_DIR / folder).mkdir(parents=True, exist_ok=True)

# ============================================================
# 3. COMMON PYTHON IMPORTS
# ============================================================

common_imports = """
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
"""

# ============================================================
# 4. SAVE ORIGINAL MATLAB AND PYTHON EXPERIMENTS
# ============================================================

saved_python = 0
saved_matlab = 0
experiment_manifest = []

for item in experiments:

    number = item["number"]
    title = item["title"]
    matlab_code = item["matlab"]
    function = item["function"]

    safe_title = (
        title.replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
        .replace("(", "")
        .replace(")", "")
    )

    filename = f"{int(number):02d}_{safe_title}"

    # --------------------------------------------------------
    # SAVE MATLAB SOURCE
    # --------------------------------------------------------

    matlab_path = BASE_DIR / "matlab" / f"{filename}.m"

    matlab_path.write_text(
        str(matlab_code),
        encoding="utf-8"
    )

    saved_matlab += 1

    # --------------------------------------------------------
    # SAVE PYTHON FUNCTION SOURCE
    # --------------------------------------------------------

    try:
        function_source = inspect.getsource(function)
        function_source = textwrap.dedent(function_source)

    except (OSError, TypeError) as error:
        raise RuntimeError(
            f"Could not retrieve Python source for experiment {number}. "
            "Make sure the experiment functions are defined in notebook cells."
        ) from error

    python_source = (
        common_imports
        + "\n\n"
        + f"# Experiment {number}: {title}\n"
        + "# Original implementation from the DSP experiment notebook.\n\n"
        + function_source
        + "\n\n"
        + f"if __name__ == '__main__':\n"
        + f"    {function.__name__}()\n"
    )

    python_path = BASE_DIR / "python" / f"{filename}.py"

    python_path.write_text(
        python_source,
        encoding="utf-8"
    )

    saved_python += 1

    experiment_manifest.append({
        "number": number,
        "title": title,
        "filename": filename
    })

# ============================================================
# 5. SAVE COMPLETE EXPERIMENT SOURCE AS A MASTER FILE
# ============================================================

# Preserve the original notebook's executed Python cells.
# This provides a complete source archive alongside individual
# experiment scripts.

try:
    from IPython import get_ipython

    notebook_history = get_ipython().user_ns.get("In", [])

    master_source = "\n\n".join(
        f"# NOTEBOOK CELL {i}\n\n{cell}"
        for i, cell in enumerate(notebook_history)
        if isinstance(cell, str) and cell.strip()
    )

    (BASE_DIR / "python" / "DSP_Notebook_Source.py").write_text(
        master_source,
        encoding="utf-8"
    )

except Exception as error:
    print("Notebook source archive could not be created:", error)

# ============================================================
# 6. COPY PDF REPORT
# ============================================================

if not PDF_FILE.exists():
    raise FileNotFoundError(
        f"PDF not found: {PDF_FILE}. "
        "Generate the PDF before running this cell."
    )

shutil.copy2(
    PDF_FILE,
    BASE_DIR / "DSP_Lab_Report.pdf"
)

# ============================================================
# 7. COPY RINGTONE INPUT
# ============================================================

if AUDIO_FILE.exists():

    shutil.copy2(
        AUDIO_FILE,
        BASE_DIR / "input" / "ringtone.mp3"
    )

else:
    print("WARNING: ringtone.mp3 not found.")

# ============================================================
# 8. CREATE REQUIREMENTS.TXT
# ============================================================

requirements = """numpy
scipy
matplotlib
soundfile
reportlab
"""

(BASE_DIR / "requirements.txt").write_text(
    requirements,
    encoding="utf-8"
)

# ============================================================
# 9. CREATE README
# ============================================================

readme = r"""
# Digital Signal Processing Laboratory Experiments

**Course:** Digital Signal Processing  
**Course Code:** ECC-351  
**Author:** ANAND AMBASTHA

---

## Overview

This repository contains Digital Signal Processing laboratory
experiments implemented in MATLAB and Python.

The repository includes original MATLAB implementations,
Python implementations, input audio data, generated results,
and the compiled laboratory report.

## Official Laboratory Manual

[Digital Signal Processing (ECC-351) Short Manual](https://drive.google.com/file/d/1uFd0gr7VJyATEy6-HB5SVoVQ7ajcHPJp/view)

## Repository Structure

```text
DSP_MATLAB_Lab_Experiments/
│
├── python/
│   ├── Individual experiment scripts (.py)
│   └── DSP_Notebook_Source.py
│
├── matlab/
│   └── Individual experiment scripts (.m)
│
├── input/
│   └── ringtone.mp3
│
├── output/
│   └── Generated plots and results
│
├── DSP_Lab_Report.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

## Experiments

The repository contains the experiments defined in the
original DSP laboratory implementation:

1. DFT and IDFT
2. Parseval's Theorem
3. Circular Time Shifting and Time Reversal
4. Linear Convolution
5. Circular Convolution
6. Linear and Circular Convolution using Zero Padding
7. FIR Low-Pass Filter
8. FIR High-Pass Filter
9. Butterworth Low-Pass Filter
10. Chebyshev Type-I Low-Pass Filter
11. Decimation
12. Interpolation
13. Audio FFT and IFFT
14. Audio Frequency-Domain Filtering

## Technologies

- MATLAB
- Python
- NumPy
- SciPy
- Matplotlib
- SoundFile
- ReportLab

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd DSP_MATLAB_Lab_Experiments
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running Python Scripts

Individual experiment scripts are available in the `python/`
directory.

Example:

```bash
python python/01_DFT_IDFT.py
```

Run scripts from the repository root directory.

**Note:** Individual scripts contain the extracted experiment
functions. If an implementation depends on helper functions
or variables defined elsewhere in the original notebook,
those dependencies must also be included before standalone
execution.

The complete notebook source archive is also provided as
`python/DSP_Notebook_Source.py`.

## Running MATLAB Scripts

Open the required `.m` file in MATLAB and execute it.

Example:

```matlab
run('matlab/01_DFT_IDFT.m')
```

## Input Audio

Audio experiments use:

`input/ringtone.mp3`

Keep the input file in this location when executing the
audio-processing experiments.

## Laboratory Report

`DSP_Lab_Report.pdf` contains:

- Aim
- Original MATLAB code
- Generated Python output
- Numerical results and graphical visualizations

Each experiment begins on a new page. The report includes
the author header and page numbering.

## Reproducibility

For meaningful MATLAB-Python comparisons:

- Use identical input sequences.
- Maintain consistent sampling frequencies.
- Verify FFT normalization and indexing.
- Use identical audio input files.
- Check filter-design specifications.
- Compare numerical outputs before comparing plots.

Some implementations may contain assumptions or adjustments
relative to the original manual. Refer to the source scripts
when verifying those details.

---

## Author

**ANAND AMBASTHA**

Digital Signal Processing Laboratory  
ECC-351
"""

(BASE_DIR / "README.md").write_text(
    readme.strip() + "\n",
    encoding="utf-8"
)

# ============================================================
# 10. CREATE GITIGNORE
# ============================================================

gitignore = """
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store
"""

(BASE_DIR / ".gitignore").write_text(
    gitignore.strip() + "\n",
    encoding="utf-8"
)

# ============================================================
# 11. VERIFY GENERATED FILES
# ============================================================

python_files = list((BASE_DIR / "python").glob("*.py"))
matlab_files = list((BASE_DIR / "matlab").glob("*.m"))

print("\n" + "=" * 60)
print("PROJECT VERIFICATION")
print("=" * 60)

print("Experiments defined:", len(experiments))
print("Python scripts saved:", saved_python)
print("MATLAB scripts saved:", saved_matlab)
print("PDF report:", (BASE_DIR / "DSP_Lab_Report.pdf").exists())
print("Ringtone:", (BASE_DIR / "input" / "ringtone.mp3").exists())

if saved_python != len(experiments):
    raise RuntimeError("Some Python experiment scripts were not saved.")

if saved_matlab != len(experiments):
    raise RuntimeError("Some MATLAB experiment scripts were not saved.")

print("\nPYTHON FILES:")
for f in sorted(python_files):
    print(" ", f.name)

print("\nMATLAB FILES:")
for f in sorted(matlab_files):
    print(" ", f.name)

# ============================================================
# 12. CREATE ZIP
# ============================================================

if ZIP_PATH.exists():
    ZIP_PATH.unlink()

with zipfile.ZipFile(
    ZIP_PATH,
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    for file_path in BASE_DIR.rglob("*"):

        if file_path.is_file():

            zipf.write(
                file_path,
                file_path.relative_to(BASE_DIR.parent)
            )

# ============================================================
# 13. VERIFY ZIP
# ============================================================

with zipfile.ZipFile(ZIP_PATH, "r") as zipf:

    contents = zipf.namelist()

    print("\nFILES INCLUDED IN ZIP:")
    for name in contents:
        print(" ", name)

    print("\nTotal files:", len(contents))

print("\n" + "=" * 60)
print("GITHUB PROJECT ZIP CREATED")
print("=" * 60)

print("Location:", ZIP_PATH)
print("Size: {:.2f} MB".format(
    ZIP_PATH.stat().st_size / (1024 * 1024)
))

# ============================================================
# 14. DOWNLOAD
# ============================================================

files.download(str(ZIP_PATH))

# NOTEBOOK CELL 35

import os
import shutil
import zipfile
import inspect
import textwrap
from pathlib import Path
from google.colab import files

# ============================================================
# 1. CONFIGURATION
# ============================================================

PROJECT_NAME = "DSP_MATLAB_Lab_Experiments"

BASE_DIR = Path("/content") / PROJECT_NAME
ZIP_PATH = Path("/content") / f"{PROJECT_NAME}.zip"

PDF_FILE = Path("/content/DSP_Lab_Manual.pdf")
AUDIO_FILE = Path("/content/ringtone.mp3")

# Check original experiment definitions
if "experiments" not in globals():
    raise NameError(
        "The experiments list is missing. "
        "Run your original DSP experiment/PDF-generation cell first."
    )

# ============================================================
# 2. CREATE FOLDERS
# ============================================================

for folder in ["python", "matlab", "input", "output"]:
    (BASE_DIR / folder).mkdir(parents=True, exist_ok=True)

# ============================================================
# 3. COMMON PYTHON IMPORTS
# ============================================================

common_imports = """
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
"""

# ============================================================
# 4. SAVE ORIGINAL MATLAB AND PYTHON EXPERIMENTS
# ============================================================

saved_python = 0
saved_matlab = 0
experiment_manifest = []

for item in experiments:

    number = item["number"]
    title = item["title"]
    matlab_code = item["matlab"]
    function = item["function"]

    safe_title = (
        title.replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
        .replace("(", "")
        .replace(")", "")
    )

    filename = f"{int(number):02d}_{safe_title}"

    # --------------------------------------------------------
    # SAVE MATLAB SOURCE
    # --------------------------------------------------------

    matlab_path = BASE_DIR / "matlab" / f"{filename}.m"

    matlab_path.write_text(
        str(matlab_code),
        encoding="utf-8"
    )

    saved_matlab += 1

    # --------------------------------------------------------
    # SAVE PYTHON FUNCTION SOURCE
    # --------------------------------------------------------

    try:
        function_source = inspect.getsource(function)
        function_source = textwrap.dedent(function_source)

    except (OSError, TypeError) as error:
        raise RuntimeError(
            f"Could not retrieve Python source for experiment {number}. "
            "Make sure the experiment functions are defined in notebook cells."
        ) from error

    python_source = (
        common_imports
        + "\n\n"
        + f"# Experiment {number}: {title}\n"
        + "# Original implementation from the DSP experiment notebook.\n\n"
        + function_source
        + "\n\n"
        + f"if __name__ == '__main__':\n"
        + f"    {function.__name__}()\n"
    )

    python_path = BASE_DIR / "python" / f"{filename}.py"

    python_path.write_text(
        python_source,
        encoding="utf-8"
    )

    saved_python += 1

    experiment_manifest.append({
        "number": number,
        "title": title,
        "filename": filename
    })

# ============================================================
# 5. SAVE COMPLETE EXPERIMENT SOURCE AS A MASTER FILE
# ============================================================

# Preserve the original notebook's executed Python cells.
# This provides a complete source archive alongside individual
# experiment scripts.

try:
    from IPython import get_ipython

    notebook_history = get_ipython().user_ns.get("In", [])

    master_source = "\n\n".join(
        f"# NOTEBOOK CELL {i}\n\n{cell}"
        for i, cell in enumerate(notebook_history)
        if isinstance(cell, str) and cell.strip()
    )

    (BASE_DIR / "python" / "DSP_Notebook_Source.py").write_text(
        master_source,
        encoding="utf-8"
    )

except Exception as error:
    print("Notebook source archive could not be created:", error)

# ============================================================
# 6. COPY PDF REPORT
# ============================================================

if not PDF_FILE.exists():
    raise FileNotFoundError(
        f"PDF not found: {PDF_FILE}. "
        "Generate the PDF before running this cell."
    )

shutil.copy2(
    PDF_FILE,
    BASE_DIR / "DSP_Lab_Report.pdf"
)

# ============================================================
# 7. COPY RINGTONE INPUT
# ============================================================

if AUDIO_FILE.exists():

    shutil.copy2(
        AUDIO_FILE,
        BASE_DIR / "input" / "ringtone.mp3"
    )

else:
    print("WARNING: ringtone.mp3 not found.")


# ============================================================
# 8. COLLECT ALL GENERATED EXPERIMENT OUTPUTS
# ============================================================

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

from pathlib import Path
import shutil

# File types to collect
output_extensions = {
    ".png", ".jpg", ".jpeg", ".svg", ".pdf",
    ".csv", ".txt", ".npy", ".npz",
    ".wav", ".flac"
}

# Directories that should not be scanned
excluded_directories = {
    PROJECT_NAME,
    "sample_data",
    ".config",
    ".cache",
    "python",
    "matlab",
    "input"
}

copied_outputs = []

for source in Path("/content").rglob("*"):

    if not source.is_file():
        continue

    # Skip files already inside the project
    if BASE_DIR in source.parents:
        continue

    # Skip the main report and input audio
    if source == PDF_FILE or source == AUDIO_FILE:
        continue

    # Skip unrelated file types
    if source.suffix.lower() not in output_extensions:
        continue

    # Skip files inside excluded directories
    if any(part in excluded_directories for part in source.parts):
        continue

    # Preserve subfolder organization where possible
    destination = OUTPUT_DIR / source.name

    # Avoid overwriting files with identical names
    counter = 1
    while destination.exists():
        destination = OUTPUT_DIR / f"{source.stem}_{counter}{source.suffix}"
        counter += 1

    shutil.copy2(source, destination)
    copied_outputs.append(destination.name)

print("GENERATED OUTPUTS COLLECTED")
print("-" * 45)

for filename in copied_outputs:
    print("Saved:", filename)

print("\nTotal output files:", len(copied_outputs))

if not copied_outputs:
    print(
        "WARNING: No generated output files were found. "
        "Check where your experiment code saves its plots and results."
    )


# ============================================================
# 8. CREATE REQUIREMENTS.TXT
# ============================================================

requirements = """numpy
scipy
matplotlib
soundfile
reportlab
"""

(BASE_DIR / "requirements.txt").write_text(
    requirements,
    encoding="utf-8"
)

# ============================================================
# 9. CREATE README
# ============================================================

readme = r"""
# Digital Signal Processing Laboratory Experiments

**Course:** Digital Signal Processing  
**Course Code:** ECC-351  
**Author:** ANAND AMBASTHA

---

## Overview

This repository contains Digital Signal Processing laboratory
experiments implemented in MATLAB and Python.

The repository includes original MATLAB implementations,
Python implementations, input audio data, generated results,
and the compiled laboratory report.

## Official Laboratory Manual

[Digital Signal Processing (ECC-351) Short Manual](https://drive.google.com/file/d/1uFd0gr7VJyATEy6-HB5SVoVQ7ajcHPJp/view)

## Repository Structure

```text
DSP_MATLAB_Lab_Experiments/
│
├── python/
│   ├── Individual experiment scripts (.py)
│   └── DSP_Notebook_Source.py
│
├── matlab/
│   └── Individual experiment scripts (.m)
│
├── input/
│   └── ringtone.mp3
│
├── output/
│   └── Generated plots and results
│
├── DSP_Lab_Report.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

## Experiments

The repository contains the experiments defined in the
original DSP laboratory implementation:

1. DFT and IDFT
2. Parseval's Theorem
3. Circular Time Shifting and Time Reversal
4. Linear Convolution
5. Circular Convolution
6. Linear and Circular Convolution using Zero Padding
7. FIR Low-Pass Filter
8. FIR High-Pass Filter
9. Butterworth Low-Pass Filter
10. Chebyshev Type-I Low-Pass Filter
11. Decimation
12. Interpolation
13. Audio FFT and IFFT
14. Audio Frequency-Domain Filtering

## Technologies

- MATLAB
- Python
- NumPy
- SciPy
- Matplotlib
- SoundFile
- ReportLab

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd DSP_MATLAB_Lab_Experiments
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running Python Scripts

Individual experiment scripts are available in the `python/`
directory.

Example:

```bash
python python/01_DFT_IDFT.py
```

Run scripts from the repository root directory.

**Note:** Individual scripts contain the extracted experiment
functions. If an implementation depends on helper functions
or variables defined elsewhere in the original notebook,
those dependencies must also be included before standalone
execution.

The complete notebook source archive is also provided as
`python/DSP_Notebook_Source.py`.

## Running MATLAB Scripts

Open the required `.m` file in MATLAB and execute it.

Example:

```matlab
run('matlab/01_DFT_IDFT.m')
```

## Input Audio

Audio experiments use:

`input/ringtone.mp3`

Keep the input file in this location when executing the
audio-processing experiments.

## Laboratory Report

`DSP_Lab_Report.pdf` contains:

- Aim
- Original MATLAB code
- Generated Python output
- Numerical results and graphical visualizations

Each experiment begins on a new page. The report includes
the author header and page numbering.

## Reproducibility

For meaningful MATLAB-Python comparisons:

- Use identical input sequences.
- Maintain consistent sampling frequencies.
- Verify FFT normalization and indexing.
- Use identical audio input files.
- Check filter-design specifications.
- Compare numerical outputs before comparing plots.

Some implementations may contain assumptions or adjustments
relative to the original manual. Refer to the source scripts
when verifying those details.

---

## Author

**ANAND AMBASTHA**

Digital Signal Processing Laboratory  
ECC-351
"""

(BASE_DIR / "README.md").write_text(
    readme.strip() + "\n",
    encoding="utf-8"
)

# ============================================================
# 10. CREATE GITIGNORE
# ============================================================

gitignore = """
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store
"""

(BASE_DIR / ".gitignore").write_text(
    gitignore.strip() + "\n",
    encoding="utf-8"
)

# ============================================================
# 11. VERIFY GENERATED FILES
# ============================================================

python_files = list((BASE_DIR / "python").glob("*.py"))
matlab_files = list((BASE_DIR / "matlab").glob("*.m"))

print("\n" + "=" * 60)
print("PROJECT VERIFICATION")
print("=" * 60)

print("Experiments defined:", len(experiments))
print("Python scripts saved:", saved_python)
print("MATLAB scripts saved:", saved_matlab)
print("PDF report:", (BASE_DIR / "DSP_Lab_Report.pdf").exists())
print("Ringtone:", (BASE_DIR / "input" / "ringtone.mp3").exists())

if saved_python != len(experiments):
    raise RuntimeError("Some Python experiment scripts were not saved.")

if saved_matlab != len(experiments):
    raise RuntimeError("Some MATLAB experiment scripts were not saved.")

print("\nPYTHON FILES:")
for f in sorted(python_files):
    print(" ", f.name)

print("\nMATLAB FILES:")
for f in sorted(matlab_files):
    print(" ", f.name)

# ============================================================
# 12. CREATE ZIP
# ============================================================

if ZIP_PATH.exists():
    ZIP_PATH.unlink()

with zipfile.ZipFile(
    ZIP_PATH,
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    for file_path in BASE_DIR.rglob("*"):

        if file_path.is_file():

            zipf.write(
                file_path,
                file_path.relative_to(BASE_DIR.parent)
            )

# ============================================================
# 13. VERIFY ZIP
# ============================================================

with zipfile.ZipFile(ZIP_PATH, "r") as zipf:

    contents = zipf.namelist()

    print("\nFILES INCLUDED IN ZIP:")
    for name in contents:
        print(" ", name)

    print("\nTotal files:", len(contents))

print("\n" + "=" * 60)
print("GITHUB PROJECT ZIP CREATED")
print("=" * 60)

print("Location:", ZIP_PATH)
print("Size: {:.2f} MB".format(
    ZIP_PATH.stat().st_size / (1024 * 1024)
))

# ============================================================
# 14. DOWNLOAD
# ============================================================

files.download(str(ZIP_PATH))