n_sets = int(input())

for _ in range(n_sets):
    n, k = map(int, input().split())
    row = (k - 1) // (n - 1)
    col = (k - 1) % (n - 1)
    print(1 + row*n + col)
