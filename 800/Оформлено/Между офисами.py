n = int(input())
s = input()
FS = s.count("FS")
SF = s.count("SF")
if SF > FS:
    print("YES")
else:
    print("NO")
