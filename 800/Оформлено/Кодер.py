from math import ceil

n = int(input())
print(ceil(n*n / 2))
a = ("C." * n)[:n]
b = ("C." * n)[1:n+1]

for i in range(n):
    if i % 2 == 0:
        print(a)
    else:
        print(b)
