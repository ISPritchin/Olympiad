n, b, d = map(int, input().split())
a = map(int, input().split())

s = 0
r = 0
for x in a:
    if x > b:
        continue
    s += x
    if s > d:
        r += 1
        s = 0
print(r)
