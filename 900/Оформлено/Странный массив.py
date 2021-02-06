from math import ceil

n_sets = int(input())
for _ in range(n_sets):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    _max = sum([ceil(_ / x) for _ in a])
    _min = ceil(sum(a) / x)
    print(_min, _max)
