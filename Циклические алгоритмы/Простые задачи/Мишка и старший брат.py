# https://codeforces.com/problemset/problem/791/A

lim, bob = map(int, input().split())
n = 0
while lim <= bob:
    lim *= 3
    bob *= 2
    n += 1
print(n)