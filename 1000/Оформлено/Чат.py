s = input()
letters = "hello"

i = 0
for c in s:
    if c == letters[i]:
        i += 1
        if i == 5:
            break

if i == 5:
    print("YES")
else:
    print("NO")
