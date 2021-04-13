b, k = map(int, input().split())
a = list(map(int, input().split()))
a = a[::-1
    ]
res = 0
if a[0] % 2 != 0:
    res = (res + 1) % 2

for k in a[1:]:
    if b % 2 == 1 and k % 2 == 1:
        res = (res + 1) % 2

if res:
    print("odd")
else:
    print("even")
