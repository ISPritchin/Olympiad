n_sets = int(input())
for _ in range(n_sets):
    x = int(input())
    assert x > 1
    if x % 2 == 0:
        print("1" * (x // 2))
    else:
        print("7" + "1" * (x // 2 - 1))