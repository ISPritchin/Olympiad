_ = input()
s = input()

if len(set((x.lower() for x in s if s.isalpha()))) == 26:
    print("YES")
else:
    print("NO")
