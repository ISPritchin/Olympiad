n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = 0
r = 0
while i < n and i < m and a[i] < 0:
    r += abs(a[i])
    i += 1
print(r)
