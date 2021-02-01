n = int(input())
cons = list(map(int, input().split()))
cons.sort()
i = 0
while i < len(cons) and cons[i] == 0:
    i += 1

r = 0
if i != len(cons):
    old = 0
    for j in range(i, len(cons)):
        if cons[j] == old:
            r += 1
            if flag:
                r = -1
                break
            flag = True
        else:
            flag = False
        old = cons[j]
print(r)
