# https://codeforces.com/problemset/problem/59/A

s = input()
lower = upper = 0
for c in s:
    if ord("A") <= ord(c) <= ord("Z"):
        upper += 1
    else:
        lower += 1
if lower >= upper:
    print(s.lower())
else:
    print(s.upper())
