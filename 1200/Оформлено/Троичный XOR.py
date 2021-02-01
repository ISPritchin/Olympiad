n_sets = int(input())

for _ in range(n_sets):
    n_digits = int(input())
    x = input()
    a = ""
    b = ""
    count = 0
    for d in x:
        count += 1
        if d in "02":
            a += str(int(d) // 2)
            b += str(int(d) // 2)
        else:
            a += "0" + x[count:]
            b += "1" + "0" * len(x[count:])
            break
    print(a)
    print(b)
