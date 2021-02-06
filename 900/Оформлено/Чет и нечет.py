m, index = [int(x) for x in input().split()]
if m % 2 == 0:
    if index <= m // 2:
        print(index*2-1)
    else:
        index -= m // 2
        print(index*2)
else:
    if index <= m // 2 + 1:
        print(index*2-1)
    else:
        index -= m // 2 + 1
        print(index*2)
