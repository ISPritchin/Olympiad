n = int(input())
a = list(map(int, input().split()))
i1 = a.index(min(a))
i2 = a.index(max(a))
i1, i2 = min(i1, i2), max(i1, i2)
print(max(i2, n-i1-1))
