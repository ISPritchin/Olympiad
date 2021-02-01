n, m, z = map(int, input().split())
arr = []

i = n
while i <= z:
    arr.append(i)
    i += n

r = 0
i = m
while i <= z:
    if i in arr:
        r += 1
    i += m

print(r)