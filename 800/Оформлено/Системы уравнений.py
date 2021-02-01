n, m = map(int, input().split())
flag = False
r = 0
for a in range(1000):
    for b in range(1000):
        if a*a + b == n and a + b*b == m:
            r += 1
print(r)
