from math import sqrt


def get_ld(x):
    last_div = 1
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            last_div = i
    return last_div

x = int(input())
d = get_ld(x)
print(d, x // d)
