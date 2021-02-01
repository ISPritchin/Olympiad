n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print(*a)
    print(*b)
