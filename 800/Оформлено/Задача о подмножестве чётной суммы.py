n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    arr = map(int, input().split())
    i1_1 = i1_2 = i0 = None
    for i, x in enumerate(arr, 1):
        if x % 2 == 0:
            i0 = i
            break
        else:
            if i1_1 is None:
                i1_1 = i
            else:
                i1_2 = i
                break
    if i0:
        print(1)
        print(i0)
    elif i1_1 and i1_2:
        print(2)
        print(i1_1, i1_2)
    else:
        print(-1)
