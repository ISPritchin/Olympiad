n, current_x = map(int, input().split())
n_sad = 0
for x in range(n):
    op, x = input().split()
    x = int(x)
    if op == "+":
        current_x += x
    else:
        if current_x - x < 0:
            n_sad += 1
        else:
            current_x -= x
print(current_x, n_sad)
