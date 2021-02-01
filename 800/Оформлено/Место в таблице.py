n = int(input())
ss = []
for _ in range(n):
    s = sum(map(int, input().split()))
    ss.append(s)
    if _ == 0:
        t = s

r = 1
for i in range(1, n):
    if ss[i] > t:
        r += 1
print(r)
