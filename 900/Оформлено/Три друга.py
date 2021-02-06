n_sets = int(input())
for _ in range(n_sets):
    a, b, c = sorted(list(map(int, input().split())))
    d1 = b - a
    d2 = c - b
    if d1 <= 1 and d2 <= 1:
        print(0)
    else:
        print(2*(c-a-2))
