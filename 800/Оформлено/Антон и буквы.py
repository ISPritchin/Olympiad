s = input()
if s == "{}":
    print(0)
else:
    letters = set(s[1:-1].split(", "))
    print(len(letters))
