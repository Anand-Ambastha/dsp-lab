
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
