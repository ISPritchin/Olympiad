T = int(input())
for i in range(T):
    a, b, n = [int(x) for x in input().split()]
    _min, _max = min(a, b), max(a, b)
    count = 1
    while _min + _max <= n:
        _min, _max = _max, _min + _max
        count += 1
    print(count)
