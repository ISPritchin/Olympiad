n_sets = int(input())
for i in range(n_sets):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    max_a = max(arr)
    min_a = min(arr)
    delta = max_a - min_a
    if k % 2 == 1:
        for x in arr:
            print(max_a-x, end=" ")
    else:
        for x in arr:
            print(x-min_a, end=" ")
    print()
