# https://codeforces.com/problemset/problem/1296/A

n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    a = [int(x) for x in input().split()]
    n_ch = len(list(filter(lambda x: x % 2 == 1, a)))
    if n % 2 == 1 and n_ch != 0:
        print("YES")
    elif n_ch != 0 and n_ch != n:
        print("YES")
    else:
        print("NO")
