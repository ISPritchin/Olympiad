n = int(input())
a = list(map(int, input().split()))
np = nm = 0
for x in a:
    if x > 0:
        np += 1
    elif x < 0:
        nm += 1

if 2*np >= len(a):
    print(1)
elif 2*nm >= len(a):
    print(-1)
else:
    print(0)
