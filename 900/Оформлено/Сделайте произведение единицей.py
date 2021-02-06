n = input()


a = list(map(int, input().split()))
s = 0
neg = 0
n_zeros = 0
for x in a:
    if x < 0:
        neg += 1
        s += -1 - x
    elif x > 0:
        s += x - 1
    else:
        n_zeros += 1

if neg % 2 == 0 or n_zeros != 0:
    print(s + n_zeros)
else:
    print(s + 2)
