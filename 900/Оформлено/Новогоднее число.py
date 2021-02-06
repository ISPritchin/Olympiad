n_sets = int(input())
for _ in range(n_sets):
    n = int(input())
    n2021 = n % 2020
    n2020 = (n - n2021) // 2020 - n2021
    if n2020 >= 0 and 2020 * n2020 + 2021 * n2021 == n :
        print("YES")
    else:
        print("NO")