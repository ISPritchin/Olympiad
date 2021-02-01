from math import ceil

n_sets = int(input())

for _ in range(n_sets):
    a, b = list(map(int, input().split()))
    a, b = min(a, b), max(a, b)

    if b % a != 0:
        print(-1)
    else:
        k = b // a
        i = 0
        while k != 1 and k % 2 == 0:
            k //= 2
            i += 1
        if k != 1 or b % a != 0:
            print(-1)
        else:
            print(ceil(i / 3))
