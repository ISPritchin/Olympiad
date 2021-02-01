from math import  ceil

n, x = map(int, input().split())
arr = map(int, input().split())
print(ceil(abs(sum(arr)) / x))
