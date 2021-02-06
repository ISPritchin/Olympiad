l, r, a = map(int, input().split())
while a != 0:
    if r > l:
        l += 1
    else:
        r += 1
    a -= 1
print(min(l, r)*2)
