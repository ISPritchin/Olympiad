from math import ceil

n_sets = int(input())
for i in range(n_sets):
    n, x = map(int, input().split())
    if n <= 2:
        print(1)
    else:
        print(2 + ceil((n - 3) // x))
