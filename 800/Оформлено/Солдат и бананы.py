k, w, n = map(int, input().split())
s = (1 + n)/2 * n*k
d = int(s-w)
if d < 0:
    print(0)
else:
    print(d)
