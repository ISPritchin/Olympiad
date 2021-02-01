n = int(input())
for i in range(n):
    n, k = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()], reverse=True)
    for j in range(0, k):
        if a[j] < b[j]:
            a[j], b[j] = b[j], a[j]
    print(sum(a))
