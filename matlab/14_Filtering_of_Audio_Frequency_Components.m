
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
