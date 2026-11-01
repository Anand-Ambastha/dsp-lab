
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
