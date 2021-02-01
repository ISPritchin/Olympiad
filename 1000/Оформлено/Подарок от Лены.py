n = int(input())
for i in range(n+1):
    s = ' ' * (2*(n-i))
    for j in range(i+1):
        s += f"{j} "
    for j in reversed(range(0, i)):
        s += f"{j} "
    s = s[:-1]
    print(s)

for i in reversed(range(n)):
    s = ' ' * (2*(n-i))
    for j in range(i+1):
        s += f"{j} "
    for j in reversed(range(0, i)):
        s += f"{j} "
    s = s[:-1]
    print(s)
