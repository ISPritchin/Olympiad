n, t = map(int, input().split())
_min = 10**(n-1)
_max = 10**n-1

if _min // t != _max // t:
    print(_max // t * t)
else:
    print(-1)
