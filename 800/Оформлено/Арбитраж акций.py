n, m, r = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(int, input().split()))
min_s = min(s)
max_b = max(b)
if min_s >= max_b:
    print(r)
else:
    print(r % min_s + r // min_s * max_b)
