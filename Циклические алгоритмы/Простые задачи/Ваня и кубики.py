# https://codeforces.com/problemset/problem/492/A

n = int(input())
l = 1
i = 2
res = 0
while n >= l:
    res += 1
    n -= l
    l += i
    i += 1
print(res)
