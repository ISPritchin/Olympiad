n, l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
a.sort()
m = max(a[0], l-a[-1])*2
for i in range(1, len(a)):
    m = max(a[i]-a[i-1], m)
print(m / 2)