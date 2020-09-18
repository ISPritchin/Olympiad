# https://codeforces.com/problemset/problem/271/A

y = int(input())
while True:
    y += 1
    if len(set(list(str(y)))) == 4:
        print(y)
        break
