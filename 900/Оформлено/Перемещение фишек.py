n = int(input())
a = map(int, input().split())
n0 = n1 = 0
for x in a:
    if x % 2 == 0:
        n0 += 1
    else:
        n1 += 1
print(min(n0, n1))
