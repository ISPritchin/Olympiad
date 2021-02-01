from math import ceil

n, k = map(int, input().split())
a = [2*n, 5*n, 8*n]
a = map(lambda x: ceil(x / k), a)
print(sum(a))