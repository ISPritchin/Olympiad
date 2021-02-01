n = int(input())
s = 0
for i in range(n):
    els = list(map(int, input().split()))
    for j in range(n):
        if i == j or j == n // 2 or j == n-i-1 or i == n // 2:
            s += els[j]
print(s)