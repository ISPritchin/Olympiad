def check_stat():
    flag = True
    n = int(input())
    pl = sl = -1
    for i in range(n):
        p, s = map(int, input().split())
        delta_p = p - pl  # 0
        delta_s = s - sl  # 1
        if delta_s > delta_p or pl > p or sl > s:
            flag = False
        pl = p
        sl = s
    return flag


n_sets = int(input())
for i in range(n_sets):
    if check_stat():
        print("YES")
    else:
        print("NO")
