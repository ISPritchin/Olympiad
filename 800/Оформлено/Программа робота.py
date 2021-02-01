for i in range(int(input())):
    x, y = map(int, input().split())
    max_xy = max(x, y)
    min_xy = min(x, y)
    if max_xy - min_xy <= 1:
        print(max_xy + min_xy)
    else:
        print(min_xy*2 + 1 + (max_xy-min_xy-1)*2)
