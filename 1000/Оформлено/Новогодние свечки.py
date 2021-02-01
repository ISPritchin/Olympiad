a, b = map(int, input().split())

n_hours = 0
n_parts = 0
while a != 0:
    n_hours += a
    n_parts += a
    a = n_parts // b
    n_parts = n_parts % b

print(n_hours)