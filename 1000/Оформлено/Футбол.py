n_goal = int(input())

a = 1
b = 0
a_name = input()
b_name = ""

for i in range(n_goal-1):
    x = input()
    if x == a_name:
        a += 1
    else:
        b_name = x
        b += 1

if a > b:
    print(a_name)
else:
    print(b_name)
