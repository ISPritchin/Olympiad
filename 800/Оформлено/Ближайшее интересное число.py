def sum_of_digit(x):
    return sum(map(int, str(x)))


x = int(input())
while True:
    if sum_of_digit(x) % 4 == 0:
        print(x)
        break
    x += 1
