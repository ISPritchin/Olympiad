n = int(input())
r = None
for i in range(1, n):
    if r is not None:
        break
    if i % 3 == 0:
        continue
    for j in range(1, n):
        if r is not None:
            break
        if j % 3 == 0:
            continue
        k = n - i - j
        if k % 3 != 0 and i + j + k == n:
            r = i, j, k

print(*r)
