
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

N1 = length(x);
N2 = length(h);
N = max(N1,N2);

x = [x zeros(1,N-N1)];
h = [h zeros(1,N-N2)];

for n = 0:N-1
    y(n+1) = 0;
    for k = 0:N-1
        y(n+1) = y(n+1) + x(k+1)*h(mod(n-k,N)+1);
    end
end

disp('Circular convolution:');
disp(y);
stem(y);
