n, k = map(int, input().split())
for i in range(n):
    for j in range(n):
        if i != j:
            print(1, end=' ')
        else:
            print(k-n+1, end=' ')
    print()
