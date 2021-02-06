n = int(input())
a = [int(x) for x in input().split()]
res = 1
n = 0
for i in range(1, len(a)):
    if a[i-1] <= a[i]:
        n += 1
    else:
        n += 1
        res = max(n, res)
        n = 0
else:
    n += 1
    res = max(n, res)
print(res)
