# https://codeforces.com/problemset/problem/136/A

n = int(input())
r = [0] * n
a = list(map(int, input().split()))
for i in range(n):
    r[a[i]-1] = i+1
for x in r:
    print(x, end=" ")
