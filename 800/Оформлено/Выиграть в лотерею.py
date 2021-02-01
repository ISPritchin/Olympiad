banknotes = [100, 20, 10, 5, 1]
s = int(input())
res = 0
for x in banknotes:
    res += s // x
    s = s % x
print(res)
