n = int(input())
s = input()
arr = [0] * 10

left = 0
right = 9
for x in s:
    if x == "L":
        while arr[left] != 0:
            left += 1
        arr[left] += 1
    elif x == "R":
        while arr[right] != 0:
            right -= 1
        arr[right] += 1
    else:
        x = int(x)
        arr[x] = 0
        left = min(left, x)
        right = max(right, x)

for x in arr:
    print(x, end="")
