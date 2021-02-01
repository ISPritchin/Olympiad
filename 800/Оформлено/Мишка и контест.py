n, k = map(int, input().split())
arr = list(map(int, input().split()))
left = right = -1
for i, x in enumerate(arr):
    if x > k:
        if left == -1:
            left = i
        right = i

if left == right == -1:
    print(n)
else:
    print(n - (right - left + 1))
