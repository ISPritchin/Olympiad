n = int(input())
f = False
for i in range(n):
    a, b = map(int, input().split()[1:])
    if a >= 2400 and b - a > 0:
        f = True
if f:
    print("YES")
else:
    print("NO")

