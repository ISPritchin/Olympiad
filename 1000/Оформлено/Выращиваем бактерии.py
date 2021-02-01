x = int(input())
n = 0
while x > 0:
    if x % 2 == 1:
        x -= 1
        n += 1
    else:
        x //= 2
print(n)
