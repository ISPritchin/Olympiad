# https://codeforces.com/problemset/problem/1154/A

a = list(map(int, input().split()))
a.sort()
_max = max(a)
for x in a[:-1]:
    print(_max - x, end=" ")