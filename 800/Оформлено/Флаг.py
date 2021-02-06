n, m = map(int, input().split())

last = -1
flag = True
for i in range(n):
    s = input()
    if flag:
        color = int(s[0])
        if len(set(s)) > 1 or color == last:
            flag = False
        last = color

if flag:
    print("YES")
else:
    print("NO")

