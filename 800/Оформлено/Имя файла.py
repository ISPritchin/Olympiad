n = int(input())
s = input()
n = 0
res = 0
for x in s:
    if x == 'x':
        n += 1
        if n >= 3:
            res += 1
    else:
        n = 0
print(res)
