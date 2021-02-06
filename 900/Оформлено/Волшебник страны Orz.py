n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    if n == 1:
        print(9)
    elif n == 2:
        print(98)
    else:
        print(989, end="")
    for j in range(n-3):
        print(j % 10, end="")
    print()