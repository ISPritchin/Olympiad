n_sets = int(input())

for _ in range(n_sets):
    n = int(input())
    if n == 2:
        print(2)
    elif n % 2 == 1:
        print(1)
    else:
        print(0)
