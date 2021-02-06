from math import sqrt


def is_prime(x):
    if x == 1:
        return False
    if x % 2 == 0 and x != 2:
        return False
    for i in range(3, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    a = 1
    j = 1
    b = 1
    while True:
        if is_prime(n-1+b) and not is_prime(b):
            break
        b += 1
    L = [b] + (n - 1) * [a]
    for i in range(n):
        L[i] = b
        print(*L)
        L[i] = a
