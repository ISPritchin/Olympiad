n, _, _ = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())

r = [0] * n

for x in a:
    r[x-1] = 1

for x in b:
    r[x-1] = 2

print(*r, sep=" ")