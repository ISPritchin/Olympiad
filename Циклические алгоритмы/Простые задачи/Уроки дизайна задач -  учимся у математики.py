# https://codeforces.com/problemset/problem/472/A
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
for i in range(2, n):
    if not is_prime(i) and not is_prime(n - i):
        print(i, n - i)
        break
