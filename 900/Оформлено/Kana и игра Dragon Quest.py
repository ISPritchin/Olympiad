n_sets = int(input())
for _ in range(n_sets):
    x, n, m = map(int, input().split())
    if x > 20:
        for i in range(n):
            x = x // 2 + 10
            if x == 20:
                break
    x -= 10*m
    if x <= 0:
        print("YES")
    else:
        print("NO")
