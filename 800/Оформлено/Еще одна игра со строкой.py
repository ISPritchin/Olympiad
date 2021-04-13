n_sets = int(input())
for _ in range(n_sets):
    s = input()
    for i, x in enumerate(s):
        if i % 2 == 0:
            if x == "a":
                print("b", end="")
            else:
                print("a", end="")
        else:
            if x == "z":
                print("y", end="")
            else:
                print("z", end="")
    print()
