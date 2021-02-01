n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    max = 4*n - 2
    for i in range(n):
        print(max, end=' ')
        max -= 2
    print()
