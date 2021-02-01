n_sets = int(input())
for _ in range(n_sets):
    a, b = map(int, input().split())
    print(a ^ b)
