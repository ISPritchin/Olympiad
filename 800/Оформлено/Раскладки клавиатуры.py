a = input()
b = input()
ad = {_a: _b for _a, _b in zip(a, b)}
s = input()
for x in s:
    if x.lower().isdigit():
        print(x, end="")
    else:
        p = ad[x.lower()]
        if x.islower():
            print(p, end="")
        else:
            print(p.upper(), end="")

