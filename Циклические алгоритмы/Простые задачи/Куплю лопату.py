# https://codeforces.com/problemset/problem/732/A

cost, r = [int(x) for x in input().split()]
for n in range(1, 10):
    if cost*n % 10 == r or cost*n % 10 == 0:
        print(n)
        break
