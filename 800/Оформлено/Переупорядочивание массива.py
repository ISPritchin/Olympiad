n_sets = int(input())
for _ in range(n_sets):
    n, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    for _a, _b in zip(a, b):
        if _a + _b > x:
            print("NO")
            break
    else:
        print("YES")
    if _ != n_sets-1:
        input()