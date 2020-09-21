# https://codeforces.com/problemset/problem/1367/A

n = int(input())
for i in range(n):
    s = input()
    print(s[::2] + s[-1])
