n = int(input())
s = list(input())
r = 0
for i in range(0, n, 2):
    a = s[i]
    b = s[i+1]
    if a == 'a' and b == 'b' or a == 'b' and b == 'a':
        continue
    if a == 'a' and b == 'a':
        s[i] = 'b'
        r += 1
    elif a == 'b' and b == 'b':
        s[i] = 'a'
        r += 1

print(r)
print("".join(s))
