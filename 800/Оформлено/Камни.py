n_sets = int(input())
for i in range(n_sets):
    a, b, c = map(int, input().split())

    y = min(b, c // 2)
    x = min(a, (b - y) // 2)
    s1 = 3 * (x + y)

    y = min(a, b // 2)
    x = min(b-y*2, c // 2)
    s2 = 3 * (x + y)

    print(max(s1, s2))
