# https://codeforces.com/problemset/problem/1030/A

n = int(input())
a = map(int, input().split())
if 1 in a:
    print("HARD")
else:
    print("EASY")
