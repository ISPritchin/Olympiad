n_sets = int(input())
for _ in range(n_sets):
    r, g, b, w = map(int, input().split())
    confs = [[r, g, b, w]]
    if r > 0 and g > 0 and b > 0:
        confs.append([r-1, g-1, b-1, w+3])
    for conf in confs:
        r, g, b, w = map(lambda x: x % 2, conf)
        if r + g + b + w == 0 or r + g + b + w == 1:
            print("YES")
            break
    else:
        print("NO")
