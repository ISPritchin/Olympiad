n_rows = int(input())
data = [input() for i in range(n_rows)]
flag = 1
for i, row in enumerate(data):
    if "OO|" in row:
        data[i] = data[i].replace("OO|", "++|")
        break
    elif "|OO" in row:
        data[i] = data[i].replace("|OO", "|++")
        break
else:
    flag = 0
    print("NO")
if flag:
    print("YES")
    print("\n".join(data))
