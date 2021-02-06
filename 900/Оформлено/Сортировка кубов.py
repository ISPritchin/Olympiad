n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    a = list(map(int, input().split()))

    r = 0
    feq = False
    for i in range(1, n):
        if a[i - 1] < a[i]:
            print("YES")
            break
        elif a[i - 1] == a[i]:
            feq = True
    else:
        if feq:
            print("YES")
        else:
            print("NO")
