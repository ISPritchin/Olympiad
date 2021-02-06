d = {
    'q': 9,
    'r': 5,
    'b': 3,
    'n': 3,
    'p': 1,
    'k': 0
}

white = 0
black = 0
for i in range(8):
    s = input()
    for x in s:
        if x == ".":
            continue
        if x.islower():
            black += d[x]
        else:
            white += d[x.lower()]

if black > white:
    print("Black")
elif black == white:
    print("Draw")
else:
    print("White")
