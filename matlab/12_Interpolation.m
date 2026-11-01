
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
