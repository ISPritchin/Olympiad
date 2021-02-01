n = int(input())
for i in range(n):
    a, b = [int(x) for x in input().split()]
    d = b - a
    if d == 0:
        print(0)
    elif d > 0 and d % 2 == 0 or d < 0 and d % 2 == 1:
        print(2)
    else:
        print(1)
