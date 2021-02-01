x = input()
digits = map(int, list(x))
res = 0
first_digit = True
for x in digits:
    if x == 9 and first_digit:
        res = 9
    elif x >= 5:
        res = res * 10 + (9-x)
    else:
        res = res * 10 + x
    first_digit = False
print(res)