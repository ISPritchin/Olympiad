n_sets = int(input())
for i in range(n_sets):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    m = arr[0]
    r = 0
    for i in range(1, len(arr)):
        r += (k - arr[i]) // m
    print(r)
