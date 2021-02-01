n_sets = int(input())
for i in range(n_sets):
    a, b = [int(x) for x in input().split()]
    if a % b == 0:
        print("YES")
    else:
        print("NO")
