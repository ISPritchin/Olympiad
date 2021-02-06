from itertools import combinations

n_sets = int(input())
for _ in range(n_sets):
    a = sorted(list(map(int, input().split())), reverse=True)
    n = 0
    if a[0] >= 1:
        a[0] -= 1
        n += 1
    if a[1] >= 1:
        a[1] -= 1
        n += 1
    if a[2] >= 1:
        a[2] -= 1
        n += 1
    a.sort(reverse=True)
    if a[0] >= 1 and a[1] >= 1:
        n += 1
        a[0] -= 1
        a[1] -= 1
    if a[0] >= 1 and a[2] >= 1:
        n += 1
        a[0] -= 1
        a[2] -= 1
    if a[1] >= 1 and a[2] >= 1:
        n += 1
        a[1] -= 1
        a[2] -= 1
    if a[0] >= 1 and a[1] >= 1 and a[2] >= 1:
        n += 1
    print(n)
