def proc_set():
    current = 0
    _min = 0

    _ = int(input())
    s = input()
    for x in s:
        if x == "(":
            current += 1
        else:
            current -= 1
            _min = min(_min, current)

    print(-_min)


n_sets = int(input())
for i in range(n_sets):
    proc_set()
