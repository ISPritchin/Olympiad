# https://codeforces.com/problemset/problem/155/A

_ = int(input())
r = [int(x) for x in input().split()]
_max = r[0]
_min = r[0]
n = 0
for i in range(1, len(r)):
    res = r[i]
    if res > _max:
        n += 1
        _max = res
    elif res < _min:
        n += 1
        _min = res
print(n)
