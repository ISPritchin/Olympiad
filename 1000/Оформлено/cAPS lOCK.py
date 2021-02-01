x = input()
if x[0].islower() and len(x) == 1 or x[0].islower() and len(x) > 1 and x[1:].isupper() or x.isupper():
    for a in x:
        if a.islower():
            print(a.upper(), end="")
        else:
            print(a.lower(), end="")
else:
    print(x)