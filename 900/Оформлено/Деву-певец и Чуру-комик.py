n, d = map(int, input().split())
ts = list(map(int, input().split()))

s = sum(ts)

if s + 10 * (n - 1) > d:
    print(-1)
else:
    print((d - s) // 5)
