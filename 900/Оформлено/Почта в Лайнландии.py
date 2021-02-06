n = int(input())
a = list(map(int, input().split()))
s = sum(a)

_mins = [0] * n
_maxs = [0] * n

for i in range(1, n-1):
    _mins[i] = min(a[i] - a[i-1], a[i+1] - a[i])
    _maxs[i] = max(a[i] - a[0], a[-1] - a[i])
_mins[0] = a[1] - a[0]
_mins[-1] = a[-1] - a[-2]
_maxs[0] = _maxs[-1] = a[-1] - a[0]

for a, b in zip(_mins, _maxs):
    print(a, b)


