import re

n_sets = int(input())

for _ in range(n_sets):
    m, n, x, y = map(int, input().split())
    matrix = [input() for i in range(m)]
    # полностью покрываем плитками 1*1
    if 2 * x <= y:
        n = 0
        for row in matrix:
            n += row.count(".")
        print(n * x)
    # покрываем плитками 1*2 где это возможно, в остальных местах 1*1
    else:
        n1 = n2 = 0
        for row in matrix:
            rs = re.findall("\.+", row)
            for r in rs:
                n2 += len(r) // 2
                n1 += len(r) % 2
        print(n1 * x + n2 * y)
