from math import ceil

n_sets = int(input())
for _ in range(n_sets):
    a, b, c, d, k = map(int, input().split())
    x = ceil(a / c)
    y = ceil(b / d)
    if x + y > k:
        print(-1)
    else:
        print(x, y)