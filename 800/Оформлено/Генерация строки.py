n_sets = int(input())
for _ in range(n_sets):
    n, k = map(int, input().split())
    for i in range(n):
        if i % 3 == 0:
            print("a", end="")
        elif i % 3 == 1:
            print("b", end="")
        else:
            print("c", end="")
    print()
