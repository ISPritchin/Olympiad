n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print(2, end="")
        print("3" * (n-1))
