n = int(input())

_ = list(map(int, input().split()))
s = []
for i, x in enumerate(_, 1):
    s.append((i, x))

a = sorted(s, key=lambda x: x[1], reverse=True)

r = 0
n = 0
for _, x in a:
    r += x*n + 1
    n += 1
print(r)

for i, _ in a:
    print(i, end=" ")
