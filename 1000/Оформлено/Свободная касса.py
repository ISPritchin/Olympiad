n = int(input())
hl, ml = map(int, input().split())
r = 1
r_max = 1

for i in range(1, n):
    hc, mc = map(int, input().split())
    if hc == hl and mc == ml:
        r += 1
    else:
        r_max = max(r_max, r)
        r = 1
    hl, ml = hc, mc
r_max = max(r_max, r)

print(r_max)
