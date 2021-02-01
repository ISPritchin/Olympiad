from math import sqrt


def is_prime(x):
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True


n, m = map(int, input().split())
for x in range(n+1, m+1):
    if is_prime(x):
        if x == m:
            print("YES")
        else:
            print("NO")
        break
else:
    print("NO")
