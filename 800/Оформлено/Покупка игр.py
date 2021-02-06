n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

i = 0
r = 0
current_b = a[0]
for x in c:
    if current_b >= x:
        r += 1
        i += 1
        if i != len(a):
            current_b = a[i]
        else:
            break
print(r)