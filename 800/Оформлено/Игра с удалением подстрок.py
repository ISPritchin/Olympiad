import re

n_sets = int(input())

for _ in range(n_sets):
    s = input()
    s = sorted(re.findall("1+", s), reverse=True)
    s = sum(map(len, s[::2]))
    print(s)
