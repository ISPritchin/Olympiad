n = int(input())
arr = sorted(list(map(int, input().split())))
r = 0
for i in range(0, n, 2):
    r += arr[i+1] - arr[i]
print(r)
