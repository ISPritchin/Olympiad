n_sets = int(input())

for i in range(n_sets):
    a = input()
    b = input()
    c = input()
    for x, y, z in zip(a, b, c):
        if (x == y != z) or (x != y and x != z and y != z):
            print("NO")
            break
    else:
        print("YES")
