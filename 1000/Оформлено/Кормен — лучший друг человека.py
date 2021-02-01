n, k = map(int, input().split())
a = list(map(int, input().split()))

n_add = 0
for i in range(1, n):
    if a[i-1] + a[i] < k:
        delta = k - (a[i-1] + a[i])
        n_add += delta
        a[i] += delta

print(n_add)
print(*a)
