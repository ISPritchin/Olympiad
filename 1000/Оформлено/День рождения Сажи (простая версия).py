n = int(input())
a = list(map(int, input().split()))
a.sort()
if len(a) % 2 == 1:
    print(len(a) // 2)
    for i in range(0, len(a) // 2):
        print(a[len(a) // 2 + i], a[i], end=" ")
    print(a[-1])
else:
    print(len(a) // 2 - 1)
    for i in range(0, len(a) // 2):
        print(a[len(a) // 2 + i], a[i], end=" ")
