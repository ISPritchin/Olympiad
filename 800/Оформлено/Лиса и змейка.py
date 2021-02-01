m, n = [int(x) for x in input().split()]

b = -1
c = -3
for i in range(m):
    if i % 2 == 0:
        print('#' * n)
    elif b % 4 == 0:
        print('.' * (n - 1) + '#')
    elif c % 4 == 0:
        print('#' + '.' * (n - 1))
    b += 1
    c += 1