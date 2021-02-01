n_sets = int(input())
for _ in range(n_sets):
    n, k = map(int, input().split())
    i = 1
    j = 0
    while i <= n:
        print(chr(ord('a') + j), end="")
        j = (j+1) % k
        i += 1
    print()