a, b = map(int, input().split())
x = y = z = 0
for i in range(1, 7):
    if abs(i-a) == abs(i-b):
        y += 1
    elif abs(i-a) < abs(i-b):
        x += 1
    else:
        z += 1
print(x, y, z)
