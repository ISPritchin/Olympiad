n = int(input())
ls = []
rs = []

for i in range(n):
    l, r = map(int, input().split())
    ls.append(l)
    rs.append(r)
x = int(input())

n_read = 0
for l, r in zip(ls, rs):
    if x > r:
        n_read += 1
    else:
        break
print(n-n_read)
