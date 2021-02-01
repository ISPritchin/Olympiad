n = int(input())

res = [0, 0, 0]
for i in range(n):
    s = [int(x) for x in input().split()]
    for j in range(3):
        res[j] += s[j]

if res.count(0) == 3:
    print("YES")
else:
    print("NO")