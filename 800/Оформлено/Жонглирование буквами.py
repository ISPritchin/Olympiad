from collections import Counter

n = int(input())
for i in range(n):
    n_s = int(input())
    a = [Counter(list(input())) for _ in range(n_s)]
    r = {chr(c): 0 for c in range(ord("a"), ord("z") + 1)}
    for d in a:
        for k in d:
            r[k] += d[k]
    for k in r:
        if r[k] % n_s != 0:
            print("NO")
            break
    else:
        print("YES")
