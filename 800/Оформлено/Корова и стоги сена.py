n_sets = int(input())
for _ in range(n_sets):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 2
    while i <= n and d > 0:
        m = min((d // (i-1)), arr[i-1])
        d -= (i-1) * m
        arr[0] += m
        arr[i-1] -= m
        i += 1
    print(arr[0])
