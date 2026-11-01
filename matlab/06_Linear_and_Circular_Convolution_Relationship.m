
clc; clear all; close all;

x = [1 2 0 1];
h = [1 5 7 3];

% Linear convolution
y = conv(x,h);

% Circular convolution by folding
N = max(length(x),length(h));
yc = zeros(1,N);

for k = 1:length(y)
    index = mod(k-1,N)+1;
    yc(index) = yc(index)+y(k);
end

% Linear convolution using circular convolution
M = length(x)+length(h)-1;
x1 = [x zeros(1,M-length(x))];
h1 = [h zeros(1,M-length(h))];

for n = 0:M-1
    z(n+1) = 0;
    for k = 0:M-1
        z(n+1) = z(n+1)+x1(k+1)*h1(mod(n-k,M)+1);
    end
end

disp('Linear convolution:');
disp(y);
disp('Circular convolution by folding:');
disp(yc);
disp('Zero-padded circular convolution:');
disp(z);
