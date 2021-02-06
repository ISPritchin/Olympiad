a = []
p = []

n = int(input())
for i in range(n):
    _a, _p = map(int, input().split())
    a.append(_a)
    p.append(_p)

p_min = []
m = float("inf")
for x in p:
    m = min(x, m)
    p_min.append(m)

s = 0
for _a, _p in zip(a, p_min):
    s += _a * _p
print(s)
