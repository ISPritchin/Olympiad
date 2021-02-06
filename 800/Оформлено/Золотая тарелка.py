w, h, k = map(int, input().split())
r = 0
while k != 0:
    r += w*h - ((w-2)*(h-2))
    w -= 4
    h -= 4
    k -= 1
print(r)
