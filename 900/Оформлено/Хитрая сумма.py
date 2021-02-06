n_sets = int(input())
for _ in range(n_sets):
    t = int(input())
    s = (1 + t)*t // 2
    i = 0
    while (p := 2**i) <= t:
        s -= 2*p
        i += 1
    print(s)