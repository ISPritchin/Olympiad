n_sets = int(input())
for i in range(n_sets):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if 2*a < b:
        print(a*(x+y))
    else:
        nb = min(x, y)
        na = max(x, y) - nb
        print(nb*b + na*a)