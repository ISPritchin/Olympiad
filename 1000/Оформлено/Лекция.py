n, m = map(int, input().split())

d = {}
for i in range(m):
    a, b = input().split()
    if len(a) <= len(b):
        d[a] = a
    else:
        d[a] = b

lecture = input().split()
for word in lecture:
    print(d[word], end=' ')