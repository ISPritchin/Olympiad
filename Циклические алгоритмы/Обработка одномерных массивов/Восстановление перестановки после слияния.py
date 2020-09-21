# https://codeforces.com/problemset/problem/1385/B

N_SETS = int(input())

for i in range(N_SETS):
    _ = int(input())
    p = [int(x) for x in input().split()]
    r = []
    for x in p:
        if x not in r:
            r.append(x)
    for x in r:
        print(x, end=" ")
    print()
