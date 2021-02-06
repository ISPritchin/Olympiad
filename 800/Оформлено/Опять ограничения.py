n, h_max, m = map(int, input().split())

a = [h_max] * n
for i in range(m):
    l, r, x = map(int, input().split())
    for i in range(l, r+1):
        a[i-1] = min(a[i-1], x)

r = 0
for x in a:
    r += x**2
print(r)