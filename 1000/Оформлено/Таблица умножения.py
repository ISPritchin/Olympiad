    from math import sqrt

    n, x = map(int, input().split())

    r = 0
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            a = x // i
            b = x // a
            if a <= n and b <= n:
                if a == b:
                    r += 1
                else:
                    r += 2
    print(r)
