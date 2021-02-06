n = int(input())
s = input()
ws = s.split()

r_max = 0
for w in ws:
    r = 0
    for l in w:
        if l.isupper():
            r += 1
    r_max = max(r, r_max)

print(r_max)
