n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

start = 1
end = start + a[0] - 1
i = 1
for x in b:
    while x > end:
        start = end + 1
        end = start + a[i] - 1
        i += 1
    if start <= x <= end:
        print(i, x - start + 1)
