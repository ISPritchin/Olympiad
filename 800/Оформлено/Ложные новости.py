s = input()
w = "heidi"
pos = [0] * len(w)
i = j = 0

while i < len(w) and j < len(s):
    if w[i] == s[j]:
        pos[i] = j
        i += 1
    j += 1

if i == len(w):
    print("YES")
else:
    print("NO")
