n_sets = int(input())
for i in range(n_sets):
    n, c0, c1, h = map(int, input().split())
    s = input()
    n0 = s.count("0")
    n1 = s.count("1")
    if c0 + h < c1:
        print(n1 * h + n * c0)
    elif c0 == c1:
        print(c0 * n)
    elif c0 > c1 + h:
        print(n0 * h + n * c1)
    else:
        print(n0*c0 + n1*c1)

