x = int(input())
a = map(int, input().split())

s = 0
min_negative = float("inf")
n_odd = 0
for x in a:
    if x % 2 == 1:
        n_odd += 1
        min_negative = min(min_negative, x)
    s += x
if n_odd % 2 == 0:
    print(s)
else:
    print(s - min_negative)
