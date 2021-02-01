a, b, c = [int(x) for x in input().split()]
print(min([
    a+b+c,
    a+a+b+b,
    a+a+c+c,
    b+b+c+c
]))