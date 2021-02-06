a = list(map(int, input().split()))
t = [0] * 101
r = [0] * 101
for x in a:
    t[x] += 1
for i in range(len(r)):
    if t[i] >= 2:
        r[i] = min(3, t[i]) * i
print(sum(a) - max(r))
