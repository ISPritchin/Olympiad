n = int(input())
arr = list(map(int, input().split()))
arr += [arr[0]]
delta = float("inf")

a = b = 0
for i in range(1, len(arr)):
    if abs(arr[i] - arr[i-1]) < delta:
        a = i
        if i + 1 > n:
            b = 1
        else:
            b = i+1
        delta = abs(arr[i] - arr[i-1])
print(a, b)