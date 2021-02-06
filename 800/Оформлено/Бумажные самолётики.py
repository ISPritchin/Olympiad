from math import ceil

k, n, s, p = map(int, input().split())
n_sheets = ceil(n / s)* k
n_p = ceil(n_sheets / p)
print(n_p)