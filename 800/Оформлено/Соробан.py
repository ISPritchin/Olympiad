s = input()[::-1]
for c in s:
    c = int(c)
    if c < 5:
        print("O-|", end="")
    else:
        print("-O|", end="")
    t = ["O"]*5
    t[c % 5] = "-"
    print("".join(t))
