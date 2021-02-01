n = int(input())
s = ["o"] * n
f1 = 1
f2 = 1
while f2 <= n:
    s[f2-1] = "O"
    f1, f2 = f2, f1+f2
print("".join(s))

