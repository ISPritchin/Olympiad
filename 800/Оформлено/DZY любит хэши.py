p, n = map(int, input().split())
a = [0] * 300

col_index = -1
for i in range(n):
    v = int(input()) % p
    if col_index == -1:
        if a[v] == 0:
            a[v] += 1
        else:
            col_index = i + 1

print(col_index)