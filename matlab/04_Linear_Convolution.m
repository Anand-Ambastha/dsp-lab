
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
