# https://codeforces.com/problemset/problem/1358/A

N_SETS = int(input())

for i in range(N_SETS):
    a, b = [int(x) for x in input().split()]
    s = a * b
    print(s // 2 + int(s % 2 != 0))
