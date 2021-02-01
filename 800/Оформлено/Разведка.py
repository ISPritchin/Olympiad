n, d = map(int, input().split())
a = list(map(int, input().split()))
p = 0
for i, x in enumerate(a):
    for j, y in enumerate(a):
        if i != j and abs(x-y) <= d:
            p += 1
print(p)