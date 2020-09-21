# https://codeforces.com/problemset/problem/1348/A

n = int(input())
for i in range(n):
    m = int(input())
    r = [2**j for j in range(1, m+1)]
    print(r[-1] + sum(r[:len(r) // 2-1]) - sum(r[len(r) // 2-1 :-1]))
