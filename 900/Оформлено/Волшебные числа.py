x = input()
i = len(x)-1
while i != -1:
    if x[i] == '1':
        i -= 1
    elif x[i-1: i+1] == "14":
        i -= 2
    elif x[i-2: i+1] == "144":
        i -= 3
    else:
        print("NO")
        break
else:
    print("YES")
