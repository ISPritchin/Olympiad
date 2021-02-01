n_sets = int(input())

for _ in range(n_sets):
    n, x, a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    max_d = n - 1
    current_d = b - a
    m = current_d + x
    if m >= max_d:
        print(max_d)
    else:
        print(m)
