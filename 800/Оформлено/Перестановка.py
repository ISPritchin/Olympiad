for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = map(int, input().split())
    if sum(arr) == m:
        print("YES")
    else:
        print("NO")
