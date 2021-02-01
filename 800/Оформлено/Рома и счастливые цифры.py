n, k = map(int, input().split())
a = input().split()
r = 0
for x in a:
    if x.count("4") + x.count("7") <= k:
        r += 1
print(r)
