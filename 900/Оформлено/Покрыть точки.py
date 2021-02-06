n_points = int(input())

r = 0
for _ in range(n_points):
    x, y = map(int, input().split())
    r = max(r, x+y)
print(r)
