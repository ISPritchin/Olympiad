_ = int(input())
s = input()
r = 0
for i, x in enumerate(s, 1):
    d = int(x)
    if d % 2 == 0:
        r += i
print(r)
