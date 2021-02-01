n_sets = int(input())
for i in range(n_sets):
    print(sum([int(x) for x in input().split()]) // 2)
