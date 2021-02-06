n = int(input())
s = input()
i = len(s) // 2 + 1 - int(len(s) % 2 == 0)

j = 1
r = [""] * n
while 1 <= i <= len(s):
    r[i-1] = s[j-1]
    if j % 2 == 1:
        i += j
    else:
        i -= j
    j += 1

if len(s) % 2 == 1:
    print("".join(r)[::-1])
else:
    print("".join(r))
