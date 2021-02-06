s = input()
if len(s) % 2 == 1:
    current = len(s) // 2
else:
    current = len(s) // 2 - 1

for i in range(len(s)):
    print(s[current], end="")
    if i % 2 == 0:
        current += i + 1
    else:
        current -= i + 1