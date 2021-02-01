x1, y1, x2, y2 = map(int, input().split())
if x1 == x2:
    a = abs(y1-y2)
    if x1 + a <= 1000:
        print(x1+a, y1, x2+a, y2)
    else:
        print(x1-a, y1, x2-a, y2)
elif y1 == y2:
    a = abs(x1-x2)
    if y1 + a <= 1000:
        print(x1, y1+a, x2, y2+a)
    else:
        print(x1, y1-a, x2, y2-a)
else:
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx != dy:
        print(-1)
    else:
        print(x1, y2, x2, y1)
