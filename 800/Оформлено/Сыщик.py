s = input()
for i in reversed(range(len(s))):
    if s[i].isalpha():
        c = s[i]
        break

if c.upper() in "A, E, I, O, U, Y":
    print("YES")
else:
    print("NO")
