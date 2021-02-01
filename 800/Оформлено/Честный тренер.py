def read_arr():
    return [int(x) for x in input().split()]


N_SETS = int(input())

for i in range(N_SETS):
    _ = int(input())
    a = read_arr()
    a.sort()
    res = float("inf")
    for i in range(1, len(a)):
        delta = a[i] - a[i - 1]
        if delta < res:
            res = delta
    print(res)
