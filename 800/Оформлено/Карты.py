n = int(input())
arr = list(map(int, input().split()))
mean = sum(arr) / len(arr)

r = []
for i, x in enumerate(arr, 1):
    r.append((x, i))
r.sort()

for i in range(len(arr) // 2):
    print(r[i][1], r[-i-1][1])
