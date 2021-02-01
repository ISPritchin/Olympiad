n = int(input())
c = 1
for i in range(1, n):
    c = (c + i) % n
    if c == 0:
        print(n, end=' ')
    else:
        print(c, end=' ')