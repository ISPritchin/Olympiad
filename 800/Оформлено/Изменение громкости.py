n_sets = int(input())
for i in range(n_sets):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    delta = b - a
    r = 0
    for x in [5, 2, 1]:
        r += delta // x
        delta %= x
    print(r)
