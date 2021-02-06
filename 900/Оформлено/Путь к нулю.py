n_sets = int(input())
for _ in range(n_sets):
    n, k = map(int, input().split())
    r = 0
    while n != 0:
        if n % k == 0:
            n //= k
            r += 1
        else:
            r += (n % k)
            n -= (n % k)
    print(r)
