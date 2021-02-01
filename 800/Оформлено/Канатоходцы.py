*a, d = map(int, input().split())
a.sort()

a, b, c = a
# смещение центрального

if d <= b - a and d <= c - b:
    print(0)
elif c - a >= 2*d:
    if b - a < c - b:
        print(d - (b - a))
    else:
        print(d - (c - b))
# движение от центра
else:
    ad = max(d - (b - a), 0)
    cd = max(d - (c - b), 0)
    print(ad + cd)