# https://codeforces.com/problemset/problem/581/A

a, b = [int(x) for x in input().split()]
d1 = min(a, b)
a -= d1
b -= d1
d2 = max(a, b) // 2
print(d1, d2)
