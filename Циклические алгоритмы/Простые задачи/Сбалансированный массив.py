n = int(input())
for i in range(n):
    x = int(input())
    half = x // 2
    if half % 2 == 1:
        print("NO")
    else:
        print("YES")
        for i in range(half):
            print(2 * (i+1), end=" ")
        for i in range(half-1):
            print(2 * (i+1)-1, end=" ")
        print(2 * (i+2)-1 + half)
