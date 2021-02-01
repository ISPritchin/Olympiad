n, t = map(int, input().split())
arr = list(map(int, input().split()))
r = 0
x_last = None
for x in reversed(arr):
    if x_last is None or x_last - x <= t:
        r += 1
    else:
        break
    x_last = x
print(r)
