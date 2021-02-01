n_sets = int(input())

for _ in range(n_sets):
    n_bottom, n_left = map(int, input().split())
    b = list(map(int, input().split()))
    l = list(map(int, input().split()))
    r = 0
    for x in b:
        if x in l:
            r += 1
    print(r)
