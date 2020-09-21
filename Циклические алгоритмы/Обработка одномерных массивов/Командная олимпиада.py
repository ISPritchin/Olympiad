# https://codeforces.com/problemset/problem/490/A

_ = int(input())
a = []
b = []
c = []
xs = [int(x) for x in input().split()]
for i, x in enumerate(xs, start=1):
    if x == 1:
        a.append(i)
    elif x == 2:
        b.append(i)
    else:
        c.append(i)

n_commands = min(len(a), len(b), len(c))
print(n_commands)
for _a, _b, _c in zip(a, b, c):
    print(_a, _b, _c)
