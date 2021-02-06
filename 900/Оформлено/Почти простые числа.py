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


n = int(input())
k = 0
for i in range(1, n+1):
    if not is_prime(i):
        r = 0
        for j in range(2, i+1):
            if i % j == 0 and is_prime(j):
                r += 1
                if r > 2:
                    break
        else:
            if r == 2:
                k += 1
print(k)