n_sets = int(input())
for i in range(n_sets):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(sum(arr[-k-1:]))