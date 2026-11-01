
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
