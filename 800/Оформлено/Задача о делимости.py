n_sets = int(input())
for i in range(n_sets):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        print((a // b + 1) * b - a)
