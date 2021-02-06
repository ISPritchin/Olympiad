n = int(input())
a = list(map(int, input().split()))

a0 = []
a1 = []
for x in a:
    if x % 2 == 0:
        a0.append(x)
    else:
        a1.append(x)

a0.sort(reverse=True)
a1.sort(reverse=True)

len0 = len(a0)
len1 = len(a1)
min_l = min(len0, len1)
print(sum(a0[min_l+1:]) + sum(a1[min_l+1:]))