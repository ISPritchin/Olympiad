n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    arr = list(map(int, input().split()))
    s_arr = sum(arr)
    nz = arr.count(0)
    if nz > 0:
        if s_arr + nz == 0:
            print(nz + 1)
        else:
            print(nz)
    else:
        if s_arr == 0:
            print(1)
        else:
            print(0)
