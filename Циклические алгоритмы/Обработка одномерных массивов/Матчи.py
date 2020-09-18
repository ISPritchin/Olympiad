# https://codeforces.com/problemset/problem/268/A

h_forms = [0] * 101
a_forms = [0] * 101
n = int(input())
for i in range(n):
    h, a = map(int, input().split())
    h_forms[h] += 1
    a_forms[a] += 1

s = 0
for h, g in zip(h_forms, a_forms):
    s += h*g
print(s)
