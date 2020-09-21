# https://codeforces.com/problemset/problem/432/A

n, k = [int(x) for x in input().split()]
xs = [int(x) for x in input().split() if int(x) <= 5-k]
print(len(xs) // 3)
