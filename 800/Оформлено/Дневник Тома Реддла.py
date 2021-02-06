n = int(input())
l = []
for i in range(n):
    s = input()
    if s in l:
        print("YES")
    else:
        print("NO")
        l.append(s)
