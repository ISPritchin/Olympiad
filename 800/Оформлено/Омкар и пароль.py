n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1:
        print(len(arr))
    else:
        print(1)