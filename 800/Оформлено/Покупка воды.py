n_sets = int(input())
for i in range(n_sets):
    n, a, b = map(int, input().split())
    v1 = a*n
    v2 = n // 2 * b + n % 2 * a
    print(min(v1, v2))
