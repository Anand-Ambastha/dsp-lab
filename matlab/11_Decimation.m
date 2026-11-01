
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
