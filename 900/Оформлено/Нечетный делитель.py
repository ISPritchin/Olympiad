n_sets = int(input())
for _ in range(n_sets):
    x = int(input())
    if x & (x-1) != 0:
        print("YES")
    else:
        print("NO")
