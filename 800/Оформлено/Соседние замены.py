n = int(input())
arr = map(int, input().split())
for x in arr:
    print(x - int(x % 2 == 0), end=" ")
