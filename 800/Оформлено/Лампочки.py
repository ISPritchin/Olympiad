n, m = map(int, input().split())
arr = [0] * m
for i in range(n):
    a = list(map(int, input().split()))
    for x in a[1:]:
        x -= 1
        arr[x] = 1

if arr.count(0):
    print("NO")
else:
    print("YES")
