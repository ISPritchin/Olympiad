n_sets = int(input())
for _ in range(n_sets):
    h, w, n = [int(x) for x in input().split()]
    nh = nw = 0
    while h % 2 == 0:
        h //= 2
        nh += 1
    while w % 2 == 0:
        w //= 2
        nw += 1
    if (2**nh)*(2**nw) >= n:
        print("YES")
    else:
        print("NO")
