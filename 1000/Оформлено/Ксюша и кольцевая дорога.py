n, k = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
res = 0
last = 1
for x in d:
    if x >= last:
        res += x - last
    else:
        res += n - last + x
    last = x
print(res)