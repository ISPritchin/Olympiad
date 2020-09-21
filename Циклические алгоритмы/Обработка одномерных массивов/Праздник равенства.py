# https://codeforces.com/problemset/problem/758/A

n = int(input())
xs = [int(x) for x in input().split()]
if n == 1:
    print(0)
else:
    m = max(xs)
    print(sum((m - x for x in xs)))
