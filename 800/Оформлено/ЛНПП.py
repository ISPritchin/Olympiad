s = input()
a = [0] * 26
for x in s:
    a[ord(x)-ord('a')] += 1

for i in reversed(range(26)):
    if a[i] != 0:
        break

c = chr(ord('a') + i)
print(c * s.count(c))
