n, m = map(int, input().split())
r_min = n // m
r_max = r_min + int(n % m != 0)
n_min = m - n % m
n_max = m - n_min
for i in range(n_min):
    print(r_min, end=" ")
for i in range(n_max):
    print(r_max, end=" ")
