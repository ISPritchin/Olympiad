s = input()
if s in "a1a8h1h8":
    print(3)
elif s[0] in "ah" or s[1] in "18":
    print(5)
else:
    print(8)
