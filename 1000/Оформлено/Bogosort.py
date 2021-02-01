n_sets = int(input())

for _ in range(n_sets):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(*a)
