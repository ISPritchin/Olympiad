n_sets = int(input())
for i in range(n_sets):
    s = sum(list(map(int, input().split())))
    print(s - 1)
