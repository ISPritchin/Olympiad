n_sets = int(input())
for i in range(n_sets):
    a, b, n = [int(x) for x in input().split()]
    if n % 2 == 0:
        print(n // 2 * (a-b))
    else:
        print(n // 2 * (a-b) + a)
