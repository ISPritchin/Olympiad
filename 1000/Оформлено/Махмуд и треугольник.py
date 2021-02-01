n = int(input())
a = list(map(int, input().split()))
a.sort()
for b, c, d in zip(a, a[1:], a[2:]):
    if b + c > d:
        print("YES")
        break
else:
    print("NO")
