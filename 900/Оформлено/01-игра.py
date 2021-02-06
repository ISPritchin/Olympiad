n_sets = int(input())
for _ in range(n_sets):
    s = input()
    n0 = s.count("0")
    n1 = s.count("1")
    nh = min(n0, n1)

    if nh % 2 == 0:
        print("NET")
    else:
        print("DA")
