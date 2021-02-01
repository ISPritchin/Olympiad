n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*arr[::-1])