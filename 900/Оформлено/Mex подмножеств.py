n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    a = list(map(int, input().split()))
    v = [0] * 101
    for x in a:
        v[x] += 1

    i2 = 0
    while v[i2] >= 2:
        i2 += 1
    i1 = 0
    while v[i1] >= 1:
        i1 += 1
    print(i1 + i2)