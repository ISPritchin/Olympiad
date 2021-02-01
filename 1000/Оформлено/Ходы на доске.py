n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    assert n % 2 == 1
    if n == 1:
        n_p = -1
    else:
        n_p = n // 2
    print((4*n_p*(n_p+1)*(2*n_p+1)) // 3)
