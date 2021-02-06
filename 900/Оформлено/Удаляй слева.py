a = input()
b = input()
i = 1
while len(a)-i >= 0 and len(b)-i >= 0 and a[len(a)-i] == b[len(b)-i]:
    i += 1
i -= 1
print(len(a) - i + len(b) - i)
