n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
print(sum(arr[a-1:b-1]))
