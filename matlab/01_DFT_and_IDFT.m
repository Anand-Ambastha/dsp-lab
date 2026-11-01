
clc; clear all; close all;

x = [1 3 -1 -2];
N = length(x);

for k = 0:N-1
    X(k+1) = 0;
    for n = 0:N-1
        X(k+1) = X(k+1) + x(n+1)*exp(-1i*2*pi*k*n/N);
    end
end

disp('DFT:');
disp(X);

X = [1 2-5i -1 2+5i];

for n = 0:N-1
    x(n+1) = 0;
    for k = 0:N-1
        x(n+1) = x(n+1) + X(k+1)*exp(1i*2*pi*k*n/N);
    end
    x(n+1) = x(n+1)/N;
end

disp('IDFT:');
disp(x);
