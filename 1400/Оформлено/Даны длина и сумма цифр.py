m, s = map(int, input().split())
if m == 1 and s == 0:
    print(0, 0)
elif m * 9 < s or s == 0:
    print("-1 -1")
else:
    ds = s
    min = [0] * m
    i = m-1
    while s != 0:
        if s > 9:
            min[i] = 9
        else:
            min[i] = s
            min[i] -= 1
            min[0] += 1
        s -= max[i]
        i -= 1
    min = "".join(map(str, min))

    s = ds
    max = [0] * m
    i = 0
    while s != 0:
        if s > 9:
            max[i] = 9
        else:
            max[i] = s
        s -= max[i]
        i += 1
    max = "".join(map(str, max))

    print(min, max)