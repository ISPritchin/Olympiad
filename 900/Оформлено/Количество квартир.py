n_sets = int(input())
for _ in range(n_sets):
    x = int(input())
    if x in [1, 2, 4]:
        print(-1)
    else:
        flag = False
        for i in range(0, x // 3 + 1):
            r = x - 3*i
            for j in range(0, r // 5 + 1):
                r2 = r - 5*j
                if r2 % 7 == 0:
                    print(i, j, r2 // 7)
                    flag = True
                    break
            if flag:
                break
