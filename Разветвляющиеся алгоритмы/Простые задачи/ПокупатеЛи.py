# https://codeforces.com/contest/1369/submission/91160476

n = int(input())
for i in range(n):
    x = int(input())
    if x % 4 == 0:
        print("YES")
    else:
        print("NO")
