n_sets = int(input())

for _ in range(n_sets):
    _ = int(input())
    a = map(int, input().split())
    r_min = 0
    r = 0
    for x in a:
        r += x
        r_min = min(r, r_min)
    print(-r_min)
