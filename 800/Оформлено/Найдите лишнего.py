n_points = int(input())
n_left = n_right = 0
for i in range(n_points):
    x, y = map(int, input().split())
    if x < 0:
        n_left += 1
    else:
        n_right += 1
if n_left == 1 or n_right == 1 or n_left == 0 or n_right == 0:
    print("YES")
else:
    print("NO")
