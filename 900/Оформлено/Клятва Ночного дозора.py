n = int(input())
a = list(map(int, input().split()))
min_a = min(a)
max_a = max(a)
r = 0
for x in a:
    if x != min_a and x != max_a:
        r += 1
print(r)
