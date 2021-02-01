from math import ceil

a = sum([int(x) for x in input().split()])
b = sum([int(x) for x in input().split()])
n = int(input())
if n >= ceil(a / 5) + ceil(b / 10):
    print("YES")
else:
    print("NO")
