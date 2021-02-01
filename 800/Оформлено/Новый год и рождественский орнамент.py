y, b, r = map(int, input().split())
y -= 1
b -= 2
r -= 3
print(min(y, b, r)*3+6)