
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
