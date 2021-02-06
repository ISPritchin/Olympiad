n_sets = int(input())
for _ in range(n_sets):
    n, a, b = map(int, input().split())
    for i in range(n):
        print(chr((ord('a') + i % b) ), end="")
    print("")
