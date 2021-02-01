n_sets = int(input())
for _ in range(n_sets):
    n_coff = int(input())
    weights = [int(x) for x in input().split()]
    w1 = len([x for x in weights if x == 1])
    w2 = len([x for x in weights if x == 2])
    if w1 % 2 == 0 and w2 % 2 == 0:
        print("YES")
    elif w2 % 2 == 1 and w1 >= 2 and w1 % 2 == 0:
        print("YES")
    else:
        print("NO")