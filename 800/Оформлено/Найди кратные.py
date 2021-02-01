n_sets = int(input())
for i in range(n_sets):
    l, r = map(int, input().split())
    x = l
    y = r // l * l
    print(x, y)
