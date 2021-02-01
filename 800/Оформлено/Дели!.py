n_sets = int(input())
for i in range(n_sets):
    x = int(input())
    n = 0
    while x != 1:
        if x % 2 == 0:
            n += 1
            x //= 2
        elif x % 3 == 0:
            n += 2
            x //= 3
        elif x % 5 == 0:
            n += 3
            x //= 5
        else:
            n = -1
            break
    print(n)
