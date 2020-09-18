# https://codeforces.com/problemset/problem/263/A

n_rows = 5
for i in range(n_rows):
    line = list(map(int, input().split()))
    if 1 in line:
        row = i
        col = line.index(1)

print(abs(row-2)+abs(col-2))