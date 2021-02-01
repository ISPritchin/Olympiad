n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    s = input()
    n_br = 0
    for i in reversed(range(n)):
        if s[i] == ")":
            n_br += 1
        else:
            break
    if n_br > n-n_br:
        print("Yes")
    else:
        print("No")
