s = input()
c1 = 0
c2 = 0
for x in s:
    if x.isupper():
        c1 += 1
    else:
        c2 +=1
if c2 >= c1:
    print(s.lower())
else:
    print(s.upper())
