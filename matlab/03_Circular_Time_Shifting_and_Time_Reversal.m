
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
