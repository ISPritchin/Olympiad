# https://codeforces.com/problemset/problem/116/A

n = int(input())
res = 0
state = 0
for i in range(n):
    out, to = map(int, input().split())
    state = state - out + to
    res = max(res, state)
print(res)