w, h = map(int, input().split())
u1, d1 = map(int, input().split())
u2, d2 = map(int, input().split())
while h != 0:
    w += h
    if h == d1:
        w = max(0, w - u1)
    elif h == d2:
        w = max(0, w - u2)
    h -= 1
print(w)
