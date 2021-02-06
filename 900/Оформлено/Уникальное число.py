n_sets = int(input())
for _ in range(n_sets):
    x = int(input())
    if x > 45:
        print(-1)
    else:
        r = ""
        i = 9
        while x != 0:
            r += str(min(i, x))
            x -= min(i, x)
            i -= 1
        print(r[::-1])
