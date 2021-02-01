n_sets = int(input())

for _ in range(n_sets):
    x = int(input())
    if x == 1:
        print(0)
    elif x == 2:
        print(1)
    elif x % 2 == 0 or x == 3:
        print(2)
    else:
        print(3)
