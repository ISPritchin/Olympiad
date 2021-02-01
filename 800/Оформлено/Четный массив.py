def read_arr():
    return [int(x) for x in input().split()]


n = int(input())
for i in range(n):
    n = int(input())
    a = read_arr()
    n_bad_odd = n_bad_even = 0
    for i, x in enumerate(a):
        if i % 2 == 0:
            if x % 2 != 0:
                n_bad_odd += 1
        else:
            if x % 2 == 0:
                n_bad_even += 1
    if n_bad_odd == n_bad_even == 0:
        print(0)
    elif n_bad_odd == n_bad_even:
        print(n_bad_odd)
    else:
        print(-1)