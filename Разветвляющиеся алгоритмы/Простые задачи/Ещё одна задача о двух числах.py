# https://codeforces.com/problemset/problem/1409/A

N_SETS = int(input())
for _ in range(N_SETS):
    a, b = [int(x) for x in input().split()]
    a, b = min(a, b), max(a, b)
    print((b-a) // 10 + int((b-a) % 10 != 0))
