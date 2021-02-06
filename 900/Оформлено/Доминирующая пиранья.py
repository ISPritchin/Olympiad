n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    a = list(map(int, input().split()))
    max_ = max(a)
    for i, x in enumerate(a):
        if x == max_:
            if i > 0 and a[i-1] < x or i < n-1 and a[i+1] < x:
                print(i+1)
                break
    else:
        print(-1)
