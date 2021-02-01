n = int(input())
arr = list(map(int, input().split()))[::-1]
r = []
for i in range(len(arr)):
    if arr[i] not in r:
        r.append(arr[i])
print(len(r))
print(*r[::-1])
