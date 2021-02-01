n = int(input())
arr = list(map(int, input().split()))
s = ((sum(arr[::3]), "chest"), (sum(arr[1::3]), "biceps"), (sum(arr[2::3]), "back"))
print(max(s)[1])
