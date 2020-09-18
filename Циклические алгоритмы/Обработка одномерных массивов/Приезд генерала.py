# https://codeforces.com/problemset/problem/144/A

n = int(input())
a = list(map(int, input().split()))
min_a = min(a)
max_a = max(a)
min_i = [i for i, x in enumerate(a) if x == min_a][-1]
max_i = [i for i, x in enumerate(a) if x == max_a][0]
n = max_i + n - min_i - 1
if max_i < min_i:
    print(n)
else:
    print(n - 1)
