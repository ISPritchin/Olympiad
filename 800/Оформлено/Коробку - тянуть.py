n_sets = int(input())
for i in range(n_sets):
    x1, y1, x2, y2 = map(int, input().split())
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)
    if x1 == x2:
        print(delta_y)
    elif y1 == y2:
        print(delta_x)
    else:
        print(delta_x + delta_y + 2)

