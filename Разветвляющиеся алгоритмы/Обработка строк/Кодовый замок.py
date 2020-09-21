# https://codeforces.com/contest/540/submission/91751046


def f(p):
    a, b = min(p), max(p)
    return min(b - a, 10 - b + a)


_ = int(input())
a = map(int, list(input()))
b = map(int, list(input()))
print(sum(map(f, zip(a, b))))
