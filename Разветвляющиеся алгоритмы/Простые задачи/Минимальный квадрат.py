# https://codeforces.com/problemset/problem/1360/A

n = int(input())
for i in range(n):
    a, b = [int(x) for x in input().split()]
    a,b = min(a, b), max(a, b)
    if a*2 > b:
        print((a*2)**2)
    else:
        print(b**2)
