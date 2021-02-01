n_sets = int(input())
for i in range(n_sets):
    n = int(input())
    r = map(int, input())
    b = map(int, input())
    balance = 0
    for x, y in zip(r, b):
        if x > y:
            balance += 1
        elif x < y:
            balance -= 1

    if balance > 0:
        print("RED")
    elif balance < 0:
        print("BLUE")
    else:
        print("EQUAL")
