n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    a = [0] * 101
    for x in map(int, input().split()):
        a[x] += 1
    print(max(a))
