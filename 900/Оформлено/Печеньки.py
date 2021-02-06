n = int(input())
a = map(int, input().split())

n0 = n1 = 0
for x in a:
    if x % 2 == 0:
        n0 += 1
    else:
        n1 += 1

if n0 == 0 and n1 % 2 == 1:
    print(n1)
elif n0 == 0 and n1 % 2 == 0:
    print(0)
elif n1 == 0:
    print(n0)
else:
    if n1 % 2 == 1:
        print(n1)
    else:
        print(n0)
