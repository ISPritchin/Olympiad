# https://codeforces.com/problemset/problem/1371/A

N_SETS = int(input())

for i in range(N_SETS):
    x = int(input())
    print(x // 2 + x % 2)
