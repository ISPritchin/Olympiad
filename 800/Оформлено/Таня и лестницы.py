n = int(input())
n_l = 0
last = []

x_last = 0
is_first = True
for x in map(int, input().split()):
    if x == 1:
        n_l += 1
        if not is_first:
            last.append(x_last)
        is_first = False
    x_last = x

last.append(x_last)

print(n_l)
print(*last)
