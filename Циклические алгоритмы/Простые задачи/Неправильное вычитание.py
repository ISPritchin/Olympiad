n, k = map(int, input().split())
res = n
for i in range(k):
    if res % 10 == 0:
        res //= 10
    else:
        res -= 1
print(res)
