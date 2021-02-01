n = int(input())
for i in range(n):
    start, finish, a, b = [int(x) for x in input().split()]
    if (finish - start) % (a + b) == 0:
        print((finish - start) // (a + b))
    else:
        print(-1)
