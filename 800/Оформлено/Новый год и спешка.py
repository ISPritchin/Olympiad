n_minutes = 240
a, b = [int(x) for x in input().split()]
n_minutes -= b
n = 0
time_cost = 5
while n_minutes >= time_cost and n < a:
    n_minutes -= time_cost
    time_cost += 5
    n += 1
print(n)
