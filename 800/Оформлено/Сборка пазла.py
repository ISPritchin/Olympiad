n_sets = int(input())
for i in range(n_sets):
    a, b = [int(x) for x in input().split()]
    if a == 1 or b == 1 or a == b == 2:
        print("YES")
    else:
        print("NO")
