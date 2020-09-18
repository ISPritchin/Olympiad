# https://codeforces.com/problemset/problem/158/A

_, k = map(int, input().split())
res = list(map(int, input().split()))
p_ball = res[k-1]
n = 0
for x in res:
    if x > 0 and x >= p_ball:
        n += 1
    else:
        break
print(n)
