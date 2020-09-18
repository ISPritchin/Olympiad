# https://codeforces.com/problemset/problem/282/A

n_operations = int(input())

x = 0
for _ in range(n_operations):
    operation = input()
    if operation[0] == "+" or operation[2] == "+":
        x += 1
    else:
        x -= 1
print(x)
