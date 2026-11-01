
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
