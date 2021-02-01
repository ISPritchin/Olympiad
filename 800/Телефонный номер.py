n_sets = int(input())
for i in range(n_sets):
    n_digits = int(input())
    s = input()
    i8 = s.find("8")
    n_digits_in_number = n_digits - i8
    if i8 == -1 or n_digits_in_number < 11:
        print("NO")
    else:
        print("YES")
