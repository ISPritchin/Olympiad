n, k = map(int, input().split())
s = input()
i1 = s.find("G")
i2 = s.find("T")
i1, i2 = min(i1, i2), max(i1, i2)

flag = True
while i1 < i2:
    if s[i1] == "#":
        flag = False
        break
    else:
        i1 += k

if i1 == i2 and flag:
    print("YES")
else:
    print("NO")
