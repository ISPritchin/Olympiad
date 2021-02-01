n = int(input())
a = list([int(x) for x in input().split()])
i = 1
res = 1
ans = 1

while i != n:
    if a[i - 1] < a[i]:
        res += 1
    else:
        ans = max(res, ans)
        res = 1
    i += 1
ans = max(res, ans)
print(ans)
