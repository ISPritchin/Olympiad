# https://codeforces.com/problemset/problem/427/A

n = int(input())
s = (int(x) for x in input().split())
n_policemen = 0
res = 0
for x in s:
    if x == -1:
        if n_policemen == 0:
            res += 1
        else:
            n_policemen -= 1
    else:
        n_policemen += x
print(res)
