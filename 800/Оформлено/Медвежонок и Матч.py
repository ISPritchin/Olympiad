n = int(input())
a = list(map(int, input().split()))
a.append(0)
a.append(91)
a = sorted(a)
last = 0
for x in a:
    if x - last > 15:
        print(last + 15)
        break
    last = x
else:
    print(90)

