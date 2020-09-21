# https://codeforces.com/problemset/problem/119/A


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b, n = map(int, input().split())
while True:
    r = gcd(a, n)
    if r > n:
        print("1")
        break
    n -= r

    r = gcd(b, n)
    if r > n:
        print("0")
        break
    n -= r
