_ = input()
arr = map(int, input().split())
d = {}
for x in arr:
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

max_height = 0
for k in d:
    max_height = max(max_height, d[k])
print(max_height, len(d))