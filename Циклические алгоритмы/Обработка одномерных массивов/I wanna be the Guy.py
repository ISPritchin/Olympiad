# https://codeforces.com/problemset/problem/469/A

n = int(input())
a = set([int(x) for x in input().split()[1:] if int(x) > 0 and int(x) <= n])
b = set([int(x) for x in input().split()[1:] if int(x) > 0 and int(x) <= n])
if len(a | b) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
