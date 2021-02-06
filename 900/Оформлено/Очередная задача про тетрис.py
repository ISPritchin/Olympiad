n_sets = int(input())
for _ in range(n_sets):
    _ = int(input())
    a = list(map(int, input().split()))
    have_n0 = have_n1 = False
    for x in a:
        if x % 2 == 0:
            have_n0 = True
        else:
            have_n1 = True
        if have_n0 and have_n1:
            print("NO")
            break
    else:
        print("YES")
