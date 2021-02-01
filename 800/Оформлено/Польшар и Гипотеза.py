from math import sqrt


def is_prime(x):
    if x == 1:
        return False
    if x % 2 == 0:
        return True
    for i in range(3, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


n = int(input())
if n % 2 == 1:
    if n == 1:
        print(3)
    else:
        print(1)
else:
    for m in range(1, 100):
        if not is_prime(m*n+1):
            print(m)
            break

