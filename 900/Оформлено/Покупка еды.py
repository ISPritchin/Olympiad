n_sets = int(input())
for _ in range(n_sets):
    x = int(input())
    s = 0
    while x >= 10:
        n = x // 10
        s += x // 10 * 10
        x %= 10
        x += n
    s += x
    print(s)