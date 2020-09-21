# https://codeforces.com/problemset/problem/1283/A

N_SETS = int(input())
for i in range(N_SETS):
    h, m = [int(x) for x in input().split()]
    print((23-h)*60+(60-m))
