n_sets = int(input())

for i in range(n_sets):
    n, k = map(int, input().split())
    if n == k:
        print("YES")
        for i in range(k):
            print(1, end=" ")
        print()
    elif n % 2 == 0:
        if k * 2 <= n:
            print("YES")
            for i in range(k - 1):
                print(2, end=" ")
            print(n - 2 * (k - 1))
        elif k % 2 == 0 and (k - 1) + 3 <= n:
            print("YES")
            for i in range(k - 1):
                print(1, end=" ")
            print(n - k + 1)
        else:
            print("NO")
    elif n % 2 == 1:
        if k > n or k % 2 == 0:
            print("NO")
        else:
            print("YES")
            for i in range(k - 1):
                print(1, end=" ")
            print(n - k + 1)
