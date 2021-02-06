def is_good(m, i, j):
    if m[i][j] == 1:
        return True
    n = len(m)
    for k in range(n):
        for l in range(n):
            if m[k][j] + m[i][l] == m[i][j]:
                return True
    return False


n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

flag_no = False
for i in range(n):
    for j in range(n):
        if not is_good(m, i, j):
            print("No")
            flag_no = True
            break
    if flag_no:
        break
else:
    print("Yes")
