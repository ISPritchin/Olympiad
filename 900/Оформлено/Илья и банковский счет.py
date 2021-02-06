x = int(input())
if x >= 0:
    print(x)
else:
    s = str(x)
    if abs(x) < 10 or abs(x) < 100 and abs(x) % 10 == 0:
        print(0)
    else:
        a = int(s[-2])
        b = int(s[-1])
        if a > b:
            print(s[:-2] + s[-1:])
        else:
            print(s[:-1])

