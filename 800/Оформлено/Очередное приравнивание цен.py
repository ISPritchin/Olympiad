from math import ceil

n_sets = int(input())
for i in range(n_sets):
    _ = input()
    a = list(map(int, input().split()))
    print(ceil(sum(a) / len(a)))
