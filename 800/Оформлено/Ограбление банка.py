n, a, b = map(int, input().split())
_ = input()
arr = map(int, input().split())

count = 0
for x in arr:
    if a < x < b:
        count += 1
print(count)