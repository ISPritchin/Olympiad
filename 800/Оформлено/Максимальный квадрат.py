n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(len(arr)):
        if arr[i] >= n-i:
            print(n-i)
            break
