k, n = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
m = float("inf")
for i in range(n-k+1):
    if m > a[i+k-1] - a[i]:
        m = a[i+k-1] - a[i]
print(m)
