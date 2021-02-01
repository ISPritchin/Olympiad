N_SETS = int(input())

for i in range(N_SETS):
    a, b, c, n = [int(x) for x in input().split()]
    M = max(a, b, c)
    eq = 3 * M - a - b - c
    if (n - eq) % 3 == 0 and n - eq >= 0:
        print("YES")
    else:
        print("NO")
