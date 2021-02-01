N_SETS = int(input())
for i in range(N_SETS):
    n, s = [int(x) for x in input().split()]
    if n == 1:
        print(0)
    elif n == 2:
        print(s)
    else:
        print(s*2)
