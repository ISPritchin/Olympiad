n = int(input())
a = [0] * 101
c = map(int, input().split())
for x in c:
    a[x] = 1

n = 0
for i in range(1, 101):
    if a[i] == 1:
        n += 1
        for j in range(i, 101, i):
            a[j] = 0
print(n)