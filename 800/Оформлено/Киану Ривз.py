n = int(input())
s = input()
if len(s) % 2 == 1 or s.count("1") != s.count("0"):
    print(1)
    print(s)
else:
    print(2)
    print(s[0], s[1:])
