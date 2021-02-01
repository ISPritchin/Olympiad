n = int(input())
x, y = map(int, input().split())

A = x + y - 2
B = (n - x) + (n - y)
if A <= B:
    print("White")
else:
    print("Black")
