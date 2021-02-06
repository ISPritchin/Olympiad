n = int(input())
a = [int(x) for x in input().split()]
a.sort(reverse=True)
s = sum(a)
r = 0
i = 0
while r <= s:
    r += a[i]
    s -= a[i]
    i += 1
print(i)
