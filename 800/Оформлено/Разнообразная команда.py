n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
for i, x in enumerate(arr, 1):
    if x not in d:
        d[x] = i

if len(d) < k:
    print("NO")
else:
    i = 1
    print("YES")
    print(*list(d.values())[:k])
