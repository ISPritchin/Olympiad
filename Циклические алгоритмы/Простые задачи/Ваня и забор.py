# https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())
hs = map(int, input().split())
res = 0
for r in hs:
    if r > h:
        res += 2
    else:
        res += 1
print(res)
