n_sets = int(input())
for _ in range(n_sets):
    n_digits = int(input())
    n8 = n_digits // 4 + int(n_digits % 4 != 0)
    n9 = n_digits - n8
    print("9"*n9 + "8"*n8)