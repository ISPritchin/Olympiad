n_sets = int(input())
for _ in range(n_sets):
    x, y = map(int, input().split())
    delta = x - y
    if delta != 1:
        print("YES")
    else:
        print("NO")
