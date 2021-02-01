import re

n = int(input())
s = list(map(len, re.findall("B+", input())))
print(len(s))
if len(s) > 0:
    print(*s)
