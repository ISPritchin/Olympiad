n = int(input())
a = list(map(int, input().split()))

current = a[0]
b = []
n = 1
for x in a[1:]:
    if x == current:
        n += 1
    else:
        b.append(n)
        n = 1
        current = x
b.append(n)

print(max([min(b[i], b[i+1]) for i in range(len(b)-1)])*2)