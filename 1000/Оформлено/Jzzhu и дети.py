from math import ceil

n, m = map(int, input().split())
a = list(map(lambda x: ceil(int(x) / m), input().split()))

_max = a[0]
_max_ind = 1
for i in range(1, n):
    if a[i] >= _max:
        _max = a[i]
        _max_ind = i + 1

print(_max_ind)
