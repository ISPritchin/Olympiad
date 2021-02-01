n_sets = int(input())
for _ in range(n_sets):
    n, m, r, c = map(int, input().split())
    h1 = m - c
    h2 = c - 1
    w1 = n - r
    w2 = r - 1
    max_h = max(h1, h2)
    max_w = max(w1, w2)
    print(max_h + max_w)

