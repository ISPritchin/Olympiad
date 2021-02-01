x, n = [int(x) for x in input().split()]
for i in range(n):
    if x % 10 == 0:
        x //= 10
    else:
        x -= 1
print(x)
