from math import gcd

n = int(input())
ch = n // 2
zn = n - ch
while ch != 0:
    if gcd(ch, zn) == 1:
        print(ch, zn)
        break
    ch -= 1
    zn += 1

