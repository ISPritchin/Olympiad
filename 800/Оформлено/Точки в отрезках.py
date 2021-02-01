n, m = map(int, input().split())

d = {i: 0 for i in range(1, m + 1)}
for i in range(n):
    l, r = map(int, input().split())
    for a in range(l, r+1):
        d[a] += 1

d = {k: d[k] for k in d if d[k] == 0}

print(len(d))
if len(d) == 0:
    print()
else:
    print(*list(d.keys()))
