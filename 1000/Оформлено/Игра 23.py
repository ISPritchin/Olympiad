a, b = map(int, input().split())

r = 0
while a != b:
    k = b // a
    if k % 2 == 0:
        a *= 2
        r += 1
    elif k % 3 == 0:
        a *= 3
        r += 1
    else:
        break

if a == b:
    print(r)
else:
    print(-1)
