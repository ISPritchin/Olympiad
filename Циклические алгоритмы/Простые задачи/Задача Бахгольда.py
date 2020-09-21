# https://codeforces.com/problemset/problem/749/A

x = int(input())
print(x // 2)
n_3 = int(x % 2 == 1)
n_2 = x // 2 - int(x % 2 == 1)
for i in range(n_2):
    print(2, end=" ")
if n_3:
    print(3, end="")
