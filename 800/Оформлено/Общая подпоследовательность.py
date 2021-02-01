n_sets = int(input())
for i in range(n_sets):
    _ = input()
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for x in a:
        if x in b:
            print("YES")
            print(1, x)
            break
    else:
        print("NO")
