a = input()
bs = input().split()
for b in bs:
    if a[0] == b[0] or a[1] == b[1]:
        print("YES")
        break
else:
    print("NO")
