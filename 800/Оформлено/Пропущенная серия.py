n = int(input())
arr = [0] * n
series = map(int, input().split())
for s in series:
    arr[s-1] = 1
print(arr.index(0)+1)

