def is_distinct(x):
    x = str(x)
    return len(set(x)) == len(x)


L, R = [int(c) for c in input().split()]
for i in range(L, R + 1):
    if is_distinct(i):
        print(i)
        break
else:
    print(-1)
